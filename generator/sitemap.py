#!/usr/bin/env python3
# Sitemap generator for the Budots Media PH site.
# Run from the repo root:  python3 generator/sitemap.py
# Writes website/sitemap.xml with per-page <lastmod> taken from git history.
import pathlib
import subprocess

BASE = "https://barts83eu.github.io/budotsmediaph-202606-fable5/"
ROOT = pathlib.Path(__file__).parent.parent
WEB = ROOT / "website"


def lastmod(path):
    out = subprocess.run(
        ["git", "log", "-1", "--format=%cs", "--", str(path.relative_to(ROOT))],
        capture_output=True, text=True, cwd=ROOT,
    ).stdout.strip()
    return out or subprocess.run(
        ["git", "log", "-1", "--format=%cs"], capture_output=True, text=True, cwd=ROOT
    ).stdout.strip()


pages = [("", WEB / "index.html")]
for d in ("stories", "projects", "ai", "showcase", "partners"):
    if (WEB / d / "index.html").exists():
        pages.append((f"{d}/", WEB / d / "index.html"))
for f in sorted((WEB / "stories").glob("*.html")):
    if f.name != "index.html":
        pages.append((f"stories/{f.name}", f))

lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
]
for rel, f in pages:
    lines += [
        "  <url>",
        f"    <loc>{BASE}{rel}</loc>",
        f"    <lastmod>{lastmod(f)}</lastmod>",
        "  </url>",
    ]
lines.append("</urlset>")
(WEB / "sitemap.xml").write_text("\n".join(lines) + "\n")
print(f"wrote website/sitemap.xml — {len(pages)} URLs")
