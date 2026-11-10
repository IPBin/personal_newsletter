"""Issue No. 1 — Tuesday, November 10, 2026.  Writes issue.json next to this file.

Worked example of a real daily issue. The research desks' output lives in parts/:
  news_regions.json  Indonesia, Canada, United States (+ chart suggestions)
  news_world.json    Around the World, Science, weather
  opportunities.json the opportunities block
  essay_*.json       essay texts fetched from the writers' own pages

    python issues/2026-11-10/make_issue.py && python -m paper.build issues/2026-11-10/issue.json
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
P = lambda name: json.load(open(HERE / "parts" / name))

regions, world, opps = P("news_regions.json"), P("news_world.json"), P("opportunities.json")
tb, nb = P("essay_true_believer.json"), P("essay_china_bear.json")
proof = json.load(open(HERE.parent / "proof-2026-11-10" / "issue.json"))

# ---------------------------------------------------------------- essays
tb_paras = [p for i, p in enumerate(tb["paras"][:28]) if i not in (3, 13, 20)]  # 3 = donation plea; 13, 20 = links to other posts
nb_paras = [re.sub(r"([a-z]\.)\d(\s|$)", r"\1\2", p) for p in nb["paras"][:31]]  # drop footnote marks

essay_tb = {
    "type": "essay", "essay_id": "1a1c0d360df73dd5", "optional": False, "priority": 9,
    "kicker": "Persuasion · Nov 9 · Opinion", "title": "The True Believer",
    "author": "Damon Linker", "publication": "Persuasion",
    "dek": "A political writer argues that Trump’s new chief of staff shows he will not soften after losing the midterms.",
    "paras": tb_paras,
    "source_note": "persuasion.community/p/the-true-believer · Damon Linker teaches political science at the University of Pennsylvania",
    "counter_label": "In plain words, and the other side",
    "counterpoint": [
        "The short version: Democrats won the midterms on Nov 3. Some people hoped Trump would now move to the middle, as Clinton, Bush and Obama did after losing. Instead, on Friday he made Stephen Miller his chief of staff. That is the person who runs the White House day to day. Linker says Miller wants the hardest line on immigration. He has pushed to suspend habeas corpus for non-citizens. Habeas corpus is the rule that the government must justify locking someone up. He has also pushed to use the Insurrection Act, a law that lets a president send soldiers into American cities. Linker’s fear is a leader who keeps calling things an “emergency” so he can step around the normal rules.",
        "The other side. This is opinion, from a magazine that openly opposes Trump. Words like “zealot” and “fanatical” are the writer’s judgement, not facts. Miller’s supporters would say he is carrying out the immigration policy Trump campaigned on and won with in 2024. Two things here are guesses. That Susie Wiles blocked the habeas plan is, in Linker’s own words, something “we have reason to suspect”. And the constitutional crisis is a forecast, not an event. Courts and a Democratic Congress will also have a say from January.",
    ],
}

essay_nb = {
    "type": "essay", "essay_id": "1a1b7deb2c081195", "new_page": False, "optional": True, "priority": 5,
    "kicker": "Noahpinion · Nov 7 · Opinion", "title": "Why I’m Becoming a China Bear",
    "author": "Noah Smith", "publication": "Noahpinion",
    "dek": "An economics writer who always expected China to keep rising explains why he has changed his mind.",
    "paras": nb_paras,
    "source_note": "noahpinion.blog/p/why-im-becoming-a-china-bear · the free part of the post; the charts are left out, and the section on AI is for subscribers",
    "counter_label": "In plain words, and the other side",
    "counterpoint": [
        "The short version: a “bear” expects something to do badly, and a “bull” expects it to do well. Smith was a China bull for years. Now he doubts China can lead the world. His first reason is here. China’s leader, Xi Jinping, wants China to make everything. The state spends about 4% of the whole economy each year helping factories. But China is too big to live on exports. Its own shoppers are spending less after the housing bust. So factories make more than anyone buys, and profits fall. China also built so many roads and railways that upkeep alone will be costly.",
        "The other side. Smith says himself that the plan “might have worked” and still might. A country that makes most of the world’s goods has real power, in trade and in war. People have predicted China’s slowdown many times and been early. His biggest reason, that China will handle AI badly, is behind the paywall, so you are reading the smaller part of his case. And he writes from the United States, with an American view of who should lead.",
    ],
}

essay_chinai = next(b for s in proof["sections"] for b in s["blocks"] if b.get("essay_id") == "1a1c03f311b75abb")
essay_chinai = {**essay_chinai, "priority": 2, "optional": True, "new_page": False,
                "counterpoint": ["It is a view from inside China, translated, about how new companies get money. Read it next to Noah Smith’s essay before it. Both say China’s state-led investing has gone too far. Liu Xiaoqing is one analyst with one view. Others in China would defend the state’s role."]}

# ---------------------------------------------------------------- newsstand
newsstand = {"type": "newsstand", "items": [
    {"essay_id": "1a1b7deb2c081195", "pub": "Noahpinion", "author": "Noah Smith", "title": "Why I’m becoming a China bear",
     "mode": "in full", "summary": "Printed in full in the Essays.", "hide_if_full": True,
     "fallback": ["Opinion. Noah Smith long expected China to keep rising. Now he doubts it. China’s plan to make everything is running into a wall, he says: its own shoppers are spending less, export markets are filling up, and factory profits are falling. The free part of the post stops before his main reason, which is AI."]},
    {"essay_id": "1a1c348a38c199f7", "pub": "AI Futures Project", "title": "Verified compute allocation disclosures as a foundational governance tool",
     "mode": "summary", "long": True, "paras": [
        "A policy proposal, and close to your interest in technical AI governance. “Compute” means the computer chips an AI company runs. The authors want AI companies to report regularly how they use their compute: how much goes to building stronger AI, how much to safety research, and how much to serving customers. Outside auditors would check the reports. They call this VCAD.",
        "Why bother? The authors want companies to slow down the building of more powerful AI. They call that “pacing”. Almost every way of slowing down, they argue, needs someone to check that no hidden chips are doing banned work. They also say it is not enough to delay big training runs. If research carries on, the progress piles up and arrives all at once later. Public reports could let people compare companies and reward the careful ones.",
        "Keep in mind: the authors rate their own confidence as “medium”. The group behind the post wants AI development slowed, so it starts from that goal. The post does not say how auditors would catch hidden chips, or why companies would agree to be checked.",
     ]},
    {"essay_id": "1a1c2657eebbb358", "pub": "Astral Codex Ten", "title": "Open Thread 459", "mode": "blurb",
     "summary": "Two notes. An astronomer wrote in to say it is untrue that there are millions of “Wow” signals. And marches for an AI treaty are planned for Saturday, Nov 14, in cities across the US, Canada and France."},
    {"essay_id": "1a1c162ac8d53883", "pub": "Visual Capitalist", "title": "The world’s biggest economies vs. debt in 2026", "mode": "blurb",
     "summary": "A chart, not an essay. The US has the largest economy. Sudan owes the most compared with the size of its economy."},
]}

poem = {"type": "box", "style": "poem", "optional": True, "priority": -2, "label": "A poem for a cold week",
        "paras": ["The way a crow / Shook down on me / The dust of snow / From a hemlock tree",
                  "Has given my heart / A change of mood / And saved some part / Of a day I had rued.",
                  "Robert Frost, “Dust of Snow”, 1920. To rue a day is to wish it had gone differently."]}
plate = {"type": "figure", "optional": True, "priority": -1, "src": "assets/art/processed/overworld-crop-kyoto.png",
         "caption": "Edo (today’s Tokyo, bottom right), where the road begins at Nihonbashi bridge. From Hokusai’s map of the Tōkaidō, about 1818."}

# ---------------------------------------------------------------- weather
wx = world["weather"]["daily"][:5]
t0 = wx[0]

# ---------------------------------------------------------------- front + desk
front = {
    "image": {"src": "assets/art/processed/front-overworld-band.png",
              "caption": "Mount Fuji and the old road from Edo to Kyoto, drawn by Katsushika Hokusai around 1818. The back page starts down that road today."},
    "lede": [],
    "today": [
        {"time": "11:15", "what": "Forecasting: Jobs and the Economy", "where": "Design Exchange, 234 Bay St · until 12:30"},
        {"time": "1:30", "what": "Post-AGI Civilization: What’s the Destination? (David Duvenaud)", "where": "Design Exchange · until 3:00"},
        {"time": "3:15", "what": "Research & Ideas Gallery (posters)", "where": "Design Exchange · until 4:45"},
        {"time": "6:00", "what": "Hinton Lectures, night 2: Paul Christiano on oversight", "where": "Livestream · until 7:30 · you can rewind", "dim": True},
    ],
    "todos": [
        {"topic": "Academics", "items": [
            {"text": "PHLB18 reading response. It was due Monday.", "src": "Todoist", "urgent": True},
            {"text": "Scaffolding Assignment 2 is still open from Nov 2. No. 3 is due Nov 23.", "src": "Todoist"},
            {"text": "Click the link in the “Confirm Email: Canvas” email, if you haven’t.", "src": "Quercus"},
        ]},
        {"topic": "TAISI", "items": [
            {"text": "Upload your receipts to HCB. Isabel asked everyone on Monday.", "src": "#taisi-team"},
            {"text": "Shivam’s cohort, Mon Nov 16: order the kosher meal too.", "src": "Todoist"},
        ]},
        {"topic": "Misc", "items": [
            {"text": "Pay off the credit card by Thursday.", "src": "Todoist", "urgent": True},
            {"text": "No date yet: Health and Wellness visit, bike, co-op papers.", "src": "Todoist"},
        ]},
    ],
    "brief": [],
}

desk = {"id": "desk", "title": "Your Desk", "tab": "For you", "aside": "What needs you, and what TAISI talked about", "blocks": [
    {"type": "attention", "title": "Needs you", "items": []},
    {"type": "agenda", "title": "This week and beyond", "items": [
        {"time": "Wed", "what": "AI Safety Week, Day 3: Forecasting AI-Enabled Power Concentration Risk", "where": "11:15–12:15 · Design Exchange · you’re approved"},
        {"time": "Wed", "what": "Hinton Lectures, night 3: governing transformative AI, then Geoffrey Hinton’s Q&A", "where": "6:00–7:30 pm · livestream"},
        {"time": "Thu", "what": "Credit card payment", "where": "your Todoist date"},
        {"time": "Sat", "what": "Marches for an AI treaty", "where": "cities in the US, Canada and France · noted in Astral Codex Ten", "dim": True},
        {"time": "Nov 16", "what": "Shivam’s cohort: you’re on food", "where": "kosher meal needed · Todoist"},
        {"time": "Nov 23", "what": "Scaffolding Assignment 3 due", "where": "Todoist"},
    ]},
    {"type": "channels", "title": "TAISI Slack · since Sunday", "channels": [
        {"name": "#taisi-team", "points": [
            "Isabel reminded everyone to upload receipts to HCB. One missing receipt has locked Joseph’s card. That hurts people who use the Uber Business account.",
            "Someone outside TAISI wants to run a linear algebra study group. Joseph thinks it does little harm and costs little: he would book a room and refer people, but not call it a TAISI program. Boyan agrees. He adds that U of T students could take MAT223 for credit instead. Joseph offered to call the organizer first.",
            "Boyan asked that anyone helping run a session watch Discord for about 30 minutes after it starts, in case someone comes late.",
            "Your Monday food order went through: Dr. Laffa (kosher) for Daniel, Ali Baba for the rest. Isabel said thanks.",
        ]},
        {"name": "#f26-facilitators", "points": ["Tazik shared the slides from Sunday’s mech-interp talk."]},
        {"name": "#hackathons", "points": ["On Sunday, Pera said to hold off on ordering food. There were leftover subs from David’s fellowship."]},
        {"name": "Quiet", "points": ["Nothing new in #general, #colloquium, #phl-panel, #reading-group, #writing-desk, #si-main, #si-notebooks or #off-topic."]},
    ]},
    {"type": "events", "title": "Your events (from Luma)", "items": [
        {"when": "Nov 10", "time": "Tue", "name": "AI Safety Week, Day 2.", "detail": "Three sessions at the Design Exchange, 11:15 to 4:45.", "status": "approved"},
        {"when": "Nov 9–11", "time": "6 pm", "name": "The Hinton Lectures 2026.", "detail": "Paul Christiano, three evenings. One livestream link works for all three.", "status": "registered"},
        {"when": "Nov 11", "time": "Wed", "name": "AI Safety Week, Day 3.", "detail": "Power Concentration Risk, 11:15.", "status": "approved"},
        {"when": "Nov 6–8", "time": "you hosted", "name": "Swarm Alignment Hackathon Toronto.", "detail": "Done. Ilyass sent the slides to guests on Sunday.", "status": "done"},
    ]},
]}

# Filled in below once the news and opportunities are in (kept here so the words sit together).
front["lede"] = [
    "Three AI Safety Week sessions fill your day at the Design Exchange, from 11:15 to 4:45. Paul Christiano’s second Hinton Lecture streams at 6. "
    + world["weather"].get("lede", "") +
    " One thing is late: the PHLB18 reading response was due Monday."
]
front["brief"] = P("brief.json")
desk["blocks"][0]["items"] = P("attention.json")

# ---------------------------------------------------------------- the world
def region(src, key, kicker, title, region_id=None):
    r = src[key]
    b = {"type": "region", "kicker": kicker, "title": title, "blurb": r["blurb"], "stories": r["stories"]}
    if region_id:
        b["region"] = region_id
    if r.get("map_points"):
        b["map_points"] = r["map_points"]
    if r.get("chart"):
        b["chart"] = r["chart"]
    b["stories"][0]["lead"] = True
    return b

graphics = P("graphics.json")   # {"after_usa": [...blocks], "after_world": [...], "bubble": {...}}
world_blocks = [
    region(regions, "indonesia", "Region one", "Indonesia", "indonesia"),
    region(regions, "canada", "Region two", "Canada", "canada"),
    region(regions, "usa", "Region three", "United States", "usa"),
    *graphics["after_usa"],
    region(world, "world", "Region four", "Around the World"),
    *graphics["after_world"],
    region(world, "science", "Region five", "Science"),
    graphics["bubble"],
]

issue = {
    "date": "2026-11-10", "date_long": "Tuesday, November 10, 2026", "weekday": "Tuesday",
    "number": "1", "edition": "Morning edition",
    "weather_word": world["weather"]["word"], "weather": {"daily": wx},
    "front": front,
    "sections": [
        desk,
        {"id": "opps", "title": "Opportunities", "new_page": False, "tab": "Don’t miss", "aside": "Sorted by deadline",
         "blocks": [{k: v for k, v in opps.items() if k in ("type", "intro", "ruler_days", "groups", "note")}]},
        {"id": "world", "title": "The World", "tab": "News", "aside": "The facts first. The opinions get labels.", "new_page": True, "blocks": world_blocks},
        {"id": "essays", "title": "The Essays", "tab": "Read slowly", "aside": "Printed whole, in the writers’ own words",
         "blocks": [essay_tb, essay_nb] + ([essay_chinai] if P("options.json").get("chinai") else [])},
        {"id": "stand", "title": "The Newsstand", "new_page": False, "tab": "Your inbox", "aside": "The last 24 hours, summed up",
         "blocks": [newsstand, poem, plate]},
    ],
    "gallery": proof["gallery"],
    "back": {**proof["back"],
             "caption": "Every trip on the Tōkaidō, the great road from Edo (now Tokyo) to Kyoto, started at this bridge. Here a lord’s parade crosses at dawn while fish sellers wait to get by. Hiroshige made 55 prints of the road. Turn the page sideways to see it the right way up."},
}
json.dump(issue, open(HERE / "issue.json", "w"), ensure_ascii=False, indent=1)
print("wrote", HERE / "issue.json")
