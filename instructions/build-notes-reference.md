# Build Notes / Thought Process — Budots Media PH Website
_Reference doc. 2026-07-04. Generated during site build._

## Structure decision
- Static site, no framework, no build step → publish anywhere.
- `website/index.html` = parallax homepage; each story = standalone page in `website/stories/`.
- Shared `css/main.css` + `js/main.js`. `website/` contains only publishable files.
- Generator lives in `generator/` (moved out of website/ 2026-07-05; the three batch scripts merged into one): `generator/build.py` + `generator/template.html` → writes `website/stories/*.html`. Add a story by adding a PAGES entry and rerunning `python3 generator/build.py`. Merge verified byte-identical (md5 930369bf…) before deleting the old `stories/build*.py` + `_template.txt`.

## Style (per budotsmedisph-instructions.md)
- Black→white top-to-bottom gradient on `body`.
- Font: Bebas Neue (Google Fonts) as free stand-in for Bebas Neue Pro (commercial); CSS falls back to Bebas Neue Pro if installed.
- Parallax: `data-parallax="speed"` attribute on any `.bg` layer; JS translates on rAF.
- Scroll indicators: top progress bar, mouse-wheel icon in hero, right-side section dots (hidden on mobile).
- Particles: canvas, drift + sine sway, yellow link-lines, fades out as page scrolls toward white zone.
- Mobile-first: svh units, clamp() type, cards auto-fit grid.

## Assets (all hotlinked — sandbox blocks binary downloads; download locally later if self-hosting)
- Official logo SVG + OC6 boat PNG + DJI drone PNG + client logos (POCC, Island Buzz, Akaw, Cebu News, Gatorade, Harley Cebu, Kalanggaman, Motul) + JPARK/NUSTAR/LGU/maps photos: `cdn.prod.website-files.com` (budotsmedia.webflow.io)
- Paddle Forward drone photos (credited Budots Media): `cdn.shopify.com` via atlascommune.com article
- Photogrammetry collage, DOT7/games/phone screenshots, beach, Cebu News: `bartsakwerda.com/wp-content`
- Olango practice hero: Google Photos lh3 og-image (album QdRjTnqiYMBqMCBT9)
- budotsmediaph_logo.png: kalanggaman.com

## Content sources
- History facts: bartsakwerda.com/budots-media + budotsmediaph.com/about + instructions md (2014 founding post-Haiyan, 2015 Maribago, 2016–2020 London Hackney/Camden, 2020 Lapu-Lapu production house, post-ChatGPT AI pivot, PL structural funds, DOT/DOT7/BYD/JPARK/NUSTAR portfolio, 8 languages).
- Big Canoe / Buzzy Budlong / Olango: atlascommune.com "Big Canoe, Bigger Dream" (photos credited Budots Media) + Google Photos album title "PFC 2021-06-01 Practice Olango".
- Ironman: 2024 IM 70.3 Lapu-Lapu (Apr 21, Mactan Newtown, CCLEX, 1,385 athletes / 54 countries, Schoeman & Visser).
- GameDev Summit: real event — Feb 2024 Boracay, DTI + GameOps + GDAP, 300+ participants / 72 companies / 32 countries; 2025 at The Lind & Sea Wind, Station 1.
- budotsmediaph.co fetched; content folded in **with all references to M.A. removed** (also excluded team-photo asset whose filename contains his name).

## Editorial decisions (flag for owner review)
- `brand-protection.html`: tells the impersonation story WITHOUT naming the individual and without nationality generalizations. Reason: publishing criminal accusations against a named, never-prosecuted person = defamation exposure; generalization would undercut the Filipino-LLM brand. Name can be added by owner at own risk — marked spot in page.
- `plank-g.html` (Mary Grace) and `cinduy-wedding.html` (2026 Cinduy Cinco): no public info found → written as styled drafts with clearly marked `[Draft — add facts via .md]` notes. Drop .md files in instructions/ to extend.
- `ai-agents.html`: opinion piece, framed as "move people up the stack" not pure replacement triumphalism.

## Pending / next
- Replace hotlinks with local `assets/img/` copies before production (curl the URL list above from a normal machine).
- Maps subpage could get an interactive Leaflet/D3 Philippines map (instructions mention maps specialization) — currently editorial page only.
- Facebook post links couldn't be fetched (login wall) — wedding/practice FB embeds to add manually if wanted.
- Verify in a real browser: `open website/index.html`.

## 2026-07-04/05 update — projects-by-budotsmedisa.md ingested
- New source file `instructions/projects-by-budotsmedisa.md` listed additional projects/initiatives; `instructions/articles.md` was created empty (no content to fold in yet).
- Added `stories/build3.py` generating three new pages:
  - `brides-of-triton.html` — JPARK Island Resort's Triton Grand Ballroom wedding expo, produced by Budots Media PH. Web-verified: running annually since 2012, Facebook video credits "JPark Wedding Expo 'Brides of Triton' by Budots Media Ph". Written with confidence, no draft marker.
  - `dot7-eskrima-tour.html` — FMA7/DOT7 Filipino Martial Arts tourism program, real (Cebu = Eskrima birthplace, WEKAF 1989 games, 30+ FMA systems in Central Visayas per web search). Client "TudTud" and 2022 tour specifics from the .md are unverified — marked `[Draft — ...]` per the same policy as `plank-g.html`/`cinduy-wedding.html`.
  - `community-initiatives.html` — founder Bart Sakwerda's non-Budots ventures: Philippines Travel Company (real, founded 2015 Maribago per web search), Cebu Chatbot Dev Meetup (real, Dec 2017, DATA OPS Philippines per web search), Cebu Japanese Meetup (from .md only, not independently verified — stated plainly, no fabricated detail added).
- `ironman.html` extended with a paragraph on the 2022 Savoy Hotel Mactan client project (Nevian Sanchez, Robert Tatii) — kept clearly separate from the 2024 public IM 70.3 Lapu-Lapu race already covered, since these are two different Ironman-branded activities.
- `lapulapu-projects.html` extended with a "long haul" paragraph: Camiguin Resorts long-term coverage + DOT7 media library stewardship.
- `index.html`: added 3 new story cards, a portfolio line for Savoy Hotel/Camiguin Resorts and long-term relationships, and LinkedIn (`linkedin.com/in/bartsakwerda`) + X (`x.com/bartsakwerda`) links in the footer, per the .md.
## 2026-07-05 update — logos localized (assets.md)
- Binary downloads now work in the sandbox (they didn't during the original build), so the "replace hotlinks" pending item is done for logos: 38 files in `website/assets/img/logos/`, all resized ≤600px and referenced locally.
- Sources per `instructions/assets.md`: budotsmediaph.co client-logo gallery (Wix) + the webflow CDN logos the site already used. Pinterest profile blocked (JS-only page); "Green Concept Cebu" has no resolvable domain — nothing fetched from those two.
- The Wix HTML's filename→media-id metadata was unreliable (titles shifted several positions — e.g. the file named `rkBYD.png` is actually the Cordova seal), so every logo was identified **visually** via dark-background contact sheets before naming. Final names in `assets/img/logos/` are trustworthy; original Wix titles are not.
- New client logos found and added to a `logowall` grid on index (CSS in main.css): DOT, JPark, NUSTAR, **Savoy Hotel Mactan Newtown** (matches the 2022 Ironman client), Mactan Newtown, Megaworld, Belmont Hotel, **Nouveau Resort Camiguin** (matches the Camiguin Resorts long-term work), Brides at Triton, BYD, Harley (white), CCLEX, Cordova, Aboitiz Foundation, JPMorganChase, Accenture, Dexcom, Ascendion, Conduent, Foundever, Aetrex, Condura, Paramount Life, Primer Group, IPG Mediabrands, ODV Creative, Gordon Ramsay F&C, Street Burger, Haejeok Hopping, Aquila Legis + the original webflow set (POCC, Island Buzz, Akaw, Cebu News, Kalanggaman, Gatorade, Motul).
- Chip backgrounds: most .co logos are white-on-transparent → `on-dark` chips; dark/photo logos (Cordova seal, Gordon Ramsay fish, jpgs) → `on-light` chips.
- Excluded from the fetch: budotsmediaph.co's 13 team photos (`image_2025-11-11_*`) per the standing M.A./team-photo exclusion policy, and the .co site's own camera-icon logo (our brand mark stays the official webflow SVG, now local at `assets/img/logos/budotsmedia-logo.svg`, used in index + story-template nav).
- Hero/story photos are still hotlinked — only logos were localized this pass.

- Attempted to fetch GREEN CONCEPTS CEBU and the linked YouTube channel (`UCq7YUYIdRcTE7oIslPAYTUA`) for more projects — YouTube blocked by a consent-wall redirect, Green Concepts Cebu's domain didn't resolve. Web search only surfaced "Green Concepts and Events," a separate Cebu event-planning company with no confirmed Budots Media link — not folded in. Owner should supply the correct URL/handle if more content is wanted from there.
