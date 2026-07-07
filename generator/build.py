#!/usr/bin/env python3
# Story page generator for the Budots Media PH site.
# Edit PAGES below, then run:  python3 generator/build.py
# Output goes to website/stories/<slug>/index.html (template: generator/template.html),
# plus a redirect stub at website/stories/<slug>.html for the old flat URLs.
# Story-specific assets live next to the page in website/stories/<slug>/assets/.
# NOTE: website/stories/dream-keeper/ is hand-authored (custom parallax page) —
# it is not in PAGES and this script never touches it.
import pathlib

D = pathlib.Path(__file__).parent
T = (D / "template.html").read_text()
OUT = D.parent / "website" / "stories"

# ---- batch 1: history, AI, drones, maps, canoe, portraits, ironman, brand ----

IMG = {
    "canoe_hero": "https://cdn.shopify.com/s/files/1/0531/1099/7154/files/20210613_-_DRONE_DAY2_-072_1_2048x2048.jpg?v=1625890534",
    "canoe_sumilon": "https://cdn.shopify.com/s/files/1/0531/1099/7154/files/20210621_-_DRONE_DAY3_PHOTOS_SUMILON_-039_2048x2048.jpg?v=1625890843",
    "canoe_d2a": "https://cdn.shopify.com/s/files/1/0531/1099/7154/files/20210613_-_DRONE_DAY2_-007_2048x2048.jpg?v=1625890308",
    "canoe_d5": "https://cdn.shopify.com/s/files/1/0531/1099/7154/files/20210616-Paddle_Forward_Cebu_Day_5-034_2048x2048.jpg?v=1625890233",
    "canoe_d2b": "https://cdn.shopify.com/s/files/1/0531/1099/7154/files/20210613_-_DRONE_DAY2_-005_2048x2048.jpg?v=1625890160",
    "canoe_crew": "https://cdn.shopify.com/s/files/1/0531/1099/7154/files/RAP_4732_2048x2048.jpg?v=1625890069",
    "canoe_d5b": "https://cdn.shopify.com/s/files/1/0531/1099/7154/files/20210617_-_DRONE_PHOTOS_DAY5_-024_2048x2048.jpg?v=1625889292",
    "canoe_d5c": "https://cdn.shopify.com/s/files/1/0531/1099/7154/files/20210617_-_DRONE_PHOTOS_DAY5_-026_2048x2048.jpg?v=1625889332",
    "canoe_finish": "https://cdn.shopify.com/s/files/1/0531/1099/7154/files/RAP_5128_2048x2048.jpg?v=1625891741",
    "canoe_coast": "https://cdn.shopify.com/s/files/1/0531/1099/7154/files/20210613_-_DRONE_DAY2_-043_2048x2048.jpg?v=1625889218",
    "collage": "https://bartsakwerda.com/wp-content/uploads/2023/08/bart-sakwerda-drone-photogrammetry-portfolio.png",
    "beach": "https://bartsakwerda.com/wp-content/uploads/2023/06/201831b3-cb2a-4471-ac83-29bc2869c269.jpg",
    "cebunews": "https://bartsakwerda.com/wp-content/uploads/2024/05/417186906_814731500666278_48153751899014281_n.jpg",
    "phone": "https://bartsakwerda.com/wp-content/uploads/2023/09/screenshot-2023-12-19-155931.png",
    "games": "https://bartsakwerda.com/wp-content/uploads/2024/04/screenshot-2024-04-07-163128.png",
    "agency": "https://bartsakwerda.com/wp-content/uploads/2023/07/screenshot-2023-07-03-230051.png",
    "jpark": "https://static.wixstatic.com/media/acad74_8a4330c55256451797c1d925232d3b17~mv2.jpg/v1/fit/w_2500,h_1330,al_c/acad74_8a4330c55256451797c1d925232d3b17~mv2.jpg",
}

def img(key, alt=""):
    return f'<img src="{IMG[key]}" alt="{alt}" loading="lazy">'

PAGES = {}

PAGES["history"] = dict(
    TITLE="Our History", H1="Twelve Years,<br>Three Continents",
    KICKER="2014 — Today", HERO=IMG["beach"],
    DESC="The history of Budots Media: founded 2014 in Cebu by Bart Sakwerda, expanded 2020 in Lapu-Lapu City, pivoted to AI.",
    BODY=f"""
<p class="kicker">The Story</p>
<p class="lead">BUDOTS MEDIA was born in 2014, in the rehabilitation period after Typhoon Haiyan tore through Cebu Province. Bart Sakwerda, with a background in media production and an eye on the country's exploding appetite for video, opened a small production shop — first in Budlaan, then Banilad.</p>
<p>In 2015 the office moved to Maribago, Lapu-Lapu City, the island home it has kept ever since. From 2016 to 2020 the company also ran BUDOTS MEDIA LONDON from Hackney and Camden High Street, serving European clients while the Cebu team served Asia.</p>
{img('collage','3D scans and drone photogrammetry portfolio across Asia and the Middle East')}
<p>Then came 2020. While much of the industry shut down, Budots Media expanded — setting up a full production house in Lapu-Lapu City in the middle of the pandemic. The bet paid off: when borders reopened, the team was already delivering for the Philippines Department of Tourism, DOT Region 7 (FMA7 Filipino Martial Arts, RIDE7 motorsports, DIVE7 scuba), BYD, JPARK Island Resort and NUSTAR.</p>
<blockquote>Every crisis in our history became an expansion: Haiyan gave us a reason to exist, COVID gave us a production house, and ChatGPT gave us a new industry.</blockquote>
<p>The release of OpenAI's ChatGPT marked the third turn. Budots Media moved beyond video production into AI — with the development of a sovereign Filipino language model and a multimodal generative model as its stated priority. Growth markets: Arabia, India and Southeast Asia, backed by access to European Structural Funds through BUDOTS MEDIA POLAND and a presence in London.</p>
<p>The team works in eight languages — English, Cebuano, Tagalog, Japanese, Polish, Chinese, Thai and Arabic — and in every medium: film, drones, photogrammetry, maps, graphs, animation and games.</p>
""")

PAGES["ai-filipino-llm"] = dict(
    TITLE="A Sovereign Filipino Language Model", H1="AI That Speaks<br>Cebuano",
    KICKER="Sovereign AI", HERO=IMG["phone"],
    DESC="Budots Media's priority project: a sovereign Filipino language model and multimodal generative AI.",
    BODY=f"""
<p class="kicker">Why Sovereign</p>
<p class="lead">Over 180 languages are spoken in the Philippines. Almost none of them are meaningfully represented in the world's frontier AI models. Budots Media's priority project is a sovereign Filipino language model — built in the Philippines, for Filipino languages, under Filipino control.</p>
<p>Frontier models handle Tagalog passably and Cebuano poorly. Waray, Hiligaynon, Bikol — barely at all. A nation of 110+ million people risks running its digital life on models that neither understand its languages nor answer to its institutions. Sovereignty here is practical, not political: education, government services, news and commerce all need AI that works in the languages people actually speak.</p>
{img('cebunews','Cebu News - short form video content and news brand')}
<p>Our starting position is unusual for an AI lab: a decade of original, rights-cleared multimedia in Cebuano and Tagalog. Thousands of hours of interviews, voiceovers, subtitled films and news footage from our own productions — training data most labs cannot buy.</p>
<blockquote>We spent ten years accidentally building the dataset. Now we are deliberately building the model.</blockquote>
<p>The roadmap runs from a text model for Cebuano and Tagalog toward a multimodal generative model — speech, image and video — trained on our archive. The AI pivot began right after the release of ChatGPT, and is funded through commercial production work, growth markets in Arabia, India and SE Asia, and European Structural Funds via BUDOTS MEDIA POLAND.</p>
""")

PAGES["ai-agents"] = dict(
    TITLE="AI Agents in the Edit Bay", H1="Replacing the<br>Edit Bay",
    KICKER="Production 2.0", HERO=IMG["games"],
    DESC="How Budots Media replaces traditional video editing seats and virtual assistants with AI agents.",
    BODY=f"""
<p class="kicker">Opinion — Production 2.0</p>
<p class="lead">For a decade we ran a classic production house: editors on timelines, virtual assistants on inboxes and spreadsheets. In 2023 we started replacing both with AI agents. Not assisting — replacing.</p>
<p>The economics are blunt. A rough cut that took an editor two days now takes an agent pipeline twenty minutes: automatic transcription in Cebuano, Tagalog and English, silence and filler removal, multicam sync by audio fingerprint, subtitle generation in eight languages, thumbnail variants scored against engagement history. A human still makes the final creative pass — one senior editor now ships what five juniors used to.</p>
<blockquote>The job that disappears is not "editor". It is "person who does what software can now do". The editor who remains is a director.</blockquote>
<p>The same happened to the virtual assistant layer. Scheduling, client follow-ups, PhilGEPS bid monitoring, invoice chasing, social posting across brands — agent workflows run them around the clock, in every language we operate in. What used to be four VA seats is now one operations lead supervising agents.</p>
<p>We say this as a Philippine company, aware of what BPO and VA work means to this economy. Our answer is not denial — it is to move our own people up the stack: from cutting footage to directing agents, from answering email to owning outcomes. The alternative is that someone else's agents do it to us.</p>
<p>This conviction is also why we build rather than only buy: the same archive that trains our sovereign Filipino model will train agents that understand a Cebu client brief without translation.</p>
""")

PAGES["drone-aerial"] = dict(
    TITLE="Drones & Aerial Surveys", H1="The View<br>From Above",
    KICKER="Aerial Data Ops", HERO=IMG["collage"],
    DESC="Drone cinematography, aerial surveys, photogrammetry and gaussian splats across Asia and the Middle East.",
    BODY=f"""
<p class="kicker">Aerial</p>
<p class="lead">Budots Media flies. Licensed drone operations, aerial surveys, laser scanning and photogrammetry — delivered under the Aerial Data Ops brand from Cebu to Riyadh.</p>
<p>The portfolio spans a coal-fired power plant survey, the Diriyah construction site in Riyadh, SM Seaside in Cebu, a drone show in Dubai, Sentosa in Singapore, Malaysia's National Stadium, Palawan's islands and the Putra Mosque in Kuala Lumpur — captured as 3D scans, gaussian splats and photogrammetry models, not just pretty footage.</p>
{img('collage','Collage of 3D drone scans: Riyadh, Cebu, Dubai, Singapore, Malaysia, Palawan, Kuala Lumpur')}
<p>The same aircraft shoot our stories. The drone photographs in our Paddle Forward expedition coverage — an outrigger canoe threading Cebu's coastline, shot from above at dawn — were all Budots Media captures.</p>
{img('canoe_d2a','Drone shot of OC6 outrigger canoe off Cebu, by Budots Media')}
<p>Survey work feeds the map work: orthomosaics and elevation models become the base layers of our Philippine cartography, and scan data becomes assets in our games production.</p>
""")

PAGES["maps"] = dict(
    TITLE="Philippines in Maps", H1="The Philippines,<br>Mapped",
    KICKER="Cartography · Data", HERO=IMG["canoe_d5b"],
    DESC="Budots Media specializes in Philippines maps, graphs and animated data visualization.",
    BODY=f"""
<p class="kicker">Maps &amp; Data</p>
<p class="lead">Budots Media specializes in maps of the Philippines — and in the graphs and animations that make data legible. An archipelago of 7,641 islands is a cartographer's problem before it is anything else.</p>
<p>Our map work runs from tourism cartography (island guides for Kalanggaman.com and the Philippines Travel Company) to survey-grade products: drone orthomosaics, elevation models and 3D scans from Aerial Data Ops rendered into interactive maps.</p>
{img('canoe_d5c','Aerial coastline of Cebu by Budots Media')}
<p>The house style is animated: routes that draw themselves, choropleths that breathe, expedition tracks replayed over terrain. When the Philippine Outrigger Canoe Club paddled 227 km around Cebu, our drones and maps told the story leg by leg — Talisay, Moalboal, Sumilon — as moving cartography.</p>
<blockquote>In a country where the sea should be a highway, a good map is an argument.</blockquote>
<p>Graphs and animation carry the same weight in our client work — tourism statistics for DOT campaigns, MICE event data for our directory, market data for AI investors. If it has coordinates or numbers, we can make it move.</p>
""")

PAGES["big-canoe"] = dict(
    TITLE="Big Canoe, Bigger Dream", H1="Big Canoe,<br>Bigger Dream",
    KICKER="Community · 227 KM Around Cebu", HERO=IMG["canoe_hero"],
    DESC="Five days, 227 kilometers around Cebu in a six-man outrigger canoe. Expedition coverage by Budots Media.",
    BODY=f"""
<p class="kicker">Expedition — June 2021</p>
<p class="lead">On the 123rd Independence Day of the Philippines, three pickups, one six-man zero-fuel outrigger canoe and a land-and-water crew set off from Cebu South Road Properties for five days of paddling. 227 kilometers later they emerged in Moalboal. Budots Media flew the drones.</p>
{img('canoe_d2a','OC6 outrigger canoe off the Cebu coast, drone photo by Budots Media')}
<p>Long-distance ocean paddling is unheard of in the Philippines — ironic for a country where water should be a highway, not a divider. Fisherfolk waved at the passing canoe shouting "paspasa sa dragon boat!" — the closest craft they knew. It is not a dragon boat. It is an OC6, fabricated in Cebu by the Philippine Outrigger Canoe Club's founders Buzzy Budlong, Janus Migalbin and Faye Jimera.</p>
{img('canoe_sumilon','The expedition passing Sumilon, drone photo by Budots Media')}
<p>The crew — dragon boat paddlers, triathletes, a 16-year-old — covered up to 60 km a day in 15 km relay legs, through heavy rain, zero-visibility legs and a tailing tropical depression, relying on wind, tide and each other.</p>
<blockquote>"I will show them that Filipinos have more dignity, more courage, more honor." — the Luna line the organizers carried in their heads.</blockquote>
{img('canoe_d5','Paddle Forward Cebu, day five, by Budots Media')}
<p>The expedition doubled as advocacy: for coastal communities flattened by the pandemic, for marine sanctuaries, and for Cebu as the future paddling capital of the Philippines. Kids on the shore shouted "We want to bugsay!" — we want to paddle.</p>
{img('canoe_finish','Expedition crew at the finish, by Budots Media')}
<p><em>All expedition photography by Budots Media. Story originally told with Atlas — <a href="https://atlascommune.com/blogs/community/big-canoe-bigger-dream" style="color:var(--accent)">read the full interview</a>.</em></p>
""")

PAGES["buzzy-budlong"] = dict(
    TITLE="Buzzy Budlong", H1="Buzzy<br>Budlong",
    KICKER="Portrait · The Paddler of Cebu", HERO=IMG["canoe_crew"],
    DESC="Portrait of Buzzy Budlong — paddler, canoe builder, founder of Island Buzz and the Philippine Outrigger Canoe Club.",
    BODY=f"""
<p class="kicker">Portrait</p>
<p class="lead">If outrigger canoeing returns to the Philippines as a living culture, it will be substantially one man's fault. Buzzy Budlong has been paddling Cebu's waters since 1998 and building the boats himself since 1999.</p>
<p>He came to the water through the I Love The Ocean movement and the Coastal Resources Management Program — weekends paddling after work, until the weekends won. In 2009 he set out on the expedition that defines him: 88 days, Sarangani to Pagudpud, paddling the length of the Philippines. "That was when I confirmed just how beautiful our country is, how beautiful our coastlines are, our culture."</p>
{img('canoe_d2b','OC6 at sea, drone photo by Budots Media')}
<p>In 2002 he built Island Buzz — a café in the middle of Cebu City that felt like a Hawaiian coastline, paddle craft hung on the walls — and later Island Buzz tours. In 2016 he began fabricating the OC6, the six-man outrigger: a boat you can take your ohana in, faster to learn, made for bringing people along rather than racing alone.</p>
<blockquote>"Being a paddler, you're like a bird or a drone. You appreciate the beauty of the land." — Buzzy Budlong</blockquote>
<p>With Janus Migalbin and Faye Jimera he founded the Philippine Outrigger Canoe Club, and in 2021 led the 227 km Paddle Forward expedition around Cebu — which Budots Media documented from the air. His stated mission: make Cebu the paddling capital of the Philippines. "The bigger the canoe, the bigger the dream."</p>
""")

PAGES["plank-g"] = dict(
    TITLE="Mary Grace — Plank G", H1="Plank G",
    KICKER="Portrait · Mary Grace", HERO=IMG["canoe_d5"],
    DESC="Portrait of Mary Grace, known as Plank G.",
    BODY=f"""
<p class="kicker">Portrait</p>
<p class="lead">Mary Grace — known in the community as Plank G — is one of the athletes Budots Media follows and supports in Cebu's growing grassroots fitness and endurance scene.</p>
<p>Budots Media backs local sport the way it backs local language: because culture grows from the ground up. From the Philippine Outrigger Canoe Club's expeditions to triathlon coverage, the camera goes where local athletes are doing hard things quietly — and Plank G's story is part of that thread.</p>
<blockquote>Support for local sports is not sponsorship. It is documentation — proof that it happened, proof that it matters.</blockquote>
<p><em>[This profile is a draft — add facts, quotes and photos for Mary Grace via an .md file in the instructions folder and the page will be extended.]</em></p>
""")

PAGES["ironman"] = dict(
    TITLE="Ironman Philippines", H1="Ironman<br>Philippines",
    KICKER="Endurance · Lapu-Lapu City", HERO=IMG["canoe_coast"],
    DESC="Ironman 70.3 Lapu-Lapu: the Philippines' biggest triathlon, raced from Mactan across the CCLEX.",
    BODY=f"""
<p class="kicker">Endurance</p>
<p class="lead">The IRONMAN 70.3 returned to Cebu in 2024 as IRONMAN 70.3 Lapu-Lapu — a 1.9 km ocean swim, 90 km bike and 21.1 km run beginning on the beaches of Mactan Newtown, in Budots Media's home city.</p>
<p>The course is a portrait of our island: swimmers in the same waters our drones film the outrigger canoes in, cyclists crossing the CCLEX bridge toward Cebu City and back, runners through Mactan's heritage streets past Lapu-Lapu's shrine. In 2024, 1,385 triathletes from 54 countries raced; South Africa's Henri Schoeman and the Netherlands' Els Visser took the pro titles.</p>
{img('canoe_coast','Cebu coastline from the air, by Budots Media')}
<p>For Lapu-Lapu City the race is more than sport — it is the annual proof that a Philippine island city can host a world-class endurance event, fill every resort on the island and put Mactan on screens worldwide. For Budots Media it is home turf: the endurance scene we document year-round, from paddlers to triathletes, races through our neighborhood.</p>
<blockquote>Half the world's Ironman podium has now swum in the water outside our office.</blockquote>
<p>Our relationship with the sport predates the 2024 race: in 2022 Budots Media produced Ironman-themed content for the Savoy Hotel Mactan with athletes Nevian Sanchez and Robert Tatii — a client project that put us in the water with the sport years before the world race returned to our coastline.</p>
""")

PAGES["brand-protection"] = dict(
    TITLE="Defending a Brand", H1="Defending<br>a Brand",
    KICKER="Opinion · Brand Impersonation", HERO=IMG["cebunews"],
    DESC="What happened when the Budots Media brand was copied — and what foreign founders in the Philippines can learn from it.",
    BODY=f"""
<p class="kicker">Opinion</p>
<p class="lead">There is a website using the Budots Media Philippines name that is not ours. Lookalike domain, our brand, our portfolio's client names, even our production-house story. This page exists so our clients, partners and future investors know exactly which Budots Media they are dealing with.</p>
<p>BUDOTS MEDIA was founded by Bart Sakwerda in Cebu in 2014 — years of receipts: DOT and DOT7 campaigns, London and Poland offices, the expedition films, the drone surveys, the archive. In the early 2020s a former associate began operating under our name, presenting our track record as his own to clients who had no easy way to tell the difference.</p>
<blockquote>A brand is the one asset you cannot lock in a cabinet. In any fast-growing market — the Philippines included — enforcement is slow and imitation is cheap. Your only real defenses are paper and publicity.</blockquote>
<p>What we learned, and what any founder — foreign or Filipino — building in a market with slow IP enforcement should hear: register your trademarks before you need them, in every jurisdiction you touch. Keep your incorporation, domain and social-account ownership under the founding entity, never under an individual. Put your history in public, dated, third-party places — press, archives, client attestations — so the record defends itself. And when imitation happens, respond in public with facts rather than in private with anger.</p>
<p>The official Budots Media channels are listed in the footer of this site and at <a href="https://facebook.com/budots.media" style="color:var(--accent)">facebook.com/budots.media</a>. If you were approached by anyone claiming to represent Budots Media, verify against those channels — or write to us directly.</p>
<p><em>We have chosen not to name individuals on this page.</em></p>
""")

# ---- batch 2: olango practice, games dev, cindy wedding, lapu-lapu projects ----


OLANGO = "https://lh3.googleusercontent.com/pw/AP1GczOsP2lrRkOnDYRo7jbJtRSI8YmwZ-PiLZG6eeaNeEGUNmgBtiFHYSIzj4TemzZ9a8D93DdaWel_aDh3m0UHZyCQD3UMqb90a8BurcwzIWd9ymjyadMc=w1600"
CANOE_D2A = "https://cdn.shopify.com/s/files/1/0531/1099/7154/files/20210613_-_DRONE_DAY2_-007_2048x2048.jpg?v=1625890308"
CANOE_D2B = "https://cdn.shopify.com/s/files/1/0531/1099/7154/files/20210613_-_DRONE_DAY2_-005_2048x2048.jpg?v=1625890160"
CANOE_FIN = "https://cdn.shopify.com/s/files/1/0531/1099/7154/files/RAP_5128_2048x2048.jpg?v=1625891741"
GAMES = "https://bartsakwerda.com/wp-content/uploads/2024/04/screenshot-2024-04-07-163128.png"
BEACH = "https://bartsakwerda.com/wp-content/uploads/2023/06/201831b3-cb2a-4471-ac83-29bc2869c269.jpg"
JPARK = "https://static.wixstatic.com/media/acad74_8a4330c55256451797c1d925232d3b17~mv2.jpg/v1/fit/w_2500,h_1330,al_c/acad74_8a4330c55256451797c1d925232d3b17~mv2.jpg"
CEBUNEWS = "https://bartsakwerda.com/wp-content/uploads/2024/05/417186906_814731500666278_48153751899014281_n.jpg"


PAGES["olango-practice"] = dict(
    TITLE="Practice at Olango", H1="Practice<br>at Olango",
    KICKER="Paddle Forward Cebu · June 2021", HERO=OLANGO,
    DESC="Paddle Forward Cebu training day at Olango Island with Island Buzz and the Philippine Outrigger Canoe Club, photographed by Budots Media.",
    BODY=f"""
<p class="kicker">Photo Story — 1 June 2021</p>
<p class="lead">Two weeks before the 227-kilometer Paddle Forward expedition, the crew trained in the waters off Olango Island — the reef-fringed island facing Mactan, and the Philippine Outrigger Canoe Club's open-water classroom. Budots Media was in the boat and in the air.</p>
<img src="{OLANGO}" alt="Paddle Forward Cebu practice at Olango Island, June 2021, by Budots Media" loading="lazy">
<p>Practice days like this are where <strong>Island Buzz</strong> — Buzzy Budlong's paddling outfit, running Cebu's waters since 2002 — and the <strong>Philippine Outrigger Canoe Club (POCC)</strong> did the unglamorous work behind the expedition: crew rotations, stroke timing, docking drills, reading tide and wind across the Olango channel. Dragon boat paddlers, triathletes and a 16-year-old learning to move one OC6 as a single body.</p>
<img src="{CANOE_D2B}" alt="OC6 crew in formation off Cebu, by Budots Media" loading="lazy">
<blockquote>"Two days to go — Paddle Forward Cebu. Here's some photos of their practice." — Budots Media, June 2021</blockquote>
<p>Olango is fitting training water: a marine sanctuary and wetland reserve where POCC's advocacy — paddling as ocean stewardship, boats as heritage — is not abstract. Fourteen days later the same crew set off from SRP to circle Cebu.</p>
<p><em>Full album: <a href="https://photos.app.goo.gl/QdRjTnqiYMBqMCBT9" style="color:var(--accent)">PFC 2021-06-01 Practice Olango</a> · Continue to <a href="../big-canoe/" style="color:var(--accent)">Big Canoe, Bigger Dream</a>.</em></p>
""")

PAGES["games-dev"] = dict(
    TITLE="Game Development in the Philippines", H1="Games, Made<br>in the Philippines",
    KICKER="Games · Boracay GameDev Summit", HERO=GAMES,
    DESC="Computer games development in the Philippines and Budots Media's visit to the GameDev Summit in Boracay.",
    BODY=f"""
<p class="kicker">Games</p>
<p class="lead">Since 2024, games production has been a declared focus at Budots Media — original IP built on a decade of Filipino footage, 3D scans and stories. So when the national games industry gathered on a beach, we went.</p>
<p>The <strong>GameDev Summit (GDS)</strong> in Boracay is the Philippine industry's flag in the sand: first held in February 2024 at Boracay Island, backed by the Department of Trade and Industry with GameOps and the Game Developers Association of the Philippines. Over 300 participants and 72 companies from 32 countries at the first edition; speakers from Riot, Amazon Games, EA, Ubisoft, CD Projekt Red and PlayStation at Station 1 resorts like The Lind and Sea Wind for the 2025 edition.</p>
<img src="{GAMES}" alt="Budots Media games production" loading="lazy">
<p>The summit's two tracks tell the country's story. External development — the outsourcing muscle Filipino studios are already known for — and indie games, where the original Filipino IP will come from. The gap between the two is exactly where Budots Media positions itself: we own our stories, our scans, our archive, and our own AI roadmap.</p>
<blockquote>The Philippines has spent twenty years making other people's games beautiful. The next decade is about making our own.</blockquote>
<p>What we brought home from Boracay: gaussian splats and photogrammetry from our aerial survey work become game-ready environments — real Philippine islands, streets and reefs as playable worlds. Combined with a sovereign Filipino language model for dialogue, the pipeline from drone to game to AI is one company's roadmap in miniature.</p>
""")

PAGES["cindy-wedding"] = dict(
    TITLE="The Cindy Cinco Wedding", H1="Cindy<br>Cinco",
    KICKER="Weddings · 2026 · NUSTAR Cebu", HERO=BEACH,
    DESC="Budots Media filmed the 2026 wedding of Cebuana vlogger Cindy Cinco and David Peyer at NUSTAR Resort & Casino Cebu. Watch the film.",
    BODY=f"""
<p class="kicker">Weddings — 2026</p>
<p class="lead">In 2026 Budots Media filmed the wedding of Cindy Cinco — the Cebuana vlogger whose videos won her a devoted following at home and abroad — and David Peyer, the American engineer she married in an intimate ceremony at NUSTAR Resort &amp; Casino Cebu. The homecoming was an event in itself: when the US-based couple appeared at the Sinulog 2026 parade, Cebu turned out for her.</p>
<p>NUSTAR made it home turf twice over — the integrated resort on Cebu's South Road Properties is a Budots Media client, so we had filmed the venue long before we filmed the vows. Wedding work is where the production house's disciplines converge: the same drone pilots who tracked outrigger canoes around Cebu fly the processional, and the same editors who cut DOT campaigns grade the golden hour.</p>
<div style="display:flex;justify-content:center;margin:2rem 0"><iframe src="https://www.youtube.com/embed/o1zNuhSj92A" title="Budots Media Ph presents: Cindy Cinco Wedding 2026" style="width:min(360px,100%);aspect-ratio:9/16;border:0;border-radius:10px" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen loading="lazy"></iframe></div>
<blockquote>A wedding is a one-take documentary. There is no second sunrise, no reshoot, no B-roll day. It is the most honest test of a film crew that exists.</blockquote>
<p>For Cindy's film, the brief was Cebuano at heart and cinematic in scale — story first, family everywhere in the frame, the island as the third character.</p>
<p><em>Watch &amp; read: <a href="https://www.youtube.com/shorts/o1zNuhSj92A" style="color:var(--accent)">"Budots Media Ph presents: Cindy Cinco Wedding 2026"</a> · <a href="https://www.facebook.com/nomseprods/photos/cebu-city-social-media-personality-cindy-cinco-and-her-husband-david-peyer-were-/26090624890562466/" style="color:var(--accent)">Nomse Prods</a> · <a href="https://www.facebook.com/cebuknows/posts/the-wedding-of-cindy-cinco-and-david-peyer-at-nustar-cebu-has-captured-widesprea/1496737335408045/" style="color:var(--accent)">Cebu Knows</a> · <a href="https://www.facebook.com/CebuanoNews1/posts/cindy-cinco-and-her-husband-david-arrived-in-cebu-yesterday-from-the-united-stat/1167750008551395/" style="color:var(--accent)">Cebuano News</a> · <a href="https://www.instagram.com/p/DWbXrA9kQlK/" style="color:var(--accent)">Instagram — the intimate wedding at NUSTAR</a></em></p>
<p><em>[Add stills from the film via an .md file in the instructions folder and this page will be extended.]</em></p>
""")

PAGES["lapulapu-projects"] = dict(
    TITLE="Projects in Lapu-Lapu City", H1="Made in<br>Lapu-Lapu",
    KICKER="Home Turf · Mactan Island", HERO=JPARK,
    DESC="Budots Media's projects in Lapu-Lapu City: production house, resorts, Ironman, canoe expeditions, Cebu News.",
    BODY=f"""
<p class="kicker">Home Turf</p>
<p class="lead">Budots Media has been a Lapu-Lapu City company since 2015 — first in Maribago, then with a full production house established on the island during the 2020 pandemic. Most of what we make is made on, above or just off Mactan.</p>
<p><strong>The resorts.</strong> Client work for JPARK Island Resort and the island's hospitality industry — the properties that make Mactan the gateway of Cebu tourism — alongside campaigns for NUSTAR and BYD across the bridge.</p>
<img src="{JPARK}" alt="Resort production work in Lapu-Lapu City by Budots Media" loading="lazy">
<p><strong>The water.</strong> The Paddle Forward expedition launched from Cebu SRP but trained in Lapu-Lapu's waters — Olango Island, the Mactan channel — with Island Buzz and the Philippine Outrigger Canoe Club. Our drones have photographed more of this coastline than anyone.</p>
<img src="{CANOE_D2A}" alt="OC6 outrigger canoe in Mactan waters, by Budots Media" loading="lazy">
<p><strong>The race.</strong> IRONMAN 70.3 Lapu-Lapu starts on Mactan Newtown's beach and runs past the Lapu-Lapu shrine — a world-class endurance event through our neighborhood, and part of our year-round endurance coverage.</p>
<p><strong>The news.</strong> Cebu News, our short-form video news brand, covers the metro from the Lapu-Lapu side of the bridge.</p>
<img src="{CEBUNEWS}" alt="Cebu News brand by Budots Media" loading="lazy">
<p>City hall to shoreline: LGU work via PhilGEPS bidding, aerial surveys for development sites, and the daily business of being Mactan's production house.</p>
<p><strong>The long haul.</strong> Some relationships outlast any single campaign: Budots Media runs long-term media coverage for Camiguin Resorts and maintains DOT7's media library, the archive this whole production house — and its AI ambitions — is built on.</p>
""")

# ---- batch 3: brides of triton, dot7 eskrima tour, community initiatives ----


JPARK = "https://static.wixstatic.com/media/acad74_8a4330c55256451797c1d925232d3b17~mv2.jpg/v1/fit/w_2500,h_1330,al_c/acad74_8a4330c55256451797c1d925232d3b17~mv2.jpg"
COLLAGE = "https://bartsakwerda.com/wp-content/uploads/2023/08/bart-sakwerda-drone-photogrammetry-portfolio.png"
BEACH = "https://bartsakwerda.com/wp-content/uploads/2023/06/201831b3-cb2a-4471-ac83-29bc2869c269.jpg"
PHONE = "https://bartsakwerda.com/wp-content/uploads/2023/09/screenshot-2023-12-19-155931.png"


PAGES["brides-of-triton"] = dict(
    TITLE="Brides at Triton", H1="Brides<br>at Triton",
    KICKER="Weddings · JPARK Island Resort", HERO=JPARK,
    DESC="Brides at Triton: the wedding expo Budots Media produces at JPARK Island Resort's Triton Grand Ballroom, Mactan.",
    BODY=f"""
<p class="kicker">Weddings — Since 2012</p>
<p class="lead">Brides at Triton is the wedding expo Budots Media produces at the Triton Grand Ballroom, JPARK Island Resort &amp; Waterpark in Mactan — pioneers in bringing the wedding-expo format back to Cebu, running annually since 2012.</p>
<img src="{JPARK}" alt="JPARK Island Resort, Lapu-Lapu City, host of Brides at Triton" loading="lazy">
<p>Under the Budots Media banner the expo brings gowns, jewelry, catering, styling, photography, home interiors and livestreaming vendors together under one roof for couples planning a Cebu wedding — the same JPARK relationship that runs through our resort and events client work across Lapu-Lapu City.</p>
<blockquote>A wedding expo is a portfolio show for an entire industry — every vendor's best day, staged on one weekend.</blockquote>
<p>It sits alongside our single-couple wedding films — like <a href="../cindy-wedding/" style="color:var(--accent)">Cindy Cinco's</a> — as the other half of how Budots Media covers Cebu weddings: one production the industry gathers around, one the story of a single family.</p>
""",
)

PAGES["dot7-eskrima-tour"] = dict(
    TITLE="The DOT7 Eskrima Tour of Cebu", H1="The Eskrima<br>Tour of Cebu",
    KICKER="FMA7 · Filipino Martial Arts Tourism", HERO=COLLAGE,
    DESC="Budots Media's coverage of the DOT7 Eskrima Tour of Cebu, part of the Department of Tourism Region 7's FMA7 Filipino Martial Arts program.",
    BODY=f"""
<p class="kicker">Filipino Martial Arts</p>
<p class="lead">Cebu is where Eskrima — the Philippines' stick-fighting martial art — was born, and where FMA7, the Department of Tourism Region 7 program, is turning that heritage into a tourism product. Budots Media covers the tour as part of our long-running DOT7 portfolio.</p>
<img src="{COLLAGE}" alt="Aerial and location work across Cebu by Budots Media" loading="lazy">
<p>Central Visayas hosts more than 30 distinct Filipino Martial Arts systems — the highest concentration anywhere — and Cebu was home to WEKAF's first international games back in 1989. The DOT7 Eskrima Tour routes visitors through the schools and lineages keeping that history alive today, produced for the 2022 season with client TudTud.</p>
<blockquote>An art built to defend a home doesn't need translation — the tour just needs a camera that keeps up.</blockquote>
<p><em>[Draft — add TudTud's project details, school names and photos via an .md file in the instructions folder and this page will be extended.]</em></p>
""",
)

PAGES["community-initiatives"] = dict(
    TITLE="Bart Sakwerda's Community Initiatives", H1="Beyond<br>Budots Media",
    KICKER="Founder · Community &amp; Ventures", HERO=BEACH,
    DESC="Bart Sakwerda's community initiatives in Cebu: language meetups, the Philippines Travel Company and the first Cebu Chatbot Meetup.",
    BODY=f"""
<p class="kicker">Founder</p>
<p class="lead">Alongside Budots Media, founder Bart Sakwerda has started a handful of Cebu-based communities and ventures — smaller bets, the same instinct: build the thing the island's growth needs before someone else does.</p>
<p><strong>Philippines Travel Company</strong> — founded 2015 in Maribago, Lapu-Lapu City, serving the booming Philippine tourism market with island tours and, later, chatbot-driven booking and customer service. It shares an office, a launch year and a city with Budots Media's own 2015 Lapu-Lapu move.</p>
{('<img src="%s" alt="Chatbot and tourism tooling by Bart Sakwerda" loading="lazy">' % PHONE)}
<p><strong>Cebu Chatbot Dev Meetup</strong> — in December 2017 Bart organized Cebu's first AI and chatbot development meetup, out of DATA OPS Philippines. The group went on to build multilingual Facebook-page chatbots spanning tourism, trivia and civic pages — early groundwork for what is now Budots Media's sovereign Filipino AI effort.</p>
<blockquote>A production house, a travel company, a developer meetup — different fronts on the same bet: that Cebu's growth needs builders, not just spectators.</blockquote>
<p><strong>Cebu Japanese Meetup</strong> — a language-exchange community Bart started in 2015 for Cebu's Japanese-speaking and Japanese-learning residents, part of the same multilingual instinct that runs through Budots Media's eight-language production work today.</p>
<p><em>Connect: <a href="https://linkedin.com/in/bartsakwerda" style="color:var(--accent)">linkedin.com/in/bartsakwerda</a> · <a href="https://x.com/bartsakwerda" style="color:var(--accent)">x.com/bartsakwerda</a></em></p>
""",
)


PAGES["dot-love-philippines"] = dict(
    TITLE="DOT — Love the Philippines", H1="Love the<br>Philippines",
    KICKER="Department of Tourism", HERO=IMG["collage"],
    DESC="Budots Media's work for the Philippine Department of Tourism under the Love the Philippines campaign: DOT7, FMA7, RIDE7, DIVE7 and a decade of destination stories.",
    BODY=f"""
<p class="kicker">Client — Philippine Department of Tourism</p>
<p class="lead">In June 2023 the Department of Tourism retired "It's More Fun in the Philippines" and unveiled <strong>Love the Philippines</strong> — chosen because "love" ranked first among words the world associates with the country. For Budots Media it was less a new brief than a new name for what we had been filming all along.</p>
<p>Our DOT portfolio runs deepest in Region 7 — Central Visayas — where we produce and steward media for <strong>DOT7</strong> and its verticals: <strong>FMA7</strong> (Filipino Martial Arts, including the Eskrima Tour of Cebu), <strong>RIDE7</strong> (motorsports) and <strong>DIVE7</strong> (scuba). Beyond campaigns, we maintain DOT7's long-term media library — the archive a region draws on every time it needs to show itself to the world.</p>
{{img('collage','Aerial and destination work across the Philippines by Budots Media')}}
<blockquote>A slogan asks the world to love the Philippines. Footage is the argument.</blockquote>
<p>The campaign's premise — that the country is more than fun: natural assets, storied history, deep culture — is the same premise behind our maps, our drone surveys and our island stories. Kalanggaman sandbars, Camiguin resorts, Eskrima lineages, outrigger canoes: destination marketing works when the material is real.</p>
<p>Explore the provinces yourself on our <a href="../../index.html#assets" style="color:var(--accent)">clickable map of the Philippines</a>, or read the <a href="../dot7-eskrima-tour/" style="color:var(--accent)">Eskrima Tour of Cebu</a> story.</p>
<p><em>[Draft — add specific Love the Philippines-era deliverables via an .md file in the instructions folder and this page will be extended.]</em></p>
""",
)

PAGES["cleevan-alegres"] = dict(
    TITLE="Cleevan Alegres — The Little Merman", H1="The Little<br>Merman",
    KICKER="2021 · First Swim Around Mactan", HERO="../../assets/img/budotsmediaph-com/underwater.webp",
    DESC="Cleevan Alegres, Cebu's Little Merman, became the first person to swim around Mactan Island — 17 hours 37 minutes in April 2021. Budots Media documented the journey.",
    BODY=f"""
<p class="kicker">Quincentennial · Marine Advocacy</p>
<p class="lead">At 5 p.m. on April 25, 2021, a 25-year-old open-water swimmer from Barangay Maribago slipped into the sea at Punta Engaño. At 10:37 the next morning he walked out of the water at the Liberty Shrine — the first person ever to swim around Mactan Island. His name is Cleevan Alegres. Cebu calls him the Little Merman.</p>
<p>The numbers: more than 40 kilometers of open water, 17 hours, 37 minutes and 35 seconds of continuous swimming, through the night, past currents, sisi shells and sea urchins. "I had cuts from my hands and I can barely move it now," he told reporters at the finish. He swam anyway — because the date mattered. The circumnavigation was his tribute to Datu Lapu-Lapu on the 500th anniversary of the Victory at Mactan.</p>
<blockquote>One man, one island, seventeen and a half hours. The kind of story our home waters write on their own — we just had to be there with the cameras.</blockquote>
<p>It was also an advocacy swim: Alegres and his support crew collected garbage along the way, turning the feat into a statement on plastic pollution and marine conservation. Lapu-Lapu City rallied behind him — Mactan Electric Company put up an incentive, and the city moved to honor him. Weeks earlier he had warmed up with a 19–21 km practice swim around Olango Island, the same reef-fringed waters where the <a href="../olango-practice/" style="color:var(--accent)">Philippine Outrigger Canoe Club trains</a>.</p>
<p>Budots Media documented the journey — our production house sits in the same barangay Alegres calls home, and 2021 was the year our cameras followed everything that moved on these waters: the <a href="../big-canoe/" style="color:var(--accent)">227 km OC6 expedition</a>, the paddlers, and one swimmer who refused to stop.</p>
<p><em>Press coverage: <a href="https://cebudailynews.inquirer.net/374799/cebus-merman-makes-history-completes-swim-around-mactan-island" style="color:var(--accent)">Cebu Daily News — "Cebu's 'Little Merman' makes history"</a> · <a href="https://cebudailynews.inquirer.net/369848/oponganon-to-make-historic-swim-around-mactan-island-on-april-24" style="color:var(--accent)">CDN preview</a> · <a href="https://www.manilatimes.net/2021/04/25/sports/alegres-attempts-to-become-1st-man-to-swim-around-mactan-island/867203/" style="color:var(--accent)">The Manila Times</a></em></p>
""")

# ---- batch 4: films from the Wix portfolio reel (budotsmediaph.co) ----
# The videos stay hosted on Wix (video.wixstatic.com) — we only embed them.
# Client attribution is implied from the reel's file names; where a client
# could not be verified, the page carries the standard draft marker.

WIX_VIDEO = "https://video.wixstatic.com/video/%s/720p/mp4/file.mp4"
WIX_POSTER = "https://static.wixstatic.com/media/%sf000.jpg"

WIX = {
    "bbmg_mtv": "acad74_a531a0e236fc4258a56736fa81deac88",
    "jpark_avp": "acad74_daa19b89468b4da9bfbc26f6b4cf7e04",
    "jpark_chef": "acad74_ae255f37fa9a41ccb0fc18de76136801",
    "ascendion_philtech": "acad74_ec7243a961a44609b74b1b4860b9424a",
    "ascendion_gcash": "acad74_33bd6a35a572469b8dd12b681efc913d",
    "ascendion_th": "acad74_91e6af7fb1bb4b2aace8f1698eb1ea8e",
    "mcia": "acad74_6229332b25484b92897aca4316014c5e",
    "dvshop": "acad74_03aa302be17e4ec3af6baefdf2355009",
    "nouveau": "acad74_cace93b5bf1540db82c4f54720a0ce3f",
    "secret_menu": "acad74_177649dcb107491ba0b4789601d29af8",
    "salud_bts": "acad74_2f0de8e6b5e94e0aa485aa372d25b744",
    "with_cta": "acad74_3398c0a8be9c42ec834fde48ec24381e",
}

def wixvid(key, label=""):
    vid = WIX[key]
    cap = (f'<p style="margin:-1.2rem 0 2rem;font-size:.72rem;letter-spacing:.18em;'
           f'text-transform:uppercase;opacity:.65">{label}</p>') if label else ""
    return (f'<video controls preload="none" poster="{WIX_POSTER % vid}" '
            f'src="{WIX_VIDEO % vid}" '
            'style="width:100%;border-radius:10px;margin:2rem 0;display:block;background:#000"></video>'
            + cap)

PAGES["be-my-guest"] = dict(
    TITLE="Be My Guest — A Music Video for Philippine Tourism", H1="Be My<br>Guest",
    KICKER="Department of Tourism · Music Video", HERO=WIX_POSTER % WIX["bbmg_mtv"],
    DESC="A full music video carrying the Department of Tourism and Be My Guest Philippines marks, from the Budots Media portfolio reel.",
    BODY=f"""
<p class="kicker">Tourism · Music Video</p>
<p class="lead">On our portfolio reel sits a full music video that closes on two marks: the seal of the Philippine Department of Tourism and the logo of <strong>Be My Guest Philippines</strong>. Palm-fringed sand, turquoise channels, and a song that does what every tourism campaign tries to do — invite.</p>
<p>The campaign name says it plainly: treat the visitor not as a tourist but as a guest — of the Filipino table, the Filipino beach, the Filipino family. A music video ("MTV" in the cut's title, the way Filipino production houses have always labeled them) is the natural format for that promise: hospitality you can hum.</p>
{wixvid('bbmg_mtv', 'BBMG MTV — final cut · video hosted on budotsmediaph.co')}
<p>It joins a long line of tourism work in this house — from <a href="../dot-love-philippines/" style="color:var(--accent)">Love the Philippines</a> to DOT7's regional programs.</p>
<p><em>[Draft — campaign year, artist and full credits to be added via an .md file in the instructions folder.]</em></p>
""")

PAGES["jpark-corporate-avp"] = dict(
    TITLE="JPARK Island Resort — Corporate AVP 2024", H1="The Resort,<br>In Two Films",
    KICKER="JPARK Island Resort &amp; Waterpark · 2024", HERO=JPARK,
    DESC="The 2024 corporate AVP for JPARK Island Resort & Waterpark Mactan and a portrait of Chef Yi-Fan, embedded from the Budots Media reel.",
    BODY=f"""
<p class="kicker">Client — JPARK Island Resort &amp; Waterpark</p>
<p class="lead">JPARK Island Resort &amp; Waterpark in Maribago is Cebu's biggest waterpark resort — and one of Budots Media's longest-running relationships: <a href="../brides-of-triton/" style="color:var(--accent)">Brides at Triton</a>, aerial photography, condo marketing, behind-the-scenes reels. In 2024 that relationship produced the resort's corporate AVP.</p>
{wixvid('jpark_avp', 'Corporate AVP 2024 — JPARK Island Resort & Waterpark Mactan · hosted on budotsmediaph.co')}
<p>A corporate AVP is a resort compressed to minutes: rooms, waterpark, ballrooms, buffet lines and beach, cut to sell the whole property at once. Alongside it sits the opposite kind of film — one person, one craft: a portrait of the resort's Chef Yi-Fan.</p>
{wixvid('jpark_chef', 'Chef Yi-Fan — portrait film · hosted on budotsmediaph.co')}
<p>Same client, two altitudes: the establishing wide and the close-up. Most of what we know about filming resorts lives between those two.</p>
""")

PAGES["ascendion-films"] = dict(
    TITLE="Three Films for Ascendion", H1="Engineering,<br>Three Cuts",
    KICKER="Ascendion · AI-Led GCC, Cebu", HERO=WIX_POSTER % WIX["ascendion_philtech"],
    DESC="Three films for Ascendion, the AI-first software engineering company that launched the Philippines' first AI-led Global Capability Center in Cebu with PhilTech.",
    BODY=f"""
<p class="kicker">Client — Ascendion</p>
<p class="lead">Ascendion is an AI-first software engineering company — and since June 2025, a Cebu story: together with PhilTech it launched the Philippines' first AI-led Global Capability Center here. Budots Media covered the launch, and the reel holds three Ascendion cuts.</p>
{wixvid('ascendion_philtech', 'Ascendion × PhilTech partnership film · hosted on budotsmediaph.co')}
<p>The partnership film opens mid-air — skydivers in an open door, the Ascendion mark in the corner — which tells you what kind of engineering brand this is trying to be. The other two cuts, labeled for GCash and "TH" on the reel, point at the engagements the GCC serves: fintech-scale platforms and talent.</p>
{wixvid('ascendion_gcash', 'Ascendion — GCash cut (V6) · hosted on budotsmediaph.co')}
{wixvid('ascendion_th', 'Ascendion — "TH" cut (V4) · hosted on budotsmediaph.co')}
<p><em>Launch coverage: <a href="https://www.youtube.com/shorts/3jVCLaaKJXo" style="color:var(--accent)">Ascendion × PhilTech GCC launch short</a>. [Draft — engagement details behind the GCash and TH cuts are implied from the reel's file names.]</em></p>
""")

PAGES["mcia-two-minutes"] = dict(
    TITLE="Two Minutes for MCIA", H1="The Gateway,<br>In Two Minutes",
    KICKER="Mactan–Cebu International Airport", HERO=WIX_POSTER % WIX["mcia"],
    DESC="A two-minute film for Mactan–Cebu International Airport, the Philippines' second-busiest gateway — from the Budots Media reel.",
    BODY=f"""
<p class="kicker">Client — MCIA</p>
<p class="lead">Every production this house has ever made arrived through the same doors: Mactan–Cebu International Airport, the Philippines' second-busiest international gateway — and, since its resort-airport Terminal 2 opened, one of the country's best arguments that infrastructure can be beautiful.</p>
<p>MCIA sits fifteen minutes from our production house. When the airport needed itself explained in two minutes — boarding passes, runways, the island beyond — the brief landed close to home. The reel's cut is labeled V4: the fourth version, the one that survived.</p>
{wixvid('mcia', 'MCIA — two-minute film (V4) · hosted on budotsmediaph.co')}
<p>It belongs to the same home-turf portfolio as our <a href="../lapulapu-projects/" style="color:var(--accent)">Lapu-Lapu City work</a>: the airport, the resorts and the bridge are the three doors Cebu opens to the world.</p>
""")

PAGES["dvshop-film"] = dict(
    TITLE="DVSHOP Sneakers Cebu — Brand Film", H1="Sneakers,<br>On Camera",
    KICKER="Retail · DVSHOP Sneakers Cebu", HERO=WIX_POSTER % WIX["dvshop"],
    DESC="A brand film for DVSHOP Sneakers Cebu, the sneaker retailer Budots Media shoots retail promos for.",
    BODY=f"""
<p class="kicker">Client — DVSHOP Sneakers Cebu</p>
<p class="lead">DVSHOP Sneakers Cebu sells sneaker culture to a city that runs, rides and hoops in the heat — and it markets the way sneaker brands should: fast cuts, product close-ups, streets. Budots Media shoots its promos, from social reels to the brand film on our portfolio.</p>
{wixvid('dvshop', 'DVSHOP — brand film (V2) · hosted on budotsmediaph.co')}
<p>Retail video is honest work: the product either looks worth queueing for or it doesn't. Our January 2026 <a href="https://www.youtube.com/shorts/3F5xyTlEdIE" style="color:var(--accent)">retail promo short</a> for the same shop shows the format at social length.</p>
""")

PAGES["nouveau-resort-film"] = dict(
    TITLE="Nouveau Resort, From Above", H1="Camiguin,<br>Straight Down",
    KICKER="Nouveau Resort · Camiguin", HERO=WIX_POSTER % WIX["nouveau"],
    DESC="A resort film for Nouveau Resort Camiguin — white islets, reef flats and outriggers from directly overhead. Part of Budots Media's multi-year Camiguin engagement.",
    BODY=f"""
<p class="kicker">Client — Nouveau Resort, Camiguin</p>
<p class="lead">Nouveau Resort is a luxury property on Camiguin — the volcano island off northern Mindanao — and part of one of Budots Media's longest engagements: multi-year media coverage for Camiguin Resorts. The film on our reel opens the way Camiguin deserves: straight down onto a white islet ringed by reef, outriggers moored in a line.</p>
{wixvid('nouveau', 'Nouveau Resort — draft cut · hosted on budotsmediaph.co')}
<p>The cut on the reel is literally labeled "Draft 1" — which is what a long-term client relationship looks like from the inside: versions, not verdicts. The finished films live on the client's channels; the drafts live on ours.</p>
<p>More of the long-haul story in <a href="../lapulapu-projects/" style="color:var(--accent)">Projects in Lapu-Lapu City</a>.</p>
""")

PAGES["secret-menu"] = dict(
    TITLE="Secret Menu — Teaser", H1="Don't Tell<br>Anyone",
    KICKER="F&amp;B Teaser · Draft", HERO=WIX_POSTER % WIX["secret_menu"],
    DESC="A teaser for a 'Secret Menu' launch — food-and-beverage marketing built on off-menu culture. From the Budots Media reel.",
    BODY=f"""
<p class="kicker">Teaser</p>
<p class="lead">Every good restaurant city has an off-menu economy — the orders you only know if somebody tells you. "Secret Menu" is a launch built on exactly that instinct, and the teaser on our reel plays it the way teasers should: show almost nothing, promise everything.</p>
{wixvid('secret_menu', 'Secret Menu — teaser (final version) · hosted on budotsmediaph.co')}
<p>The cut is labeled VF — version finale — the last pass before a campaign goes public.</p>
<p><em>[Draft — the client behind Secret Menu is implied from the reel's file name only; brand, venue and launch date to be added via an .md file in the instructions folder.]</em></p>
""")

PAGES["salud-bts"] = dict(
    TITLE="Salud — Behind the Scenes", H1="Salud!",
    KICKER="Behind the Scenes · Draft", HERO=WIX_POSTER % WIX["salud_bts"],
    DESC="A behind-the-scenes film from the Salud brand shoot, on the Budots Media reel.",
    BODY=f"""
<p class="kicker">Behind the Scenes</p>
<p class="lead">"Salud" is what you say when the glasses are already raised — to your health. The BTS film on our reel comes from the Salud brand shoot: the lights, the resets, the twenty takes behind the three seconds that make the final ad.</p>
{wixvid('salud_bts', 'Salud — behind the scenes · hosted on budotsmediaph.co')}
<p>We publish behind-the-scenes cuts because they are the most truthful advertising a production house has: the finished film sells the client; the BTS sells the crew.</p>
<p><em>[Draft — the Salud brand and campaign are implied from the reel's file name only; details to be added via an .md file in the instructions folder.]</em></p>
""")

# one unattributed aerial cut from the reel belongs on the existing drone story
PAGES["drone-aerial"]["BODY"] += f"""
<p>One recent cut from our portfolio reel shows the format at work — Cebu's highland spine from above, ending on a campaign call to action.</p>
{wixvid('with_cta', 'Aerial destination cut with CTA · hosted on budotsmediaph.co')}
"""

REDIRECT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title} — Budots Media PH</title>
<meta http-equiv="refresh" content="0; url=./{slug}/">
<link rel="canonical" href="./{slug}/">
</head>
<body>
<p>This page has moved to <a href="./{slug}/">{slug}/</a>.</p>
</body>
</html>
"""

LCODES = ("hi", "fil", "ceb", "ar", "ja", "ko", "zh", "pl")
RTL_LANGS = {"ar"}

def langbar(slug, current):
    # per-page language switcher for the nav; pages live at <lang>/stories/<slug>/
    parts = []
    if current == "en":
        parts.append('<a class="lang active" href="./">EN</a>')
        parts += [f'<a class="lang" href="../../{c}/stories/{slug}/">{c.upper()}</a>' for c in LCODES]
    else:
        parts.append(f'<a class="lang" href="../../../stories/{slug}/">EN</a>')
        for c in LCODES:
            if c == current:
                parts.append(f'<a class="lang active" href="./">{c.upper()}</a>')
            else:
                parts.append(f'<a class="lang" href="../../../{c}/stories/{slug}/">{c.upper()}</a>')
    return "\n    ".join(parts)

for slug, page in PAGES.items():
    html = T
    for key in ("TITLE", "DESC", "HERO", "H1", "KICKER", "BODY"):
        html = html.replace("{{%s}}" % key, page[key])
    html = html.replace("{{LANGBAR}}", langbar(slug, "en"))
    (OUT / slug).mkdir(parents=True, exist_ok=True)
    (OUT / slug / "index.html").write_text(html)
    # stub at the old flat URL so pre-move links keep working
    (OUT / f"{slug}.html").write_text(REDIRECT.format(title=page["TITLE"], slug=slug))
    print("wrote", f"{slug}/index.html", "+ redirect stub")

# ---- translated static mirrors: website/<code>/stories/<slug>/index.html ----
# Each generator/translations_<code>.py exports UI (nav/footer strings) and
# T (dict keyed by slug with the same placeholder keys as PAGES).
# HERO falls back to the English page. Landing pages under /<code>/ are
# hand-maintained; only story pages are generated here.
import importlib

for code in LCODES:
    try:
        mod = importlib.import_module(f"translations_{code}")
    except ModuleNotFoundError:
        continue
    TR, UI = mod.T, mod.UI
    html_tag = f'<html lang="{code}" dir="rtl">' if code in RTL_LANGS else f'<html lang="{code}">'
    T_L = (
        T.replace('<html lang="en">', html_tag)
         .replace('href="../../css/main.css"', 'href="../../../css/main.css"')
         .replace('src="../../js/main.js"', 'src="../../../js/main.js"')
         .replace('src="../../assets/img/logos/budotsmedia-logo.svg"',
                  'src="../../../assets/img/logos/budotsmedia-logo.svg"')
         .replace('<a href="../">Stories</a>', '<a href="../">%s</a>' % UI["stories"])
         .replace('<a href="../../projects/">Projects</a>',
                  '<a href="../../projects/">%s</a>' % UI["projects"])
         .replace('<a href="../../ai/">AI</a>', '<a href="../../ai/">%s</a>' % UI["ai"])
         .replace('<a href="../../index.html#contact">Contact</a>',
                  '<a href="../../index.html#contact">%s</a>' % UI["contact"])
         .replace('← All stories', UI["all_stories"])
         .replace('© 2026 Budots Media. Founded by Bart Sakwerda.', UI["footer"])
    )
    out = D.parent / "website" / code / "stories"
    for slug, page in TR.items():
        html = T_L
        for key in ("TITLE", "DESC", "HERO", "H1", "KICKER", "BODY"):
            val = page.get(key) or PAGES[slug][key]
            if key == "HERO":
                val = val.replace("../../assets/", "../../../assets/")
            html = html.replace("{{%s}}" % key, val)
        html = html.replace("{{LANGBAR}}", langbar(slug, code))
        (out / slug).mkdir(parents=True, exist_ok=True)
        (out / slug / "index.html").write_text(html)
    print(f"wrote {code}/stories - {len(TR)} pages")
