# Issue for Tue 10 Nov 2026 (proof, second draft). Written in plain English on purpose:
# short sentences, common words. The daily run writes issue.json directly.
import json
from pathlib import Path

HERE = Path(__file__).parent
T = json.load(open(HERE / "texts.json"))

FUKUYAMA = [
    "After being massively repudiated in Tuesday’s midterm election, Donald Trump has become a lame-duck president with significantly curtailed authority. What is likely to happen in the remaining two years until a new chief executive is sworn in on January 20, 2029?",
    "It should be obvious at this point that Trump will not bow to the popular will and move away from those policies that have proven to be so toxic. Completely in character, early signs are that he is doubling down, as indicated by his replacement of Chief of Staff Susie Wiles with hardliner Stephen Miller, and the weird choice of offering Dana White, head of the Ultimate Fighting Championship and a man described by Trump as “a violent Fighter and Warrior,” the role of press secretary. Meanwhile, lame-duck presidents of the past have embarked on new foreign policy initiatives in their remaining years, since the Constitution gives them much more discretionary authority than in domestic policy.",
    "So what can we expect?",
    "There is one general consideration that will shape all potential possibilities. That is the fact that Trump has been very good for all of America’s traditional rivals, like China, Russia, and North Korea. Trump has sought to have good relations with the authoritarian leaders of each of these nations, and has worked tirelessly to weaken the United States by pursuing polarizing policies targeting the “enemy within”—namely, his domestic opponents. Trump has further weakened the United States militarily by depleting ammunition stocks with his ill-considered war against Iran and his Defense Secretary Pete Hegseth’s purging of competent military officers. And he has alienated American allies in Europe and Asia by waging a tariff war against them.",
    "Trump has said that China wouldn’t dare move on Taiwan while he was president, but might under a Democratic successor. He is actually right about this, but for somewhat different reasons than those in Trump’s head. Why should the Chinese take on the enormous risk of a military operation now, when they have a U.S. president doing their work for them, defunding scientific research, as well as feuding with close allies like Japan and South Korea, while backing down on bilateral U.S.-China trade issues?",
    ">> If Xi Jinping were ever willing to attack Taiwan, it would have to be in the next two years.",
    "The midterm election has suddenly changed this calculus. It is now increasingly likely that Trump will be succeeded not by an isolationist Republican like JD Vance, but rather by a Democrat, who is very likely to reverse all of Trump’s foreign policy stances on day one. That means that if Xi Jinping were ever willing to attack Taiwan, it would have to be in the next two years. And what is the likelihood that a lame-duck Trump would meet a Chinese challenge with a spirited military defense of Taipei?",
    "Similar considerations apply in the case of Russia. Trump has essentially switched sides in Russia’s war with Ukraine, seeking to weaken sanctions and denying Ukraine access to the weapons it needs to defend itself. A democratic president in 2029 could reverse this quickly, if it is not already too late and if Ukraine succeeds in holding on. Vladimir Putin has every incentive to complete the military conquest of Ukraine in the next two years.",
    "A country that has not been at the top of people’s danger list is one that should be: North Korea. Pyongyang has learned a lot from its direct military involvement in the Russia-Ukraine war. It has absorbed the lesson that the future lies in large numbers of cheap FPV drones, and is rapidly working to reduce South Korea’s substantial battlefield advantage in older generations of military equipment. In addition, it now has a substantial nuclear arsenal that is capable of being used against the mainland United States. So what is the likelihood that a lame-duck President Trump would take a strong stance in defending South Korea, and commit to using American nuclear weapons as a deterrent against the North? Again, the window of opportunity lies in the next two years, not after.",
    "Thus we are at a moment of heightened peril. Three powerful authoritarian governments have a friend currently in the White House, but that friend will be leaving in two years and will almost certainly be replaced by a more hostile successor. This greatly increases the incentives for them to move in the near term while they have a better chance of getting away with their plans.",
    "Trump’s incentives, meanwhile, are to pull closer to the authoritarian trio, perhaps by trying to restart a dialogue with Pyongyang. But the nicer he is to them, the greater the likelihood that they will take advantage of good relations with the United States to move quickly.",
    "Trump’s erratic foreign policy has destabilized much of the world. We see this currently in the Middle East, where there is no clear way out of the war with Iran. But that instability might easily spill over into other theaters, with incalculable consequences.",
]

CHINAI = [
    "Context: Liu Xiaoqing is director of analysis at IT Juzi, one of my favorite sources on China’s venture capital ecosystem. Last week, she posted a lengthy denunciation that begins with this bold statement:",
    "> In 2026, a year where “embodied AI” has become practically in unison with “Chinese venture capital,” there are too many things happening that run counter to common sense.",
    "Let’s break down Liu’s critique into five main parts.",
    "## 1. Inflated valuations based on résumés alone",
    "Big tech execs and elite university PhD graduates easily land initial valuations of hundreds of millions of RMB. Liu critiques the restless, rushed mindset of these young geniuses, who spin and chase narratives defined by fundraising windows — unmoored from technological progress and maturity.",
    "## 2. All-star lineups that don’t form real teams",
    "Liu has seen countless founding teams that look good on paper: “a brilliant technical lead, a former executive from a major tech firm, a supply-chain veteran, and someone well-versed in the world of capital.” In practice, the whole is much less than the sum of its parts. In a piece full of zingers, this might have been my favorite one:",
    "> Yet, for many teams today, the journey looks more like this: the first time you meet happens at a dinner arranged by a financial advisor, the second time you meet takes place at the negotiating table for a term sheet, and the third you meet is the signing ceremony. People with completely different backgrounds, splitting equity 40/30/30, suddenly find themselves “running a company together” from day one. That’s not called a partnership; that’s called assembling a party for a video game quest.",
    ">> That’s not called a partnership; that’s called assembling a party for a video game quest.",
    "## 3. Startups that look like tech giants from day one",
    "Liu recalls learning about an embodied AI startup founded in 2023. Its founding experience reflects how the VC market is skipping steps when it comes to cultivating organizational capital:",
    "> They had raised hundreds of millions in their Series A round. Their office was in a high-rise building, complete with a logo wall at the reception. They had hired an HR director poached from a major tech giant, who spent the very first month setting up a rigid corporate hierarchy and performance review system. The founder, in his early thirties, had previously launched a startup out of a residential apartment, where four people shared a single case of instant noodles and spent three days haggling with a cloud service provider just to save on server costs. Only five years separate these two experiences. Yet, throughout those five years, he never truly experienced the process of an organization growing from five people to five hundred. But in this second venture, his team started out with five hundred people from the start.",
    "## 4. Dependence on government-backed funds",
    "Liu writes, “And here’s the most terrifying, yet often overlooked, aspect: a massive portion of this capital comes from state-backed funds.” Government guidance funds often involve an initial seed fund contributed by the government, with the remaining majority raised from local state-owned enterprises, private capital, and bank partners. However, as Liu notes, “When private capital enters a government guidance fund, it often comes with strings attached, such as requirements for ‘re-investment’ (investing a portion of the capital back into the local area), specific policy objectives, and various constraints that prioritize goals other than pure financial return.”",
    "Liu’s piece contains this sobering quote: “Yet, even among the most professional and long-established funds, those that have been around for only seven or eight years, the number that have truly completed the full lifecycle of ‘fundraising, investment, management, and exit’ can be counted on one’s fingers.” Again, the big question is what happens when these funds reach maturity (typical funds have a lifespan of 7–10 years)? Liu shares more stories: “I have encountered instances where, by the time a fund reached maturity, not a single project had exited. In the end, the only solution was for a local state-owned enterprise (SOE) to step in and take over the assets.”",
    "## 5. A fragile system",
    "Putting all of these points together, Liu’s thesis is that China’s VC ecosystem is far too fragile. She outlines this un-virtuous circle: “Capital flows in too quickly, forcing young founders to chase ever-higher valuations; the pace of growth outstrips the organization’s ability to mature… by the time these valuations are reached, no clear path for an exit has been established; with no exit in sight, the pressure ultimately falls back on the founders.”",
    "She ends with a comparison to a previous wave of mass entrepreneurship in the mid-2010s, when there was a boom of e-commerce and internet startups. There were also absurd valuations in that wave, but the chaotic mix was resilient because the ecosystem had a tolerance for failure. Liu points out, “Consequently, while that previous wave saw a massive number of casualties, the deaths were ‘clean’ — leaving the soil, in fact, even more fertile.” In contrast, the current Chinese entrepreneurship wave is lacking time and tolerance for failure.",
]

issue = {
    "date": "2026-11-10",
    "date_long": "Tuesday, November 10, 2026",
    "weekday": "Tuesday",
    "number": "0 (proof 2)",
    "edition": "Morning edition",
    "weather_word": "Mild & dry",
    "weather": T["weather"],
    "front": {
        "image": {
            "src": "assets/art/processed/front-overworld-band.png",
            "caption": "Mount Fuji and the old road from Edo to Kyoto, drawn by Katsushika Hokusai around 1818. Starting today, the back page walks that road with Hiroshige — one stop per issue, 55 in all.",
        },
        "lede": [
            "Today is a big AI Safety Week day. You have three sessions at the Design Exchange, from 11:15 to 4:45. The weather is kind: dry and up to 16°. Before you go, click the link in the Quercus email. Without it, school news can’t reach this paper.",
        ],
        "today": [
            {"time": "11:15", "what": "Forecasting: Jobs and the Economy", "where": "Design Exchange, 234 Bay St · until 12:30 (moved from 10:45)"},
            {"time": "1:30", "what": "Post-AGI Civilization: What’s the Destination? (David Duvenaud)", "where": "Design Exchange · until 3:00"},
            {"time": "3:15", "what": "Research & Ideas Gallery (posters)", "where": "Design Exchange · until 4:45"},
            {"time": "—", "what": "Assessing Loss-of-Control Risk: you’re on the waitlist", "where": "Luma will email you if a spot opens", "dim": True},
        ],
        "todos": [
            {"topic": "Academics", "items": [
                {"text": "Open the “Confirm Email: Canvas” email (Nov 9) and click the link.", "src": "Quercus", "urgent": True},
            ]},
            {"topic": "TAISI", "items": [
                {"text": "Vote on the team social: Sat Nov 28, 6 pm. React to Joseph’s post.", "src": "#taisi-team"},
                {"text": "Book the writing-desk room for weeks 3 and 4 when booking opens.", "src": "#writing-desk"},
                {"text": "Check the OpenRouter key sheet. Every key given out needs a name and email.", "src": "#hackathons"},
            ]},
            {"topic": "Misc", "items": [
                {"text": "Decide on the GovAI summer fellowships. Both close Sun Nov 22.", "src": "Opportunities"},
                {"text": "Connect Todoist so your own list shows up here.", "src": "setup"},
            ]},
        ],
    },
    "sections": [
        # ------------------------------------------------------------------ DESK
        {"id": "desk", "title": "Your Desk", "tab": "For you", "aside": "What needs you, and what TAISI talked about",
         "blocks": [
            {"type": "attention", "title": "Needs you", "items": [
                {"what": "Finish the Quercus setup.", "detail": "Canvas sent a link to your Gmail on Nov 9. Until you click it, course news won’t come through.", "src": "Gmail"},
                {"what": "Two deadlines in 12 days.", "detail": "GovAI’s London and Washington summer fellowships both close Sunday, Nov 22. They pay a stipend and take early-career people from anywhere.", "src": "governance.ai"},
                {"what": "A fellowship made for people like you.", "detail": "Kairos Pathfinder helps students who run AI safety groups. It isn’t open yet, but it starts Dec 6, so it could open any day.", "src": "aisafety.com"},
            ]},
            {"type": "agenda", "title": "This week and beyond", "items": [
                {"time": "Wed", "what": "AI Safety Week, Day 3: Forecasting AI-Enabled Power Concentration Risk", "where": "11:15–12:15 · Design Exchange · you’re approved"},
                {"time": "Nov 17", "what": "Colloquium co-working session (proposed)", "where": "4–6 pm · #colloquium", "dim": True},
                {"time": "Nov 26", "what": "AI Math Capabilities: A Fireside Chat", "where": "6–9 pm · Trajectory Labs · you’re registered"},
                {"time": "Nov 28", "what": "TAISI team social (proposed)", "where": "6 pm · vote in #taisi-team", "dim": True},
            ]},
            {"type": "channels", "title": "TAISI Slack · the last week", "channels": [
                {"name": "#taisi-team", "points": [
                    "Joseph wants an end-of-semester team social on Saturday, Nov 28 at 6 pm. He asked everyone to vote with a reaction.",
                    "Annie got sick (probably strep) before the weekend. Giles and Tazik covered her Saturday and Sunday groups.",
                    "After a mix-up over hackathon food, Isabel asked: post food orders in the main channel, not in threads. She doesn’t see thread alerts.",
                ]},
                {"name": "#f26-facilitators", "points": [
                    "Facilitators now plan here, Boyan says. Saturday’s group meets 6–7:30 (7 people). Sunday’s meets 5:30–7 (10 people).",
                    "Tazik shared the slides from the mech-interp talk on Nov 8.",
                    "Week 5’s reading list was late. Joseph said it would be up by midday Nov 4.",
                ]},
                {"name": "#colloquium", "points": [
                    "Lessons from the last talk: tell speakers who the audience is, book the room until 8 pm, and keep room BA2135. The sound and screen worked well.",
                    "Idea: a co-working session on Tuesday, Nov 17, 4–6 pm. Pera will ask Ayushman to speak. An “AI 2027 explained” talk is also an option.",
                ]},
                {"name": "#phl-panel", "points": [
                    "Working title: “After AGI: What Might a Good Outcome for Humanity Look Like?” David Duvenaud said yes. He’ll talk about his MATS mentoring work.",
                ]},
                {"name": "#hackathons", "points": [
                    "The Swarm Alignment Hackathon ran Nov 6–8. Each person got a $50 OpenRouter key. The organizers asked that every key be logged in the sheet.",
                ]},
                {"name": "#si-main", "points": [
                    "Oscar is looking for AI Safety Week volunteers for Tuesday and Wednesday. That’s today and tomorrow, if you want to help between talks.",
                ]},
            ]},
            {"type": "events", "title": "Your events (from Luma)", "items": [
                {"when": "Nov 10", "time": "Tue", "name": "AI Safety Week, Day 2.", "detail": "Three sessions approved. One waitlist (Loss-of-Control Risk).", "status": "approved"},
                {"when": "Nov 11", "time": "Wed", "name": "AI Safety Week, Day 3.", "detail": "Power Concentration Risk, 11:15.", "status": "approved"},
                {"when": "Nov 26", "time": "Thu", "name": "AI Math Capabilities: A Fireside Chat.", "detail": "Trajectory Labs, 6–9 pm.", "status": "registered"},
                {"when": "Nov 6–8", "time": "you hosted", "name": "Swarm Alignment Hackathon Toronto.", "detail": "Done. Ilyass sent the slides to guests on Nov 8. Luma counted 38 sign-ups before late drop-outs.", "status": "done"},
            ]},
         ]},
        # ------------------------------------------------------------------ OPPS
        {"id": "opps", "new_page": False, "title": "Opportunities", "tab": "Don’t miss", "aside": "Sorted by deadline. ★ = a good fit for you",
         "blocks": [
            {"type": "opportunities", "ruler_days": 28,
             "intro": "Each item stays here every day until its deadline passes. New ones get a NEW tag.",
             "groups": [
                {"title": "Closing in the next two weeks", "items": [
                    {"name": "Frontier AI Governance course", "org": "AI Safety Montréal", "desc": "A 5-week, part-time course from Nov 17. It uses BlueDot’s lessons.", "deadline": "2026-11-10", "deadline_short": "Nov 10", "deadline_note": "today", "tags": ["course", "Canada"], "url": "aisafetymontreal.org/programs", "on_ruler": False},
                    {"name": "Gen Stream, Cohort 2", "org": "Gen Stream", "short": "Gen Stream", "desc": "A 7-day workshop in Oxford for “generalists” (organizers, builders, writers) moving into AI safety. Costs are paid. Starts Nov 22.", "deadline": "2026-11-11", "deadline_short": "Nov 11", "deadline_note": "tomorrow", "tags": ["workshop", "ops-friendly", "funded"], "url": "genstream.org", "star": True},
                    {"name": "CLR Fundamentals Program", "org": "Center on Long-Term Risk", "short": "CLR course", "desc": "A free one-month online course from Nov 20. Topics: worst-case risks, AI personas, and safety with many AI agents.", "deadline": "2026-11-16", "deadline_short": "Nov 16", "deadline_note": "Mon", "tags": ["course", "online"], "url": "forum.effectivealtruism.org (CLR Fundamentals)", "star": True},
                    {"name": "AGI Strategy course", "org": "AI Safety Montréal", "desc": "One month, part-time, from Nov 23. In English or French.", "deadline": "2026-11-16", "deadline_short": "Nov 16", "deadline_note": "Mon", "tags": ["course", "Canada"], "url": "aisafetymontreal.org/programs", "on_ruler": False},
                    {"name": "Iliad Intensive (January 2027)", "org": "Iliad", "short": "Iliad", "desc": "Four weeks in Berkeley on the math side of AI alignment. For people with math, physics or CS training. Costs are paid.", "deadline": "2026-11-16", "deadline_short": "Nov 16", "deadline_note": "Mon", "tags": ["bootcamp", "funded", "math"], "url": "iliad.ac/calendar", "on_ruler": False},
                    {"name": "GovAI UK Summer Fellowship 2027", "org": "Centre for the Governance of AI", "short": "GovAI (UK + DC)", "desc": "Three months in London, June 7 to Aug 27, on AI policy research or practice. Paid. Early-career people welcome, from any country.", "deadline": "2026-11-22", "deadline_short": "Nov 22", "deadline_note": "Sun", "tags": ["fellowship", "paid", "undergrad ok"], "url": "governance.ai/opportunities", "star": True},
                    {"name": "GovAI DC Summer Fellowship 2027", "org": "Centre for the Governance of AI", "desc": "Same idea, three months in Washington, focused on US AI policy careers. Paid.", "deadline": "2026-11-22", "deadline_short": "Nov 22", "deadline_note": "Sun", "tags": ["fellowship", "paid", "US focus"], "url": "governance.ai", "on_ruler": False},
                    {"name": "AFFINE Superintelligence Alignment Seminar", "org": "AFFINE", "short": "AFFINE · Tarbell", "desc": "Four weeks from Jan 4 on the deep ideas behind alignment. Paid.", "deadline": "2026-11-22", "deadline_short": "Nov 22", "deadline_note": "Sun", "tags": ["seminar", "paid"], "url": "affine.org/program", "on_ruler": False},
                    {"name": "Tarbell Fellowship 2027", "org": "Tarbell Center", "desc": "A year of training in AI journalism, with a job placement at a newsroom. Paid.", "deadline": "2026-11-22", "deadline_short": "Nov 22", "deadline_note": "Sun", "tags": ["fellowship", "journalism"], "url": "tarbellcenter.org/fellowship", "on_ruler": False},
                    {"name": "Anthropic Residency", "org": "Anthropic", "desc": "Paid projects of 6 weeks to 6 months. Aimed at professors, founders and senior engineers, so probably not for now.", "deadline": "2026-11-22", "deadline_short": "Nov 22", "deadline_note": "listed", "tags": ["residency", "senior"], "url": "alignment.anthropic.com", "on_ruler": False},
                ]},
                {"title": "Opening soon: watch these", "items": [
                    {"name": "Kairos Pathfinder Fellowship, Spring 2027", "org": "Kairos", "desc": "Five months, part-time, for students who run university AI safety or policy groups. You get a mentor, money for your group, and a stipend. Starts Dec 6.", "deadline_short": "soon", "deadline_note": "not open", "tags": ["fellowship", "group leaders", "undergrad ok"], "url": "pathfinder.kairos-project.org", "star": True},
                    {"name": "SPAR, Spring 2027", "org": "SPAR", "desc": "Remote, part-time research for 3 months (5–40 hours a week). Open to undergrads. Applications open around December. There’s an interest form now.", "deadline_short": "Dec", "deadline_note": "opens", "tags": ["research", "remote", "undergrad ok"], "url": "sparai.org", "star": True},
                    {"name": "Apart Research weekend hackathons", "org": "Apart", "short": "Apart hackathon", "desc": "Free weekend events with local hubs: AI × Epistemics (Nov 13–15), Threat Intelligence (Dec 4–6), Agent Attribution (Dec 11–13). TAISI could host a Toronto hub again.", "deadline": "2026-11-13", "deadline_short": "Nov 13", "deadline_note": "starts", "tags": ["hackathon", "free", "host?"], "url": "apartresearch.com/sprints", "star": True},
                    {"name": "AI Safety Camp 12 · PRISM · LASR Labs", "org": "various", "desc": "Online research programs starting Jan 9 (AI Safety Camp) and Jan 31 (PRISM). LASR’s paid London summer program (£15,000) has a sign-up list.", "deadline_short": "—", "deadline_note": "not open", "tags": ["research"], "url": "aisafety.camp · prism-research.org · lasrlabs.org"},
                ]},
                {"title": "Later, and always open", "items": [
                    {"name": "Oxford AI governance PhD funding", "org": "Oxford AIGI", "desc": "Funded PhD spots starting October 2027. One for later.", "deadline": "2026-12-02", "deadline_short": "Dec 2", "deadline_note": "", "tags": ["PhD"], "url": "aigi.ox.ac.uk", "on_ruler": False},
                    {"name": "LawAI Summer Fellowships", "org": "Institute for Law & AI", "desc": "Two months from June 14, in Washington or Cambridge. For law students and lawyers.", "deadline": "2027-01-29", "deadline_short": "Jan 29", "deadline_note": "", "tags": ["law"], "url": "law-ai.org"},
                    {"name": "Money for TAISI projects", "org": "always open", "desc": "EA Infrastructure Fund ($1k–$500k), BlueDot quick grants (up to $20k), Coefficient Giving, Lightcone Commons, Manifund.", "deadline_short": "any time", "deadline_note": "", "tags": ["grants", "for groups"], "url": "funds.effectivealtruism.org · bluedot.org/grants"},
                ]},
             ], "note": "Recently closed: MATS Winter, Pivotal Q1, ERA Winter, Anthropic Fellows (January 2027) and Horizon 2027. Most dates come from aisafety.com. I checked them on the program’s own site for GovAI, SPAR, Kairos, LASR and Apart. Always check before you apply."},
         ]},
        # ------------------------------------------------------------------ WORLD
        {"id": "world", "title": "The World", "tab": "News", "aside": "The facts first. The opinions get labels.",
         "blocks": [
            {"type": "region", "region": "indonesia", "kicker": "Region one", "title": "Indonesia",
             "blurb": "A new labour law, fire season, and fish houses made from ash.",
             "map_points": [{"lon": 106.85, "lat": -6.2, "label": "Jakarta"}, {"lon": 114.6, "lat": -3.0, "label": "S. Kalimantan"}, {"lon": 140.7, "lat": -2.55, "label": "Jayapura", "anchor": "end"}],
             "stories": [
                {"lead": True, "tag": "Work", "headline": "Indonesia’s new employment law is now public",
                 "paras": ["The government has published Law No. 27 of 2026 on Employment Protection. Anyone can now read it online. Manpower Minister Yassierli announced this on Monday.",
                           "The law is long: 313 articles in 23 chapters. It covers equal opportunity, job training, informal work, foreign workers, wages, firing, and workplace inspections.",
                           "Parliament approved it on Oct 6. President Prabowo signed it on Oct 28, and it took effect the same day. Older rules from 2003 and 2023 still apply where they don’t clash with it."],
                 "why": "It sets the basic rules for how workers are treated across the country.", "outlet": "ANTARA", "date": "Nov 9", "url": "en.antaranews.com/news/441251"},
                {"tag": "Fires", "headline": "Two helicopter crashes lead to a review of air firefighting",
                 "paras": ["A firefighting helicopter crashed in South Kalimantan on Sunday. One Indonesian crew member died. Two crew from Australia and New Zealand survived.",
                           "Earlier in the week, an army helicopter also crashed while fighting fires in Central Kalimantan. The disaster agency (BNPB) is now checking its aircraft, its water-dropping methods, and crew fitness. Firefighting on the ground goes on."],
                 "why": "Dropping water from the air is a key part of fighting fires on Borneo.", "outlet": "ANTARA", "date": "Nov 9", "url": "en.antaranews.com/news/441315"},
                {"tag": "Fires", "headline": "The bigger plan: keep the peat wet",
                 "paras": ["Peat is soggy soil made of old plants. When it dries out, it burns easily and for a long time. The head of the peat and mangrove agency said on Monday that keeping peat wet is now the top priority.",
                           "The plan: build small dams in canals, send river water into dry peat, and replant the land. Old wooden dams that have leaked or rotted will be fixed. Villages will watch for hot spots and be the first line of defence. The government may reward villages that stop fires, ahead of strong El Niño years expected around 2029–2030."],
                 "why": "Preventing fires is cheaper and safer than fighting them.", "outlet": "ANTARA", "date": "Nov 9", "url": "en.antaranews.com/news/441427"},
                {"tag": "Economy", "headline": "Three laws stand between Indonesia and the OECD",
                 "paras": ["The OECD is a club of mostly rich countries that share economic rules. Indonesia wants to join by 2028.",
                           "Economic minister Airlangga Hartarto said three laws must be done in 2027: rules against bribing foreign officials, a new statistics law, and an updated competition law (the current one is from 1999). Reviews are done in 20 of 24 areas. The OECD’s leader visits on Nov 25."],
                 "why": "Joining means rewriting parts of the country’s economic rules.", "outlet": "ANTARA", "date": "Nov 9", "url": "en.antaranews.com/news/441331"},
                {"tag": "Good news", "headline": "Fish houses made from power-plant ash",
                 "paras": ["Off a beach in Jayapura, Papua, the state power company is sinking small concrete “fish houses” to make new reefs. About 30% of the mix is ash left over from burning coal.",
                           "Two tonnes of ash make 50 houses, each about 130 kg. After 60 days, sea life had started to move in. A local fisherman says he now has to go 10 km out to find fish, because erosion and trash pushed them away from shore.",
                           "A marine scientist adds a warning: the ash must be proven safe, and reefs take years to recover. Artificial reefs are one tool, not a full fix."],
                 "why": "One project tackles waste, damaged reefs, and fishing jobs at once.", "outlet": "ANTARA", "date": "Nov 9", "url": "en.antaranews.com/news/441267"},
                {"tag": "Culture", "headline": "An Indonesian theatre group wins a prize in Seoul",
                 "paras": ["Lab Teater Ciputat won a Special Jury Award at a theatre festival in Seoul. Their play is based on Malin Kundang, a West Sumatran folk tale about leaving home. The group hopes to do more projects with Korean artists."],
                 "why": "A small, real example of cultural ties across Asia.", "outlet": "ANTARA", "date": "Nov 8", "url": "en.antaranews.com/news/441191"},
                {"tag": "Banks", "headline": "Banks told to tighten cyber security",
                 "paras": ["The government and the financial regulator (OJK) asked banks to watch big transfers in real time and freeze odd ones until they’re checked. It follows a rise in cyber attacks on banks worldwide. The article gave no numbers for attacks in Indonesia."],
                 "why": "More of daily life now runs through bank apps.", "outlet": "ANTARA", "date": "Nov 9", "url": "en.antaranews.com/news/441383"},
             ]},
            {"type": "region", "region": "canada", "kicker": "Region two", "title": "Canada",
             "blurb": "The budget a week on, the jobs numbers, and the Bank of Canada’s rules.",
             "map_points": [{"lon": -75.7, "lat": 45.42, "label": "Ottawa"}, {"lon": -122.85, "lat": 49.19, "label": "Surrey"}, {"lon": -106.67, "lat": 52.13, "label": "Saskatoon"}, {"lon": -79.87, "lat": 43.26, "label": "Hamilton", "anchor": "end"}],
             "stories": [
                {"lead": True, "tag": "Budget", "headline": "The budget doesn’t mention foreign aid at all",
                 "paras": ["The federal budget came out on Nov 5. It doesn’t mention foreign aid or international development even once. The Canadian Press checked: every budget since 2010 did.",
                           "Aid groups think last year’s plan to cut $2.7 billion over four years still stands. They were relieved there were no new cuts. Foreign Affairs Minister Anita Anand says a foreign-policy update is coming “in a matter of weeks”."],
                 "views": "Aid groups call the budget “largely silent” on helping other countries. The ONE Campaign wants $5.5 billion a year. The government says aid is still a priority.",
                 "why": "It shows Ottawa is focusing its money at home.", "outlet": "The Canadian Press via Global News", "date": "Nov 7", "url": "globalnews.ca/news/12141139"},
                {"tag": "Jobs", "headline": "Canada lost 4,700 jobs in October",
                 "paras": ["Unemployment rose to 6.7%, Statistics Canada says. Young people are having a harder time finding work. The numbers came out the day after the budget, which said the job market was better than a year ago."],
                 "why": "The monthly numbers and the budget’s story don’t quite match.", "outlet": "CTV News (summary only)", "date": "Nov 6", "url": "ctvnews.ca (Canada lost 4,700 jobs)"},
                {"tag": "Money", "headline": "The Bank of Canada keeps its 2% goal",
                 "paras": ["Every five years, Ottawa and the Bank of Canada agree on the Bank’s main job. They just renewed it: keep inflation (how fast prices rise) near 2% a year.",
                           "The Bank sets interest rates on its own. Last week it raised its key rate for the first time in three years, because it worries rising prices could spread."],
                 "why": "This goal shapes the interest rate on every loan and mortgage.", "outlet": "The Canadian Press via BNN Bloomberg", "date": "Nov 5", "url": "bnnbloomberg.ca (inflation target renewal)"},
                {"tag": "Provinces", "headline": "Saskatchewan’s premier likes the budget, mostly",
                 "paras": ["Scott Moe called it “probably the best budget we’ve had in a decade, but that isn’t saying much.” He liked a new tax break on investments and a 10-year plan to end homelessness. He wanted more money for cities."],
                 "why": "Provinces decide a lot about how the budget plays out.", "outlet": "Global News", "date": "Nov 7", "url": "globalnews.ca/news/12139915"},
                {"tag": "Weather", "headline": "Storms knock out power on the B.C. coast",
                 "paras": ["Two storms hit B.C.’s south coast and Vancouver Island on Nov 7–8. A tree fell on two cars in Surrey and one driver died. There have been over 380,000 power outages since Friday; about 317,000 are fixed. A third storm was expected Monday."],
                 "why": "Repeated storms are testing the power grid.", "outlet": "Global News", "date": "Nov 8", "url": "globalnews.ca/news/12141788"},
                {"tag": "Ontario", "headline": "A Hamilton dental college may close",
                 "paras": ["The Southern Ontario Dental College trains dental hygienists and assistants. It says it may close as soon as next month, because Ontario has paused student aid (OSAP) for colleges like it."],
                 "why": "Student aid rules can decide whether small schools survive.", "outlet": "The Canadian Press via CTV (summary only)", "date": "Nov 9", "url": "ctvnews.ca (OSAP pause)"},
             ]},
            {"type": "region", "region": "usa", "kicker": "Region three", "title": "United States",
             "blurb": "A week after the midterms: who won, and what voters want fixed.",
             "map_points": [{"lon": -77.04, "lat": 38.9, "label": "Washington"}, {"lon": -111.1, "lat": 37.1, "label": "Lake Powell"}, {"lon": -89.6, "lat": 32.7, "label": "Mississippi", "anchor": "end"}],
             "chart": {"kind": "split", "title": "Who controls Congress (results so far)", "source": "Counts as of Nov 9, from the Sentinel newsletter. The dashed line is half the seats.", "rows": [
                 {"label": "Senate · 100 seats", "parts": [{"name": "Dem", "value": 54, "style": "solid"}, {"name": "Rep", "value": 44, "style": "grey"}, {"name": "?", "value": 2, "style": "outline"}]},
                 {"label": "House · 435 seats", "parts": [{"name": "Dem", "value": 254, "style": "solid"}, {"name": "Rep", "value": 162, "style": "grey"}, {"name": "not called", "value": 19, "style": "outline"}]},
             ]},
             "stories": [
                {"lead": True, "tag": "Economy", "headline": "After the midterms, the big issue is prices",
                 "paras": ["The Associated Press says voters on Nov 3 sent a clear message: fix inflation. Democrats now control Congress. Prices are up 3.7% from a year ago. AP links part of that to tariffs and to the war with Iran that began in February.",
                           "Jobs look fine: 165,000 were added last month, and unemployment is 4.1%. But the government borrows about $2 trillion a year, and interest on its debt now costs over $1 trillion a year. That is more than it spends on the military.",
                           "President Trump says he’ll work with Democrats “unless they want to be destructive.” Two senators from different parties are drafting a plan to fix Social Security, which is set to run short in 2032."],
                 "views": "Budget expert Marc Goldwein says controlling inflation and interest rates comes first. Harvard’s Jason Furman says AI investment is the bigger economic story.",
                 "why": "It sets the to-do list for the new Congress in January.", "outlet": "AP via PBS NewsHour", "date": "Nov 8", "url": "pbs.org/newshour (voters demanded economic relief)"},
                {"tag": "Politics", "headline": "Mississippi’s Senate race is still too close to call",
                 "paras": ["Democrat Scott Colom, a 43-year-old local prosecutor, is in a razor-thin race against Republican Senator Cindy Hyde-Smith. Late ballots are still being counted, and counties must finish by Friday.",
                           "If Colom wins, he would be Mississippi’s first Black senator since the 1870s. It wouldn’t change who controls the Senate."],
                 "why": "Close races show how much every ballot and every rule matters.", "outlet": "AP via PBS NewsHour", "date": "Nov 7", "url": "pbs.org/newshour (Colom, Mississippi)"},
                {"tag": "Water", "headline": "Floods give the dry Southwest a rare break",
                 "paras": ["Storms in late October flooded parts of the Southwest. Lake Powell, a huge reservoir on the Colorado River, rose more than 20 feet. It is still only about a quarter full.",
                           "Water managers won’t change their plans until they see next spring’s snow. A plan to cut water use in California, Nevada and Arizona is being fought in court."],
                 "why": "A wet month buys time, but the long drought isn’t over.", "outlet": "AP via PBS NewsHour", "date": "Nov 8", "url": "pbs.org/newshour (Lake Powell rises 20 feet)"},
             ]},
            {"type": "numbers", "title": "The US economy in four numbers", "items": [
                {"n": "3.7%", "label": "how much prices rose in a year"},
                {"n": "4.1%", "label": "unemployment rate"},
                {"n": "$2T", "label": "borrowed by the government each year"},
                {"n": "$1T+", "label": "yearly interest on the debt, more than the military"},
             ], "source": "AP via PBS NewsHour, Nov 8"},
            {"type": "region", "kicker": "Region four", "title": "Around the World",
             "blurb": "Six places, none of them about AI.",
             "stories": [
                {"lead": True, "tag": "Argentina", "headline": "The Pope tells Argentina: people come before the economy",
                 "paras": ["Pope Leo XIV arrived in Buenos Aires on Sunday. It’s the first papal visit to Argentina since 1987. In his first speech he said the economy must serve people, not the other way around. He also asked for more money for schools and universities, where funding has fallen about 40% since 2023.",
                           "That lands as a message to President Javier Milei, who has made deep spending cuts. Milei has brought inflation down from about 200% to about 32% and balanced the budget. But real wages are still below 2023 levels, and about 300,000 formal jobs are gone."],
                 "views": "Milei’s government says the cuts are needed reform. Argentina’s bishops have criticized his government in most of their policy statements.",
                 "why": "A religious leader is openly weighing in on how a country runs its economy.", "outlet": "AP via PBS NewsHour", "date": "Nov 8", "url": "pbs.org/newshour (Pope arrives in Argentina)"},
                {"tag": "Israel", "headline": "An opposition leader gets the first try at forming a government",
                 "paras": ["Israel’s Oct 27 election gave no side a majority. On Sunday, President Herzog gave opposition leader Gadi Eisenkot, a former army chief, 28 days to build a coalition. Arab-led parties made record gains, and one says it will back him. Netanyahu stays on as caretaker until a new government forms."],
                 "views": "Netanyahu has claimed, without evidence, that Arab parties “stole” the election. Election officials say the vote was valid.",
                 "why": "Israel may get its first new prime minister in years.", "outlet": "AP via PBS NewsHour", "date": "Nov 8", "url": "pbs.org/newshour (Eisenkot)"},
                {"tag": "Iran", "headline": "Iran warns the US as talks stall",
                 "paras": ["Iran’s foreign minister warned that Iran would “rain down hell” if the US attacks again. He said talks slowed because of the US elections. President Trump said new strikes were “highly unlikely” if talks on Iran’s nuclear program and shipping in the Strait of Hormuz make progress. An oil tanker hit a sea mine near the strait, Iranian state media said."],
                 "why": "The war affects oil prices, and so prices everywhere.", "outlet": "Al Jazeera", "date": "Nov 8", "url": "aljazeera.com (Iran threatens)"},
                {"tag": "South Africa", "headline": "The ANC has its worst local election since 1994",
                 "paras": ["In local elections on Nov 4, the ANC got about 31% of the vote. It’s still the biggest party, but about 120 town councils now have no party in control. Parties have 14 days to make deals. Voters say water shortages, power cuts and poor services drove their choices."],
                 "why": "Coalition deals will decide who runs cities like Johannesburg.", "outlet": "Africanews", "date": "Nov 8", "url": "africanews.com (ANC suffers major blow)"},
                {"tag": "Moldova", "headline": "A new power line to Romania cuts reliance on Russia",
                 "paras": ["Moldova opened a high-voltage line linking it to Romania and the EU’s power market. It means Moldova no longer has to rely on a power plant in Russian-backed Transnistria. The president says Moldova now buys “zero Russian gas”. The line opened about two years late."],
                 "why": "Energy is how big neighbours put pressure on small countries.", "outlet": "Al Jazeera (AFP)", "date": "Nov 9", "url": "aljazeera.com (Moldova power line)"},
                {"tag": "Germany", "headline": "Germany may get its first woman president",
                 "paras": ["Chancellor Friedrich Merz says he’ll nominate Ilse Aigner, 61, a Bavarian politician and former farm minister. The vote is Jan 30, and she is almost sure to win. Germany’s president is mostly a ceremonial job, but can act as a neutral referee in a crisis."],
                 "why": "A symbolic first for one of Europe’s biggest countries.", "outlet": "Al Jazeera (AFP, DPA, Reuters)", "date": "Nov 8", "url": "aljazeera.com (Aigner)"},
             ]},
            {"type": "chart", "title": "South Africa’s local election, Nov 4", "sub": "Share of the vote. No party has half, so deals decide who governs.", "kind": "bars", "unit": "%", "max": 50,
             "rows": [{"label": "ANC", "value": 30.8, "style": "solid"}, {"label": "Democratic Alliance", "value": 24.6, "style": "grey"}, {"label": "MK Party", "value": 9.8, "style": "outline"}],
             "source": "Electoral Commission figures, via Africanews"},
            {"type": "box", "label": "How many people marched in Amsterdam?", "paras": [
                "On Sunday, a large crowd marched in Amsterdam to ask the Dutch government to cut ties with Israel over the war in Gaza. How large? Al Jazeera said hundreds of thousands. Africanews said tens of thousands. The South China Morning Post said around 20,000.",
                "Those numbers are up to ten times apart. Crowd sizes are hard to count, and each side has reasons to count high or low. When you see a crowd number, ask who counted.",
             ]},
            {"type": "region", "kicker": "Region five", "title": "Science",
             "blurb": "Two careful steps forward.",
             "stories": [
                {"tag": "Space", "headline": "A pretend Mars crew walks out after a year",
                 "paras": ["Four people spent just over a year inside a 3D-printed “Mars” house at NASA in Texas. They grew food, did fake spacewalks, and waited 13 to 22 minutes for every message from mission control. They even had two weeks with no contact at all. They came out on Oct 31.",
                           "NASA will use what it learned to plan real trips to Mars, which it says could come in the early 2030s."],
                 "why": "Being alone and far away may be harder than the rocket part.", "outlet": "Nature", "date": "Nov 9", "url": "nature.com/articles/d41586-026-03588-w"},
                {"tag": "Health", "headline": "How the Ozempic drug may protect kidneys",
                 "paras": ["Scientists looked at kidney samples from 106 people with diabetes and kidney disease, before and after treatment. People on semaglutide (the drug in Ozempic) had better blood flow and less scarring than people on a fake pill. Earlier studies showed fewer kidney failures; this one starts to explain why."],
                 "why": "It suggests the drug helps kidneys directly, not just through weight loss.", "outlet": "Science News", "date": "Nov 9", "url": "sciencenews.org (semaglutide)"},
             ]},
            {"type": "box", "style": "tint", "label": "Bubble check", "paras": [
                "About half the newsletters in your inbox since Friday were about AI. None of today’s 24 news stories is. For a change of pace this week, try the Astral Codex Ten review of Walter Ong’s Orality and Literacy. It’s about how learning to write changed the way people think.",
            ]},
         ]},
        # ------------------------------------------------------------------ ESSAYS
        {"id": "essays", "title": "The Essays", "tab": "Read slowly", "aside": "Printed whole, in the writers’ own words",
         "blocks": [
            {"type": "essay", "essay_id": "1a1bd77f3e6cfc5b", "kicker": "Persuasion · Nov 8 · Opinion", "priority": 3,
             "title": "The Midterms Just Made the World More Dangerous", "author": "Francis Fukuyama", "publication": "Persuasion",
             "dek": "A famous political scientist argues that America’s rivals now have a two-year window to act.",
             "paras": FUKUYAMA, "source_note": "persuasion.community/p/the-next-two-years-might-be-more · from your subscription email",
             "counter_label": "In plain words, and the other side",
             "counterpoint": [
                 "The short version: Fukuyama thinks Trump is weak for two years and friendly to China, Russia and North Korea. So those countries might act now, before a tougher president arrives in 2029.",
                 "Things to keep in mind. This is opinion, from a writer who strongly opposes Trump. It is a guess about what other leaders might do, not a report. Others argue that a weakened president makes adventures riskier, not safer, for rivals, and that China has its own reasons (its economy, its army’s readiness) that don’t depend on who is in the White House.",
             ]},
            {"type": "essay", "essay_id": "1a1c03f311b75abb", "new_page": True, "optional": True, "priority": 1, "kicker": "ChinAI #381 · Nov 9",
             "title": "China’s Venture Capital Market Is Defying Common Sense", "author": "Jeffrey Ding (translating Liu Xiaoqing)", "publication": "ChinAI Newsletter",
             "dek": "A Chinese analyst lists five ways money for new tech companies has gone wrong.",
             "paras": CHINAI, "source_note": "chinai.substack.com/p/chinai-381-chinas-venture-capital · full translation linked there",
             "counter_label": "Why it’s here",
             "counterpoint": [
                 "It’s a view from inside China, translated, about how startups get money. Compare it with Noah Smith’s “China bear” post in the Newsstand. Both say China’s state-driven model has limits, but from very different angles.",
             ]},
            {"type": "essay", "essay_id": "1a1bb1c55bd40fe7", "new_page": True, "optional": True, "priority": 0, "kicker": "Homo Economicus · Nov 8 · Opinion",
             "title": "The Least of All Freedoms", "author": "Nicholas Decker", "publication": "Homo Economicus",
             "dek": "An economist argues we should let smarter machines make our big decisions.",
             "paras": T["decker"], "source_note": "nicholasdecker.substack.com/p/the-least-of-all-freedoms · from your subscription email",
             "counter_label": "In plain words, and the other side",
             "counterpoint": [
                 "The short version: Decker says political freedom mostly means the power to push other people around. So if a smarter AI made decisions instead, we wouldn’t lose much. Note the last line: the post is sponsored by Mechanize, a company that builds AI to automate work.",
                 "The other side. (1) Democracy’s best feature may be that you can remove bad leaders without violence. You can’t vote out a machine. (2) “Smarter” only helps if the AI wants what we want, and that is the alignment problem itself. (3) Courts work partly because people can overrule them over time, so his comparison cuts both ways.",
                 "A question for the 1:30 session today: what would you need to see before trusting a judge you could never remove?",
             ]},
         ]},
        # ------------------------------------------------------------------ NEWSSTAND
        {"id": "stand", "new_page": False, "title": "The Newsstand", "tab": "Your inbox", "aside": "Everything else that arrived, summed up",
         "blocks": [
            {"type": "newsstand", "items": [
                {"essay_id": "1a1bb1c55bd40fe7", "pub": "Homo Economicus", "author": "Nicholas Decker", "title": "The Least of All Freedoms", "mode": "in full", "summary": "Printed in full in the essays.", "long": True, "fallback": [
                    "Opinion. An economist argues we should hand big decisions to smarter AI. His reason: political freedom mostly means the power to push other people around, so we wouldn’t lose much. He compares an AI ruler to a very wise judge.",
                    "The other side: you can vote out bad leaders, but not a machine; “smarter” only helps if the AI wants what we want; and courts work partly because people can overrule them over time. Note: the post is sponsored by Mechanize, which builds AI to automate jobs."]},
                {"essay_id": "1a1c03f311b75abb", "pub": "ChinAI #381", "author": "Jeffrey Ding", "title": "China’s venture capital market is defying common sense", "mode": "in full", "summary": "Printed in full in the essays.", "long": True, "fallback": [
                    "A Chinese analyst, Liu Xiaoqing, says money for new tech companies in China (especially robot “embodied AI” startups) has gone wrong in five ways. Founders get huge valuations just for their résumés. Teams are thrown together by bankers and never really gel. Startups act like giant companies from day one. Much of the money comes from government funds with strings attached, and few of them have ever cashed out. So the whole system is fragile.",
                    "Her best line: a team that meets at a dinner, then at the deal table, then at the signing “isn’t a partnership; that’s assembling a party for a video game quest.” In the 2010s, she says, failures were “clean” and made the soil richer. Today there’s no time and no tolerance for failure."]},
                {"essay_id": "1a1c1d7ea4b49307", "pub": "Sentinel Global Risks Watch", "title": "AI may be speeding up AI research", "mode": "summary", "long": True, "paras": [
                    "This weekly risk report leads with AI. Anthropic told investors its AI may soon double the speed of its own AI research. METR, an outside testing group, spent August to October inside Anthropic and agreed: about a 2× speed-up on clear, well-defined tasks (somewhere between 1.3× and 3×).",
                    "Reactions split. Some forecasters say this makes super-smart AI likely within one or two years. Others, like Oxford’s Toby Ord, say there may be other explanations. Sentinel’s own forecasters give a 6% chance (range 0.2% to 50%) that AI causes human extinction in the next ten years, and an 11% chance the US orders a pause on frontier AI before 2028.",
                    "It also covers the midterms (seat counts on the World page), a UK warning of an AI-enabled cyber attack on key services by 2028, and oil falling below $100 a barrel on hopes the Iran war ends sooner.",
                ]},
                {"essay_id": "1a1c0d360df73dd5", "pub": "Persuasion", "author": "Damon Linker", "title": "The True Believer", "mode": "summary", "long": True, "paras": [
                    "Opinion. After the midterms, some hoped Trump would soften. Linker says that hope ended when Trump made Stephen Miller his chief of staff. Past presidents (Clinton, Bush, Obama) moved to the middle after losing midterms. Linker argues Trump is doing the opposite.",
                    "His main worry: Miller has pushed to suspend habeas corpus (the right to challenge being locked up) for non-citizens and to use the Insurrection Act against protesters. Linker says the danger is a leader who keeps calling things an “emergency” to justify stepping outside normal law. He expects a possible constitutional crisis in the next two years.",
                    "Keep in mind: Persuasion opposes Trump. Miller’s supporters say he is carrying out the immigration policies Trump campaigned on.",
                ]},
                {"essay_id": "1a1c163db54ba802", "pub": "Forethought", "title": "Two Kinds of Test-Time Scaling", "mode": "summary", "long": True, "paras": [
                    "When AI “thinks longer” on a problem, it usually does better. The author asks: can it keep improving even past the longest thinking it ever did in training? He calls that “compute extrapolation.”",
                    "He argues it started around late 2025, when models learned to summarise their own notes and keep going. If true, three things follow. The most impressive AI feats will improve faster. Safety testing gets very expensive, since you can never be sure what a model could do with more time. And companies may race by spending huge sums on single hard problems. He admits the evidence is indirect. About 3,800 words: a good one to print in full on a lighter day.",
                ]},
                {"essay_id": "1a1b7deb2c081195", "pub": "Noahpinion", "author": "Noah Smith", "title": "Why I’m becoming a China bear", "mode": "summary", "long": True, "paras": [
                    "A long-time believer in China’s rise changes his mind. He still thinks China will be very powerful, but no longer thinks it will run the world. His reasons: China’s push to make everything is hitting limits. Export markets are full, people at home aren’t spending since the housing crash, and many factories make little profit. Building roads and trains has also levelled off.",
                    "His biggest reason, AI, is behind the paywall. Pair it with the ChinAI essay on the previous pages.",
                ]},
                {"essay_id": "1a1bfff966d27820", "pub": "Slow Boring", "author": "Matthew Yglesias", "title": "The rise of the Hispanic moderate", "mode": "summary", "paras": [
                    "Democrats once assumed a growing Hispanic population would hand them easy wins. Yglesias calls that a big mistake: many Hispanic voters are moderate. Trump made gains with them in 2020 and 2024. In 2026 many came back to Democrats, partly because of Trump, and partly because Democrats ran more moderate Latino candidates. (Paywalled after the opening.)",
                ]},
                {"essay_id": "1a1c0c7407f83360", "pub": "Don’t Worry About the Vase", "author": "Zvi Mowshowitz", "title": "AI R&D Is Accelerating Towards Potential RSI in 2027", "mode": "blurb", "summary": "A very long read on the same METR report: how much AI now speeds up AI research, and whether that leads to AI improving itself (“RSI”) as soon as 2027."},
                {"essay_id": "1a1c08693dc9291f", "pub": "Import AI 480", "author": "Jack Clark", "title": "Space economies, AI for science, robot hands", "mode": "blurb", "summary": "A weekly research roundup. It opens with a question: when will we have robots on the Moon?"},
                {"essay_id": "1a1c1217386b5aa2", "pub": "Bentham’s Newsletter", "title": "The Scariest Recent AI Development", "mode": "blurb", "summary": "Argues that AGI might be close. (Saturday’s post defended Anthropic’s CEO against his critics.)"},
                {"essay_id": "1a1b7259af5586af", "pub": "Torchbearer Community", "title": "The advocacy gap in international AI verification", "mode": "blurb", "summary": "Argues that checking whether countries keep AI agreements is possible, and politically doable."},
                {"essay_id": "1a1b2c85152553f5", "pub": "Astral Codex Ten", "title": "Your Book Review: Orality and Literacy", "mode": "saved", "summary": "A reader’s review of Walter Ong’s classic book about how writing changes thinking. Long. Saved for a lighter day."},
                {"essay_id": "1a1b5b2f462b6edc", "pub": "Yascha Mounk", "title": "Martin Wolf on democratic capitalism after Trump", "mode": "podcast", "summary": "A 76-minute talk: can democracy recover from populism, is AI a bubble, and could France cause the next euro crisis?"},
                {"essay_id": "1a1c162ac8d53883", "pub": "Visual Capitalist", "title": "The world’s biggest economies vs. debt in 2026", "mode": "chart", "summary": "The US has the biggest economy, but Sudan has the most debt compared with its size. The chart is only online."},
            ]},
         ]},
        # ------------------------------------------------------------------ ABOUT
        {"id": "colophon", "new_page": False, "in_index": False, "title": "About This Paper", "tab": "Colophon", "aside": "Issue zero is a test",
         "blocks": [
            {"type": "colophon", "parts": [
                {"title": "Where today’s news came from", "paras": [
                    "Your Google Calendar. Gmail labels News, UofT, Quercus and Luma. All eleven TAISI Slack channels. ANTARA, The Canadian Press, Global News, CTV, BNN Bloomberg, AP (via PBS), Al Jazeera, Africanews, Nature and Science News. Opportunities from aisafety.com and the programs’ own sites.",
                ]},
                {"title": "House rules", "paras": [
                    "Plain words. No “breaking”, no shouting. Every story says why it matters. If people disagree, you see both sides. Opinion is labelled. The paper has an end, and that’s the point.",
                ]},
                {"title": "Not here yet", "paras": [
                    "Todoist, your other two Slack workspaces, Discord, Toronto events from Luma, and news photos. Quercus and UofT mail start once you confirm the Quercus email.",
                ]},
            ]},
         ]},
    ],
    "gallery": {"src": "assets/art/processed/overworld.png", "caption": "Katsushika Hokusai, Famous Places on the Tōkaidō in One View (c. 1818). UBC Library, no known copyright restrictions."},
    "back": {
        "src": "assets/art/processed/back-01-nihonbashi.png",
        "kicker": "The Road · Stop 1 of 55",
        "title": "Nihonbashi: Morning View · Hiroshige, c. 1834",
        "caption": "Every trip on the Tōkaidō, the great road from Edo (now Tokyo) to Kyoto, started at this bridge. Here a lord’s parade crosses at dawn while fish sellers wait to get by. Hiroshige made 55 prints of the road. This paper will show one each issue. Turn the page sideways to see it the right way up.",
        "credit": "Public domain. Cooper Hewitt, Smithsonian Design Museum, via Wikimedia Commons.",
    },
}

(HERE / "issue.json").write_text(json.dumps(issue, indent=1, ensure_ascii=False))
print("written")
