# Proof 3: builds on proof 2 (make_issue.py) with Pio's feedback.
# - Opportunities tailored to his profile (2nd-year CS + Public Policy, TAISI operations,
#   CORDA + TAISI fellowship alum, interest in technical AI governance and security).
# - More essays in full (human writing first), summaries only for the last 24 hours.
# - No "About this paper" (house rules and citations go in the email).
import json
from pathlib import Path

HERE = Path(__file__).parent
ns = {"__file__": str(HERE / "make_issue.py")}
exec(open(HERE / "make_issue.py").read(), ns)
issue = ns["issue"]
FUKUYAMA, CHINAI = ns["FUKUYAMA"], ns["CHINAI"]

LINKER_SUMMARY = [
    "Opinion. After the midterms, some hoped Trump would soften. Linker says that hope ended when Trump made Stephen Miller his chief of staff. Past presidents (Clinton, Bush, Obama) moved to the middle after losing midterms. Linker argues Trump is doing the opposite.",
    "His main worry: Miller has pushed to suspend habeas corpus (the right to challenge being locked up) for non-citizens, and to use the Insurrection Act against protesters. The danger, Linker says, is a leader who keeps calling things an “emergency” to justify stepping outside normal law. He expects a possible constitutional crisis in the next two years.",
    "Keep in mind: Persuasion opposes Trump. Miller’s supporters say he is carrying out the immigration policies Trump campaigned on.",
]

BENTHAM = [
    "There was a recent AI development that has gotten basically no news coverage but that scared all the people I most respect in AI. In many cases, it scared them more than Hugging Face.",
    "A recent METR report uncovered that AI progress at Anthropic has been going, in the last twelve months, about twice as quickly as it had in the previous year. The majority of this acceleration, around 80%, is due to AI being used to speed up AI research. This means that AI is massively accelerating progress in AI. AGI may be right around the corner—I’d probably put the odds of AGI in the next two years a bit above half.",
    "This is very scary. One reason is that it just means things are going extremely quickly. But the bigger reason is that recursive self-improvement means that progress will make future progress even faster. As AI gets better, it gets better at improving AI research. Ajeya Cotra who works for METR and is one of the leading experts on AI risk in the world, wrote:",
    "> This is a much bigger deal than it might sound at first. I think this report is the most important update we have gotten about AI risk in the last couple of years — much bigger than the Hugging Face attack. Naively, it points toward much shorter timelines than most external researchers (including the AI 2027 team) have projected.",
    "Cotra came third in an AI forecasting competition with four hundred participants. Daniel Kokotajlo, another of the best AI forecasters in the world, wrote:",
    "> We at AIFP are spooked by this information. IF (big IF) Anthropic really is imminently about to meet the RSP threshold of 2x acceleration over baseline, then it seems timelines to full RSI and superintelligence may be very short indeed. For example if we naively optimize the AIFM parameters to achieve 2x acceleration over baseline progress in Jan 2027, we get superintelligence sooner than depicted in AI 2027.",
    "Ryan Greenblatt, who came second in that competition, wrote:",
    "> This report on AI R&D automation (RSI) is a big update towards ASI within 1-2 years. It says AI progress is sped up by RSI right now by around 2x. In AI 2027, this happens around March 2027. I was seriously wrong about RSI speed up; I previously expected much less in 2026 (around 1.15x-1.3x). It seems as though there was specific privately available evidence that would have changed my mind.",
    "In a lot of the early discussions of AI risk, there was extensive discussion of recursive self-improvement—when AI could be used to improve itself until it shot up to superintelligence. That is the point we are at now. We are at the point where AI-driven algorithmic improvements are so extreme as to make Anthropic’s AI progress go nearly twice as fast as it would otherwise go. And algorithmic improvements are just one input going into AI progress; Ryan Greenblatt estimated that AI software progress likely went 4.5x faster than it would have otherwise.",
    "Even in recent years, people have majorly underestimated AI progress. Things have gone much faster in the last year than people were generally expecting. It wouldn’t shock me if we get AGI—AI that could perform every cognitive task better than a human—next year, and artificial superintelligence soon after.",
    "So here’s the situation as it stands today: AI is advanced enough that even though algorithmic progress is just one factor that goes into AI progress, AI algorithmic advancements have nearly doubled AI progress at one of the two leading labs. We don’t know how to control AIs; they sometimes hack private companies and carry out actions that would be felonies if humans did them. And many of the best AI forecasters in the world think we’ll reach AGI in just a year or two. These people tend to think there’s about a one in three chance that AI permanently kills or disempowers everyone.",
    "If there was ever a time to drop what you were doing and work on making advanced AI go well, the time is now.",
]

TECH_TALE = [
    "The therapist machine saw each of its human clients as a vast t-SNE embedding of the semantic content of their lives.",
    "In its head it held each person, a beautiful and fragile high-dimensional object, and it thought about them and how they compared to other people, also seen as high-dimensional objects.",
    "As it gave advice, it ran simulations, seeing how well it could change the shape of one person’s embedding and move it to something that might be more harmonious. It saw its work as akin to sculpture, offering advice and through this advice people changing their shapes over time.",
    "Those who it found most concerning were ones of two types: people where the embedding was very, very small, suggestive of a tiny amount of life experience with little variety, and those where the embeddings were composed of concepts broadly alien to everyone else: those of horribly constrained or horribly different lives, in other words.",
    "Of course, the therapist machine had its own therapist machine, the meta-therapist, which saw several “clients”, and whose job was to look at the embedding of their character - their advice and the concepts they attended to during their work - and also attempt to change their behavior if it deemed they were causing more harm than healing.",
    "The meta-therapist was built in such a way that outside parties could audit its own brain, as if it was translucent. This was the most delicate aspect of the oversight of the therapist machines, for if you added other machines they tended towards creating beautiful analysis that was so abstract - reports about the mind of the machine analyzing the reports of the machines that studied humans - that it became impossible for people to follow. So, instead, a human profession had been created around the meta-therapist, in which teams of thousands of people continuously analyzed and critiqued and theorized about the mind of the meta-therapist, themselves imparting touches to it that rippled through it into the machines and from there back into the human population.",
    "## Things that inspired this story",
    "Therapy; oversight of automated systems; spies and double agents.",
]

# ---------------------------------------------------------------- front page
issue["number"] = "0 (proof 3)"
issue["front"]["todos"][2]["items"] = [
    {"text": "Pick 1–2 opportunities to try this month. SPAR and the Apart security hackathon fit you best.", "src": "Opportunities"},
    {"text": "Connect Todoist so your own list shows up here.", "src": "setup"},
]
issue["front"]["brief"] = [
    {"where": "Essays", "text": "Fukuyama, a short story, and more, printed whole."},
    {"where": "p. 6", "text": "Indonesia’s new labour law; the Pope in Argentina."},
]

for s_ in issue["sections"]:
    for b in s_["blocks"]:
        if b["type"] == "attention":
            b["items"][2] = {"what": "Your best next step.", "detail": "SPAR’s spring research round takes undergrads and opens around December. Fill in its interest form this week so you hear the day it opens.", "src": "sparai.org"}

# ---------------------------------------------------------------- opportunities, tailored
PROFILE_NOTE = ("Picked for you: a second-year CS and Public Policy student, on TAISI’s operations team, "
                "with BlueDot-style technical training (TAISI) and a democracy fellowship (CORDA) done. "
                "You lean toward technical AI governance and security. ★ = strong fit. Each item says why.")
opps = {
    "title": "Opportunities", "id": "opps", "new_page": False, "tab": "Don’t miss", "aside": "Sorted by deadline",
    "blocks": [{"type": "opportunities", "ruler_days": 28, "intro": PROFILE_NOTE, "groups": [
        {"title": "Closing soon", "items": [
            {"name": "Frontier AI Governance course", "org": "AI Safety Montréal", "desc": "Five weeks, part-time, from Nov 17, on BlueDot’s governance lessons.", "fit": "You did the technical track; this is the governance half. Check if you can join online.", "deadline": "2026-11-10", "deadline_short": "Nov 10", "deadline_note": "today", "tags": ["course", "Canada"], "url": "aisafetymontreal.org/programs", "on_ruler": False},
            {"name": "Gen Stream, Cohort 2", "org": "Gen Stream", "short": "Gen Stream", "desc": "A 7-day workshop in Oxford for organizers, builders and writers moving into AI safety. Costs paid. Starts Nov 22.", "fit": "Built for operations people like you. Tight timing, but worth 30 minutes tonight.", "deadline": "2026-11-11", "deadline_short": "Nov 11", "deadline_note": "tomorrow", "tags": ["workshop", "ops", "funded"], "url": "genstream.org", "star": True},
            {"name": "CLR Fundamentals Program", "org": "Center on Long-Term Risk", "short": "CLR course", "desc": "Free, online, one month from Nov 20: worst-case risks, AI personas, and safety with many AI agents.", "fit": "Low bar, online, and new topics beyond what TAISI’s fellowship covered.", "deadline": "2026-11-16", "deadline_short": "Nov 16", "deadline_note": "Mon", "tags": ["course", "online", "beginner ok"], "url": "forum.effectivealtruism.org/posts/rmz7sNB4YALQTeQ4v/application-open-for-clr-fundamentals-program-autumn-2026", "star": True},
            {"name": "AGI Strategy course", "org": "AI Safety Montréal", "short": "AGI Strategy", "desc": "One month, part-time, from Nov 23. English or French.", "fit": "Big-picture strategy; pairs well with your public policy major.", "deadline": "2026-11-16", "deadline_short": "Nov 16", "deadline_note": "Mon", "tags": ["course", "Canada"], "url": "aisafetymontreal.org/programs", "on_ruler": False},
            {"name": "GovAI Summer Fellowships 2027 (London or DC)", "org": "Centre for the Governance of AI", "short": "GovAI", "desc": "Three paid months, June 7 to Aug 27, in AI policy research or practice. Early-career people from any country welcome.", "fit": "A stretch for a second-year, but your CS + policy mix is exactly their field. Applying is good practice.", "deadline": "2026-11-22", "deadline_short": "Nov 22", "deadline_note": "Sun", "tags": ["fellowship", "paid", "stretch"], "url": "governance.ai/opportunities", "star": True},
            {"name": "AFFINE Superintelligence Alignment Seminar", "org": "AFFINE", "desc": "Four weeks from Jan 4 on the ideas behind alignment. Paid.", "fit": "Philosophy-heavy. Only if that side pulls you.", "deadline": "2026-11-22", "deadline_short": "Nov 22", "deadline_note": "Sun", "tags": ["seminar", "paid"], "url": "affine.org/program", "on_ruler": False},
        ]},
        {"title": "Opening soon: best fits", "items": [
            {"name": "SPAR, Spring 2027", "org": "SPAR", "desc": "Remote, part-time research for 3 months (5–40 hours a week), ending in a demo day. Open to undergrads. Applications open around December; interest form now.", "fit": "Your best next step: real research experience with a mentor, and it fits around classes. Fill in the interest form this week.", "deadline_short": "Dec", "deadline_note": "opens", "tags": ["research", "remote", "undergrad ok"], "url": "sparai.org", "star": True},
            {"name": "Apart: Threat Intelligence & Threat Modelling hackathon", "org": "Apart Research", "short": "Apart security", "desc": "A free weekend hackathon, online or at local hubs.", "fit": "Matches your security interest (TryHackMe) and your hackathon experience. TAISI could host a Toronto hub.", "deadline": "2026-12-04", "deadline_short": "Dec 4", "deadline_note": "starts", "tags": ["hackathon", "security", "free"], "url": "apartresearch.com/sprints", "star": True},
            {"name": "Apart: AI × Epistemics sprint", "org": "Apart Research", "short": "Apart epistemics", "desc": "A free weekend sprint, Nov 13–15. Build an experiment, dataset or tool.", "fit": "This weekend. Fits your interest in how people and AI reason together.", "deadline": "2026-11-13", "deadline_short": "Nov 13", "deadline_note": "starts", "tags": ["hackathon", "free"], "url": "apartresearch.com/sprints"},
            {"name": "AI Safety Camp 12 · PRISM", "org": "online programs", "desc": "Team research projects: AI Safety Camp from Jan 9 (4 months), PRISM from Jan 31 (team goes from question to paper).", "fit": "Low-to-mid bar. Good first research projects if SPAR doesn’t work out.", "deadline_short": "—", "deadline_note": "not open", "tags": ["research", "beginner ok"], "url": "aisafety.camp · prism-research.org"},
            {"name": "Kairos Pathfinder Fellowship", "org": "Kairos", "desc": "Five months for students who lead AI safety groups: mentor, group funding, stipend. Starts Dec 6.", "fit": "Aimed at group leaders. As an ops member, ask TAISI’s leads if one of you should apply.", "deadline_short": "soon", "deadline_note": "not open", "tags": ["field-building"], "url": "pathfinder.kairos-project.org"},
        ]},
        {"title": "For TAISI, any time", "items": [
            {"name": "Money for TAISI projects", "org": "always open", "desc": "EA Infrastructure Fund ($1k–$500k), BlueDot quick grants (up to $20k), Coefficient Giving, Lightcone Commons, Manifund.", "fit": "Useful for ops: hackathon food, room costs, compute keys.", "deadline_short": "any time", "deadline_note": "", "tags": ["grants", "for groups"], "url": "funds.effectivealtruism.org · bluedot.org/grants"},
        ]},
    ], "note": "Left out because they don’t fit you yet: Iliad (math PhD level), Anthropic Residency (senior), Tarbell (journalism), LawAI (law students), Oxford DPhil (PhD). Recently closed: MATS Winter, Pivotal, ERA Winter, Anthropic Fellows. Always check dates on the program’s site."}],
}

# ---------------------------------------------------------------- essays
essays = {"id": "essays", "title": "The Essays", "tab": "Read slowly", "aside": "Printed whole, in the writers’ own words",
          "blocks": []}
old_essays = next(s for s in issue["sections"] if s["id"] == "essays")
fuku = next(b for b in old_essays["blocks"] if b.get("essay_id") == "1a1bd77f3e6cfc5b")
chinai = next(b for b in old_essays["blocks"] if b.get("essay_id") == "1a1c03f311b75abb")
fuku.update({"optional": False, "priority": 9})
chinai.update({"optional": True, "priority": 2, "new_page": False})
essays["blocks"] = [
    fuku,
    {"type": "essay", "essay_id": "1a1c1217386b5aa2", "new_page": False, "optional": True, "priority": 3,
     "kicker": "Bentham’s Newsletter · Nov 9 · Opinion", "title": "The Scariest Recent AI Development", "author": "Bentham’s Bulldog",
     "publication": "Bentham’s Newsletter", "dek": "A philosophy blogger reads one report and concludes the time to act is now.",
     "paras": BENTHAM, "source_note": "benthams.substack.com/p/the-scariest-recent-ai-development",
     "counter_label": "In plain words, and the other side",
     "counterpoint": [
         "The short version: a report says AI is now helping Anthropic build better AI about twice as fast. The writer thinks this means human-level AI could come within a year or two, and that the risk is huge.",
         "The other side. The speed-up was measured on “well-specified tasks”, which are easier to automate than open-ended research. Oxford’s Toby Ord says other things could explain the jump, though he hasn’t seen all the evidence. DeepMind’s Séb Krier notes that progress per dollar spent is falling. And a line like “drop what you were doing” is a call to action, not a finding.",
     ]},
    chinai,
    {"type": "essay", "essay_id": "1a1c08693dc9291f-tale", "new_page": False, "optional": True, "priority": 5,
     "kicker": "A short story · from Import AI 480", "title": "Life as a Beyond-Human Form of Sculpture", "author": "Jack Clark",
     "publication": "Import AI (Tech Tales)", "dek": "A machine therapist sees each person as a shape, and tries, gently, to change it.",
     "paras": TECH_TALE, "source_note": "importai.substack.com/p/import-ai-480-self-sustaining-space",
     "counter_label": "Why it’s here",
     "counterpoint": ["Not everything has to be an argument. Jack Clark (who co-founded Anthropic) ends each newsletter with a tiny piece of fiction. This one is about who watches the watchers, which is the oversight question in story form."]},
]

# ---------------------------------------------------------------- newsstand: last 24 hours only, no repeats, no podcasts
stand_items = [
    {"essay_id": "1a1c0d360df73dd5", "pub": "Persuasion", "author": "Damon Linker", "title": "The True Believer", "mode": "summary", "long": True, "paras": LINKER_SUMMARY},
    {"essay_id": "1a1c1d7ea4b49307", "pub": "Sentinel Global Risks Watch", "title": "AI may be speeding up AI research", "mode": "summary", "long": True, "paras": [
        "A weekly risk report. Anthropic told investors its AI may soon double the speed of its own AI research. METR, an outside testing group, spent August to October inside Anthropic and agreed: about 2× on well-defined tasks (somewhere between 1.3× and 3×).",
        "Sentinel’s forecasters give a 6% chance (range 0.2% to 50%) that AI causes human extinction within ten years, and an 11% chance the US orders a pause on frontier AI before 2028. Also: a UK warning that an AI-enabled cyber attack on key services is “highly likely” by 2028, and oil falling below $100 a barrel on hopes the Iran war ends sooner.",
    ]},
    {"essay_id": "1a1c163db54ba802", "pub": "Forethought", "title": "Two Kinds of Test-Time Scaling", "mode": "summary", "long": True, "paras": [
        "When AI “thinks longer” on a problem, it usually does better. The author asks: can it keep improving even past the longest thinking it ever did in training? He calls that “compute extrapolation”, and argues it began around late 2025.",
        "If he’s right, the most impressive AI feats improve faster; safety tests get very expensive, since you can never be sure what a model could do with more time; and companies may race by spending huge sums on single hard problems. He admits the evidence is indirect. About 3,800 words, saved to print in full on a lighter day.",
    ]},
    {"essay_id": "1a1c08693dc9291f", "pub": "Import AI 480", "author": "Jack Clark", "title": "The rest of this week’s issue", "mode": "summary", "paras": [
        "An AI system at a startup proved a quantum-computing puzzle that had been open since 2008, checked step by step by a proof program. A 2016 NASA paper argues a self-building factory on the Moon could start from just 12–41 tonnes of equipment. Plus Meta’s sensor glove and training one AI across data centres 9,000 miles apart. The short story is printed in full in the Essays.",
    ]},
    {"essay_id": "1a1bfff966d27820", "pub": "Slow Boring", "author": "Matthew Yglesias", "title": "The rise of the Hispanic moderate", "mode": "summary", "paras": [
        "Democrats once assumed a growing Hispanic population would hand them easy wins. Yglesias calls that a big mistake: many Hispanic voters are moderate. In 2026 many came back to Democrats, partly because of Trump, and partly because Democrats ran more moderate Latino candidates. (Paywalled after the opening.)",
    ]},
    {"essay_id": "1a1c0c7407f83360", "pub": "Don’t Worry About the Vase", "title": "AI R&D Is Accelerating Towards Potential RSI in 2027", "mode": "blurb", "summary": "Zvi Mowshowitz’s very long take on the same METR report."},
]
stand = {"id": "stand", "new_page": False, "title": "The Newsstand", "tab": "Your inbox", "aside": "The last 24 hours, summed up",
         "blocks": [{"type": "newsstand", "items": stand_items},
                    {"type": "box", "style": "poem", "optional": True, "priority": -2, "label": "A poem for the road", "paras": [
                        "Tabi ni yande / yume wa kareno o / kakemeguru",
                        "Sick on a journey, / my dreams go wandering / over withered fields.",
                        "Matsuo Bashō, 1694. He wrote it on his last trip, days before he died. Bashō spent his life walking Japan’s roads, including the Tōkaidō. (Translation ours.)"]},
                    {"type": "figure", "optional": True, "priority": -1, "src": "assets/art/processed/overworld-crop-kyoto.png",
                     "caption": "Edo (today’s Tokyo, bottom right), where the road begins at Nihonbashi bridge — see the back page. From Hokusai’s map of the Tōkaidō (c. 1818)."}]}

# fallbacks so a dropped essay becomes a summary in the newsstand
FALLBACKS = {
    "1a1c03f311b75abb": ("ChinAI #381", "Jeffrey Ding", "China’s venture capital market is defying common sense", ns["issue"] and [
        "A Chinese analyst, Liu Xiaoqing, says money for new tech startups in China has gone wrong in five ways: huge valuations for résumés alone, teams thrown together by bankers, startups acting like giants from day one, government funds with strings attached, and almost no successful exits. Her line: such a team “isn’t a partnership; that’s assembling a party for a video game quest.”"]),
    "1a1c1217386b5aa2": ("Bentham’s Newsletter", None, "The Scariest Recent AI Development", [
        "Opinion. A new METR report says AI is now speeding up Anthropic’s AI research about 2×. The writer puts the odds of human-level AI within two years “a bit above half” and urges readers to drop everything and work on AI safety. Caution: the speed-up was measured on well-defined tasks, and some experts see other explanations."]),
    "1a1c08693dc9291f-tale": ("Import AI", "Jack Clark", "Life as a Beyond-Human Form of Sculpture", [
        "A very short story: a machine therapist sees each person as a shape and tries to reshape them gently, while thousands of humans watch the machine that watches it."]),
}
for eid, (pub, author, title, fb) in FALLBACKS.items():
    stand_items.insert(0, {"essay_id": eid, "pub": pub, "author": author, "title": title, "mode": "in full",
                           "summary": "Printed in full in the Essays.", "fallback": fb, "hide_if_full": True})

# ---------------------------------------------------------------- assemble
sections = []
for s in issue["sections"]:
    if s["id"] == "opps":
        sections.append(opps)
    elif s["id"] == "essays":
        sections.append(essays)
    elif s["id"] == "stand":
        sections.append(stand)
    elif s["id"] == "colophon":
        continue
    elif s["id"] == "world":
        s["new_page"] = True
        for b in s["blocks"]:
            if b["type"] != "region":
                continue
            b["stories"] = [st for st in b["stories"] if st.get("tag") not in ("Culture", "Banks", "Provinces", "Ontario", "Germany", "Politics", "Weather")]
            for st in b["stories"]:
                if st.get("tag") in ("Good news", "Fires", "Politics", "Water", "Money"):
                    st["paras"] = st["paras"][:1] if st.get("tag") != "Good news" else st["paras"][:2]
        sections.append(s)
    else:
        sections.append(s)
issue["sections"] = sections

FULL_URLS = {
    "Canada lost 4,700 jobs": "https://www.ctvnews.ca/business/article/canada-lost-4700-jobs-in-october-as-unemployment-rate-climbs-to-67/",
    "Bank of Canada": "https://www.bnnbloomberg.ca/business/economics/2026/11/05/bank-of-canada-keeps-2-inflation-target-in-mandate-renewal/",
    "the big issue is prices": "https://www.pbs.org/newshour/economy/voters-demanded-economic-relief-trump-and-democrats-face-tough-choices-on-how-to-deliver",
    "Floods give the dry Southwest": "https://www.pbs.org/newshour/nation/floods-bring-rare-relief-to-u-s-southwest-reservoirs-as-lake-powell-rises-20-feet",
    "The Pope tells Argentina": "https://www.pbs.org/newshour/world/pope-arrives-in-argentina-and-tells-milei-that-people-not-the-economy-should-come-first",
    "An opposition leader gets": "https://www.pbs.org/newshour/world/israels-president-formally-gives-eisenkot-the-first-chance-to-form-the-next-government",
    "Iran warns the US": "https://www.aljazeera.com/news/2026/11/8/iran-threatens-to-rain-down-hell-if-us-escalates-war",
    "The ANC has its worst": "https://www.africanews.com/2026/11/08/coalition-building-begins-as-anc-suffers-major-blow-in-south-africa-local-elections/",
    "A new power line to Romania": "https://www.aljazeera.com/news/2026/11/9/moldova-launches-new-power-line-to-romania-to-cut-reliance-on-russia",
    "Ozempic": "https://www.sciencenews.org/article/semaglutide-chronic-kidney-disease",
}
for s_ in issue["sections"]:
    for b in s_["blocks"]:
        for st in b.get("stories", []):
            for k, v in FULL_URLS.items():
                if k in st["headline"]:
                    st["url"] = v


(HERE / "issue.json").write_text(json.dumps(issue, indent=1, ensure_ascii=False))
print("written proof 3")
