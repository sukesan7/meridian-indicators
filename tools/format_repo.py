#!/usr/bin/env python3
"""Apply deterministic, safe text hygiene fixes to repository files."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

from repo_utils import iter_repository_files, normalize_bare_markdown_links, normalize_text

DEFAULT_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class FileChange:
    path: Path
    trailing_whitespace_lines: int
    bare_links_fixed: int


def process_repository(root: Path, *, write: bool) -> list[FileChange]:
    """Check or rewrite supported text files and return the files needing changes."""
    root = root.resolve()
    changes: list[FileChange] = []

    for path in iter_repository_files(root, text_only=True):
        try:
            original = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError as exc:
            raise RuntimeError(f"Expected UTF-8 text in {path.relative_to(root)}: {exc}") from exc

        formatted, trailing_count = normalize_text(original)
        bare_link_count = 0
        if path.suffix.lower() == ".md":
            formatted, bare_link_count = normalize_bare_markdown_links(
                formatted,
                source_path=path,
                root=root,
            )

        if formatted == original:
            continue

        changes.append(
            FileChange(
                path=path.relative_to(root),
                trailing_whitespace_lines=trailing_count,
                bare_links_fixed=bare_link_count,
            )
        )
        if write:
            path.write_text(formatted, encoding="utf-8", newline="\n")

    return changes


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Normalize supported repository text files. Version-control internals, binaries, "
            "dependencies and build outputs are always excluded."
        )
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Report changes without writing files.")
    mode.add_argument("--write", action="store_true", help="Apply safe formatting fixes in place.")
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_ROOT,
        help="Repository root. Defaults to the parent of tools/.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(f"Repository root does not exist: {root}", file=sys.stderr)
        return 2

    try:
        changes = process_repository(root, write=args.write)
    except (OSError, RuntimeError) as exc:
        print(f"Formatting failed: {exc}", file=sys.stderr)
        return 2

    if not changes:
        print("Repository text hygiene passed; no changes required.")
        return 0

    action = "Updated" if args.write else "Would update"
    for change in changes:
        details: list[str] = []
        if change.trailing_whitespace_lines:
            details.append(f"{change.trailing_whitespace_lines} trailing-whitespace line(s)")
        if change.bare_links_fixed:
            details.append(f"{change.bare_links_fixed} bare external link(s)")
        if not details:
            details.append("line endings or final newline")
        print(f"{action} {change.path}: {', '.join(details)}")

    if args.check:
        print(f"Text hygiene failed: {len(changes)} file(s) require formatting.")
        print("Run: python tools/format_repo.py --write")
        return 1

    print(f"Text hygiene complete: updated {len(changes)} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
