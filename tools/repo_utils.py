#!/usr/bin/env python3
"""Shared repository-file and text-normalization helpers."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Iterator

IGNORED_DIRECTORIES = frozenset(
    {
        ".git",
        ".hg",
        ".svn",
        ".mypy_cache",
        ".pytest_cache",
        ".ruff_cache",
        ".tox",
        ".venv",
        "__pycache__",
        "build",
        "dist",
        "node_modules",
        "venv",
    }
)

TEXT_SUFFIXES = frozenset(
    {
        ".cfg",
        ".css",
        ".csv",
        ".editorconfig",
        ".gitattributes",
        ".gitignore",
        ".html",
        ".ini",
        ".js",
        ".json",
        ".md",
        ".pine",
        ".py",
        ".sh",
        ".toml",
        ".ts",
        ".txt",
        ".xml",
        ".yaml",
        ".yml",
    }
)

TEXT_FILENAMES = frozenset(
    {
        ".editorconfig",
        ".gitattributes",
        ".gitignore",
        "CODEOWNERS",
        "Dockerfile",
        "LICENSE",
        "Makefile",
        "NOTICE",
    }
)

MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
BARE_WEB_TARGET_PATTERN = re.compile(
    r"^(?:www\.)?(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+"
    r"[A-Za-z]{2,63}(?::\d{1,5})?(?:[/?#][^\s]*)?$"
)
URI_SCHEME_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


def is_text_file(path: Path) -> bool:
    """Return whether a repository file is safe to process as UTF-8 text."""
    return path.name in TEXT_FILENAMES or path.suffix.lower() in TEXT_SUFFIXES


def iter_repository_files(root: Path, *, text_only: bool = False) -> Iterator[Path]:
    """Yield repository files while pruning VCS, dependency and build internals."""
    root = root.resolve()
    for current, directories, filenames in os.walk(root):
        directories[:] = sorted(
            directory for directory in directories if directory not in IGNORED_DIRECTORIES
        )
        current_path = Path(current)
        for filename in sorted(filenames):
            path = current_path / filename
            if path.is_symlink() or not path.is_file():
                continue
            if text_only and not is_text_file(path):
                continue
            yield path


def split_markdown_target(raw_target: str) -> tuple[str, str]:
    """Split a Markdown link destination from its optional title suffix."""
    stripped = raw_target.strip()
    if not stripped:
        return "", ""
    if stripped.startswith("<"):
        closing = stripped.find(">")
        if closing != -1:
            return stripped[1:closing], stripped[closing + 1 :]
    parts = stripped.split(maxsplit=1)
    target = parts[0]
    suffix = f" {parts[1]}" if len(parts) == 2 else ""
    return target, suffix


def is_external_markdown_target(target: str) -> bool:
    """Return whether a Markdown destination is already explicitly external."""
    return bool(
        target.startswith(("#", "//"))
        or URI_SCHEME_PATTERN.match(target)
    )


def normalize_bare_markdown_links(text: str, *, source_path: Path, root: Path) -> tuple[str, int]:
    """Prefix likely external bare-domain links with HTTPS when no local path exists."""
    fixes = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal fixes
        raw_target = match.group(1)
        target, title_suffix = split_markdown_target(raw_target)
        if not target or is_external_markdown_target(target):
            return match.group(0)
        if not BARE_WEB_TARGET_PATTERN.fullmatch(target):
            return match.group(0)

        local_candidate = (source_path.parent / target).resolve()
        try:
            local_candidate.relative_to(root.resolve())
        except ValueError:
            pass
        else:
            if local_candidate.exists():
                return match.group(0)

        fixes += 1
        prefix_length = match.start(1) - match.start(0)
        suffix_length = match.end(0) - match.end(1)
        prefix = match.group(0)[:prefix_length]
        suffix = match.group(0)[len(match.group(0)) - suffix_length :] if suffix_length else ""
        return f"{prefix}https://{target}{title_suffix}{suffix}"

    return MARKDOWN_LINK_PATTERN.sub(replace, text), fixes


def normalize_text(text: str) -> tuple[str, int]:
    """Normalize line endings, strip trailing horizontal whitespace and add one final newline."""
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = normalized.split("\n")
    changed_lines = 0

    for index, line in enumerate(lines):
        stripped = line.rstrip(" \t")
        if stripped != line:
            lines[index] = stripped
            changed_lines += 1

    while lines and lines[-1] == "":
        lines.pop()
    normalized = "\n".join(lines) + "\n"
    return normalized, changed_lines
