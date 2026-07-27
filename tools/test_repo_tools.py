#!/usr/bin/env python3
"""Regression tests for repository hygiene and file traversal."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from format_repo import process_repository
from repo_utils import iter_repository_files


class RepositoryToolTests(unittest.TestCase):
    def test_version_control_internals_are_excluded(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "README.md").write_text("# Test\n", encoding="utf-8")
            git_object = root / ".git" / "objects" / "aa" / "object"
            git_object.parent.mkdir(parents=True)
            git_object.write_bytes(b"binary payload with spaces   \x00\xff")

            files = {path.relative_to(root).as_posix() for path in iter_repository_files(root)}

            self.assertEqual(files, {"README.md"})

    def test_formatter_repairs_safe_text_hygiene_issues(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            readme = root / "README.md"
            readme.write_bytes(b"# Test  \r\n\r\n[Site](google.com)\t\r\n")

            changes = process_repository(root, write=True)

            self.assertEqual(len(changes), 1)
            self.assertEqual(changes[0].trailing_whitespace_lines, 2)
            self.assertEqual(changes[0].bare_links_fixed, 1)
            self.assertEqual(readme.read_text(encoding="utf-8"), "# Test\n\n[Site](https://google.com)\n")
            self.assertEqual(process_repository(root, write=False), [])


if __name__ == "__main__":
    unittest.main()
