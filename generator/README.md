# Story-page generator — notes

Generates every page in `website/stories/` (18 pages currently) from one template. Plain Python 3, standard library only — no dependencies to install.

## How it works

```
generator/build.py        page content (PAGES dict) + image URLs (IMG dict)
generator/template.html   shared page shell (nav, hero, footer, GA tag)
        │
        └── python3 generator/build.py  →  website/stories/*.html
```

`build.py` takes `template.html` and, for each entry in `PAGES`, substitutes six placeholders, then writes the file into `website/stories/`:

| Placeholder | Meaning |
|---|---|
| `{{TITLE}}` | `<title>` text (suffix "— Budots Media PH" comes from the template) |
| `{{DESC}}` | Meta description |
| `{{HERO}}` | Hero background image URL (usually an `IMG[...]` entry) |
| `{{H1}}` | Hero heading — may contain `<br>` for line breaks |
| `{{KICKER}}` | Small line under the H1 |
| `{{BODY}}` | Article HTML |

## Rules

- **Never edit `website/stories/*.html` directly.** Every run of `build.py` rewrites all of them — direct edits are silently overwritten. Content changes go in `PAGES` in `build.py`; layout/head changes (analytics, fonts, nav) go in `template.html`.
- `website/index.html` is **not** generated — it is maintained by hand. Anything added to the template head (like the Google Analytics tag, `G-0QY44NZW9Y`, added 2026-07-05) must be mirrored in `index.html` manually, and vice versa.
- After editing, run from the repo root: `python3 generator/build.py` — then commit the regenerated pages together with the generator change. Pushing to `main` auto-deploys via GitHub Pages.

## Sitemap

`python3 generator/sitemap.py` regenerates `website/sitemap.xml` (all landing pages + stories, `<lastmod>` from each file's last git commit). Run it after adding or renaming pages, before pushing.

## Adding a story page

1. Add an entry to `PAGES` in `build.py`:
   ```python
   PAGES["my-story.html"] = dict(
       TITLE="My Story", H1="My<br>Story",
       KICKER="Client — Year", HERO=IMG["beach"],
       DESC="One-sentence meta description.",
       BODY=f"""
   <p class="kicker">Section label</p>
   <p class="lead">Opening paragraph.</p>
   <p>Body text…</p>
   {img('collage', 'alt text')}
   <blockquote>Pull quote.</blockquote>
   """)
   ```
2. Run `python3 generator/build.py`.
3. Add a story card linking to it in `website/index.html` (`#stories` section), and an entry in `website/sitemap.xml`.

## Body conventions

- CSS classes from `website/css/main.css`: `kicker` (small label), `lead` (large opening paragraph), plain `<p>`, `<blockquote>` for pull quotes.
- Images: add the URL to the `IMG` dict and use the `img('key', 'alt')` helper — it adds `loading="lazy"`. Hero photos are currently hotlinked from external CDNs (see `instructions/build-notes-reference.md`); logos are local under `assets/img/logos/`.
- Unverified facts: write the page as a styled draft and mark the spot with `<p><em>[Draft — add facts via .md file in instructions/]</em></p>` — same policy as `plank-g.html` and `cinduy-wedding.html`.

## History

Merged 2026-07-05 from three earlier batch scripts (`stories/build*.py`); output verified byte-identical before the old scripts were deleted. Design/content decisions are logged in `instructions/build-notes-reference.md`.
