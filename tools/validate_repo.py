#!/usr/bin/env python3
"""Dependency-free static checks for the Meridian Indicators repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

from repo_utils import (
    BARE_WEB_TARGET_PATTERN,
    is_external_markdown_target,
    iter_repository_files,
    split_markdown_target,
)

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def load_manifest() -> dict:
    path = ROOT / "manifest.json"
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"manifest.json cannot be read: {exc}")
        return {"indicators": []}


def check_manifest(manifest: dict) -> None:
    seen_ids: set[str] = set()
    seen_sources: set[str] = set()
    for item in manifest.get("indicators", []):
        indicator_id = item.get("id", "")
        source = item.get("source", "")
        documentation = item.get("documentation", "")
        version = item.get("version", "")

        if not indicator_id or indicator_id in seen_ids:
            fail(f"manifest indicator id is missing or duplicated: {indicator_id!r}")
        seen_ids.add(indicator_id)

        if not source or source in seen_sources:
            fail(f"manifest source is missing or duplicated: {source!r}")
        seen_sources.add(source)

        source_path = ROOT / source
        doc_path = ROOT / documentation
        if not source_path.is_file():
            fail(f"manifest source does not exist: {source}")
            continue
        if not doc_path.is_file():
            fail(f"manifest documentation does not exist: {documentation}")

        text = source_path.read_text(encoding="utf-8")
        expected_header = f"// {item.get('name')} · v{version}"
        if expected_header not in text.splitlines()[:5]:
            fail(f"source metadata does not match manifest: {source}")
        if "setups" in indicator_id and f'const string VERSION = "{version}"' not in text:
            fail(f"setup VERSION constant does not match manifest: {source}")

    actual_sources = {
        str(path.relative_to(ROOT)).replace("\\", "/")
        for path in (ROOT / "src").rglob("*.pine")
    }
    unlisted = sorted(actual_sources - seen_sources)
    if unlisted:
        fail(f"Pine sources missing from manifest: {', '.join(unlisted)}")


def strip_strings(text: str) -> str:
    return re.sub(r'"(?:\\.|[^"\\])*"', '""', text)


def check_pine_files() -> None:
    for path in sorted((ROOT / "src").rglob("*.pine")):
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()

        if not lines or lines[0] != "//@version=6":
            fail(f"{rel}: first line must be //@version=6")
        if len(lines) < 3 or lines[1] != "// SPDX-License-Identifier: MPL-2.0":
            fail(f"{rel}: missing SPDX header")

        comments = [index + 1 for index, line in enumerate(lines) if line.lstrip().startswith("//")]
        if comments != [1, 2, 3]:
            fail(f"{rel}: source comments must be limited to the three-line metadata header")

        cleaned = strip_strings(text)
        for opening, closing in (("(", ")"), ("[", "]"), ("{", "}")):
            balance = 0
            for char in cleaned:
                if char == opening:
                    balance += 1
                elif char == closing:
                    balance -= 1
                    if balance < 0:
                        fail(f"{rel}: unmatched {closing}")
                        break
            if balance != 0:
                fail(f"{rel}: unbalanced {opening}{closing} delimiters ({balance})")

        for line_number, line in enumerate(lines, 1):
            if line.rstrip(" \t") != line:
                fail(f"{rel}: trailing whitespace on line {line_number}")

        if re.search(r"-v\d", path.name):
            fail(f"{rel}: public source filenames must remain versionless")
        if any(marker in text for marker in ("YOUR_USERNAME", "TODO", "FIXME", "HACK")):
            fail(f"{rel}: contains a release placeholder or unfinished marker")

        imports = re.findall(r"(?m)^import\s+([^\s]+)", text)
        for dependency in imports:
            if dependency != "TradingView/ta/12":
                fail(f"{rel}: unreviewed Pine dependency {dependency}")


def markdown_links(text: str) -> list[str]:
    return [match.group(1).strip() for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", text)]


def check_markdown_links() -> None:
    markdown_files = sorted(
        path for path in iter_repository_files(ROOT, text_only=True) if path.suffix.lower() == ".md"
    )
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for raw_target in markdown_links(text):
            target, _ = split_markdown_target(raw_target)
            target_without_fragment = target.split("#", 1)[0]
            if not target_without_fragment or is_external_markdown_target(target):
                continue
            if BARE_WEB_TARGET_PATTERN.fullmatch(target):
                fail(
                    f"{path.relative_to(ROOT)}: external link is missing a URL scheme: "
                    f"{raw_target} (use https://{target})"
                )
                continue

            local = (path.parent / unquote(target_without_fragment)).resolve()
            try:
                local.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"{path.relative_to(ROOT)}: link escapes repository: {raw_target}")
                continue
            if not local.exists():
                fail(f"{path.relative_to(ROOT)}: broken local link: {raw_target}")


def normalize_setup(text: str) -> str:
    replacements = {
        '"Meridian — Futures Setups Research"': '"Meridian — Futures Setups"',
        'shorttitle = "Meridian Setups Research"': 'shorttitle = "Meridian Futures Setups"',
        "// Meridian — Futures Setups Research · v0.3.6-beta": "// Meridian — Futures Setups · v0.3.6-beta",
        "const bool RESEARCH_BUILD = true": "const bool RESEARCH_BUILD = false",
        'bool showAllResearchZones = input.bool(true, "Show active research zones"': 'bool showAllResearchZones = input.bool(false, "Show active research zones"',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def check_setup_parity() -> None:
    daily = (ROOT / "src/futures/meridian-futures-setups.pine").read_text(encoding="utf-8")
    research = (ROOT / "src/futures/meridian-futures-setups-research.pine").read_text(encoding="utf-8")
    if normalize_setup(daily) != normalize_setup(research):
        fail("Futures Setups daily and research builds differ outside approved build toggles")


def check_release_hygiene() -> None:
    required = [
        "README.md",
        "LICENSE",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "DISCLAIMER.md",
        "manifest.json",
        "docs/getting-started.md",
        "docs/architecture.md",
        "docs/data-integrity.md",
        "docs/troubleshooting.md",
        "tools/format_repo.py",
    ]
    for rel in required:
        if not (ROOT / rel).exists():
            fail(f"required release file is missing: {rel}")

    forbidden_fragments = ("v0.3.0-beta", "meridian-futures-setups-legacy", "YOUR_USERNAME")
    validator_path = Path(__file__).resolve()
    utility_path = (ROOT / "tools/repo_utils.py").resolve()

    for path in iter_repository_files(ROOT, text_only=True):
        resolved = path.resolve()
        if resolved in {validator_path, utility_path}:
            continue

        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), 1):
            if line.rstrip(" \t") != line:
                fail(f"{path.relative_to(ROOT)}: trailing whitespace on line {line_number}")
        if text and not text.endswith("\n"):
            fail(f"{path.relative_to(ROOT)}: missing final newline")
        if "\r" in text:
            fail(f"{path.relative_to(ROOT)}: non-LF line endings detected")
        for fragment in forbidden_fragments:
            if fragment in text:
                fail(f"{path.relative_to(ROOT)}: stale release fragment {fragment!r}")


def main() -> int:
    manifest = load_manifest()
    check_manifest(manifest)
    check_pine_files()
    check_markdown_links()
    check_setup_parity()
    check_release_hygiene()

    if ERRORS:
        print(f"Validation failed with {len(ERRORS)} issue(s):")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    source_count = len(list((ROOT / "src").rglob("*.pine")))
    document_count = len(
        [path for path in iter_repository_files(ROOT, text_only=True) if path.suffix.lower() == ".md"]
    )
    print(f"Validation passed: {source_count} Pine sources, {document_count} Markdown files.")
    print("Note: static validation does not replace TradingView compilation or market-data testing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
