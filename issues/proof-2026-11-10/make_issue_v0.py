# One-off: the proof issue for Tue 10 Nov 2026, assembled by hand in the setup session.
# Daily issues are written straight to issue.json by the morning run.
import json
from pathlib import Path

WEATHER = {"daily": [
    {"date": "2026-11-10", "day_of_week": "Tuesday", "high": 16.0, "low": 5.4, "precipitation_chance": 10, "precipitation_type": "rain"},
    {"date": "2026-11-11", "day_of_week": "Wednesday", "high": 11.8, "low": 5.3, "precipitation_chance": 35, "precipitation_type": "rain"},
    {"date": "2026-11-12", "day_of_week": "Thursday", "high": 6.1, "low": 1.5, "precipitation_chance": 15, "precipitation_type": "rain"},
    {"date": "2026-11-13", "day_of_week": "Friday", "high": 5.5, "low": 1.5, "precipitation_chance": 15, "precipitation_type": "snow"},
    {"date": "2026-11-14", "day_of_week": "Saturday", "high": 6.5, "low": 1.7, "precipitation_chance": 10, "precipitation_type": "snow"},
]}

DECKER = [
    "Bryan Caplan (professor of economics at George Mason University) recently tweeted the following: [the tweet, an image in the original email, is not reproduced here — in it Caplan welcomed the idea of handing more decision-making to AI].",
    "A lot of people on twitter disliked this. Much of the criticism was vulgar and sexual in nature. That which wasn’t focused on how turning over decision making to an AI would reduce human freedom. I believe this is false, and is deeply confused about what freedom is. I would support turning over as much decision making as possible to more intelligent entities in the future, and believe that it would be a substantial improvement over the status quo.",
    "We should start by defining what freedom is. Consider a set of choices. To restrict the number of choices possible is to reduce our freedom. To expand it is to increase it. Given the choice between a ham and a turkey sandwich, to ban the individual from picking ham is to reduce their freedom, while to allow someone to pick egg salad is to increase it.",
    "Now of course, some actions are incompatible with the choice sets of other people. If I am to take the ham sandwich which someone else intends to eat, I have reduced their freedom. We therefore agree not to do things which reduce the choice sets of other people, and agree to take coercive action against those who would do those things.",
    "That is the core function of government. It is not the only thing which it does, of course. Although we have done an excellent job of hiding it, politics are about violence. What is decided in the political process is who should be able to coerce whom, and to what extent. We do not call it theft, of course – we call it taxes – but its violent nature is still the same. If one does not pay their taxes, they are arrested; if they decline to be arrested, they are killed. The government exists largely to take ham sandwiches from some people and give them to others. A fifth of our whole production every year is given and taken in transfers, largely from the young to the old. It is the struggle of group against group.",
    "To prevent us from destroying ourselves, we are bound by past commitments. We have a Constitution, and in it we enumerate rights which cannot be violated. We are to have free speech. We have the right to have our case heard by a jury of our peers in the event that we are accused of restricting the choice sets of other people. We cannot write a bill of attainder. We formerly restricted ourselves from levying an income tax. When we find that we want to break these chains we have placed on ourselves, we turn over the decision making to a court. These individuals are selected in a process kept (historically) as far away from conscious politicking as possible, on the basis of intellectual merit, and their decisions, while unpopular, must be followed.",
    "To turn over the government to AI would be to take our disputes for arbitration. If we agree that smarter and wiser judges are better, then why would we not take our disputes and our problems to the smartest and wisest judge?",
    "All of these are restrictions on political freedom. But political freedom is the least of all freedoms. Retaining political freedom means simply retaining the option to harm others. The courts restrict your political freedom, because you cannot vote with your compatriots to lynch someone. We cannot keep ourselves from the cookies in the box, but we can do our best to throw the ability to harm others so far out of reach that we cannot pick it back up again.",
    "I am not impressed by the voter, as I have written before. I believe that his ignorance is a strength, because it keeps him from doing what he wants. The voter wants to hurt others to accomplish impossible ends. He wants to restrict the freedom of billions to live and work and love where they wish; he wants to take from others to support himself; he wants to restrict the freedom of others under the banner “common sense”. He is callous, shallow, and conceited.",
    "And yet, it has never been desirable for the people to be without power, for the power of the government could equally well be used to oppress them. There must be some sort of check on the government to prevent tyranny. Until, perhaps, soon.",
    "I find the notion that there is anything special about human government deplorable. You, already, are substantially disenfranchised. It’s called representative democracy. So that we are not subject to the ignorant whims of the people, we separate out the decision making process, and give it to people who are subject only to the infrequent check of the voters. To change who makes decisions makes you no more a slave than you were before.",
    "Those who want our decisions to be made by humans are like those who celebrate an anti-colonial dictator. What good does it do you to be oppressed by tyrants with the same skin color as you? Perhaps you have notions that you will be the one deciding things in the future. Of course, lots of people think that, and they can’t all be right.",
    "Humans have been in power a long time. And what have they done with it? We have grown, yes. We are lucky that such a flourishing has been possible. But we have grown far less than we would otherwise have, were it not for violence and the exploitation of man by man. Much of the world is still in poverty, caused by misrule. I hope that we can do better.",
    "It is possible that we never do want to hand over our decision making to an AI. Perhaps we can never trust it enough, or perhaps we might be unable to bind ourselves to the AI’s decisions. There are obviously practical obstacles which might interfere.",
    "But we should be clear about one thing. There is something special about humans making decisions for themselves, but there is nothing special about when they make decisions for others. Freedom is not the power to oppress others.",
    "## P.S.",
    "There are two basic categories of AI risk. Either AI escapes our control, and causes a catastrophe, or AI remains in our control, and humans use it to oppress us. These two dangers have different implications for development. The possibility of AI escaping our control encourages us to go slowly so that we have more time to monitor. But the possibility of humans using AI to oppress us tells us to go faster – so that the men with guns, who are for now doddering and stupid, don’t realize that they have lost their power until it is too late.",
    "This post is brought to you by Mechanize, Inc. They are hiring for a variety of positions, including software engineers. I encourage you to apply here. I promise that my views are entirely independent of my sponsorship.",
]

issue = {
    "date": "2026-11-10",
    "date_long": "Tuesday, November 10, 2026",
    "weekday": "Tuesday",
    "number": "0 (proof)",
    "edition": "Morning edition",
    "weather": WEATHER,
    "front": {
        "lede": [
            "A day at the Design Exchange. AI Safety Week’s second day gives you three sessions nearly back to back, from 11:15 to 4:45, all at 234 Bay Street — and the weather is kind: dry, with a high of 16°. One small job before you leave: confirm the Quercus forwarding email, or the university part of this paper will stay empty.",
            "Elsewhere: the US absorbs its midterms, Canada’s budget turns five days old, and Indonesia publishes a new labour law. The essay argues for handing decisions to AI; a counterweight follows.",
        ],
        "today": [
            {"time": "11:15", "what": "Forecasting: Jobs and the Economy (MIT FutureTech)", "where": "AI Safety Week, Day 2 · Design Exchange, 234 Bay St · until 12:30 (time moved from 10:45)"},
            {"time": "1:30", "what": "Post-AGI Civilization: What’s the Destination? (David Duvenaud)", "where": "Design Exchange · until 3:00"},
            {"time": "3:15", "what": "Research & Ideas Gallery — posters and open conversation", "where": "Design Exchange · until 4:45"},
            {"time": "—", "what": "Assessing Loss-of-Control Risk: you are on the waitlist", "where": "AI Safety Week, Day 2 · Luma will email if a spot opens", "dim": True},
        ],
        "todos": [
            {"topic": "Academics", "items": [
                {"text": "Confirm your Gmail address in Quercus — open “Confirm Email: Canvas” (Nov 9) and click the link.", "src": "Quercus", "urgent": True},
            ]},
            {"topic": "TAISI", "items": [
                {"text": "Vote on the end-of-semester social, Sat Nov 28 at 6 pm (thumbs up / shrug / down on Joseph’s post).", "src": "#taisi-team"},
                {"text": "Book the writing-desk room for weeks 3 and 4 once the booking window opens.", "src": "#writing-desk"},
                {"text": "Check the OpenRouter key sheet: “Given to” and “Email” filled for every key handed out.", "src": "#hackathons"},
            ]},
            {"topic": "Misc", "items": [
                {"text": "Decide on the GovAI summer fellowships — both close Sunday, Nov 22.", "src": "Opportunities"},
                {"text": "Connect Todoist so your own list appears here.", "src": "setup"},
            ]},
        ],
    },
    "sections": [
        {"id": "desk", "title": "Your Desk", "aside": "What needs you, and what happened in TAISI",
         "blocks": [
            {"type": "agenda", "title": "This week", "items": [
            {"time": "Wed", "what": "Day 3: Forecasting AI-Enabled Power Concentration Risk (MIGS)", "where": "11:15–12:15 · Design Exchange"},
            {"time": "Nov 17", "what": "Colloquium co-working session (proposed, 4–6 pm)", "where": "#colloquium", "dim": True},
            {"time": "Nov 26", "what": "AI Math Capabilities: A Fireside Chat", "where": "6–9 pm · Trajectory Labs · registered"},
            {"time": "Nov 28", "what": "TAISI team social (proposed, 6 pm)", "where": "#taisi-team · vote pending", "dim": True},
        ]},
            {"type": "attention", "title": "Needs you", "items": [
                {"what": "Quercus forwarding isn’t finished.", "detail": "Canvas sent a confirmation link to your Gmail on Nov 9. Until you click it, course announcements won’t reach this paper.", "src": "Gmail · Quercus label"},
                {"what": "Two deadlines in twelve days.", "detail": "GovAI’s UK and DC Summer Fellowships 2027 close Sunday, Nov 22 (stipend; early-career welcome; applicants from anywhere).", "src": "governance.ai"},
                {"what": "A fellowship built for TAISI people.", "detail": "Kairos Pathfinder (Spring 2027) pairs student AI-safety group organizers with mentors and group funding. Not open yet; starts Dec 6, so it may open any day.", "src": "aisafety.com"},
            ]},
            {"type": "channels", "title": "TAISI Slack · last week", "channels": [
                {"name": "#taisi-team", "points": [
                    "Joseph proposes an end-of-semester team social on Saturday, Nov 28 at 6 pm and asked everyone to react to vote.",
                    "Annie fell ill (likely strep) before the weekend; Giles and Tazik covered the Saturday and Sunday cohorts.",
                    "Isabel’s request after the hackathon food mix-up: post food orders in the main channel, not in threads — she doesn’t get thread notifications.",
                ]},
                {"name": "#f26-facilitators", "points": [
                    "Facilitator coordination has moved here (Boyan). Cohorts: Saturday 6–7:30 (7 signed up), Sunday 5:30–7 (10).",
                    "Tazik shared the slides from the mech-interp talk (Nov 8).",
                    "The week-5 reading list was running late on Nov 4; Joseph promised it by midday the next day.",
                ]},
                {"name": "#colloquium", "points": [
                    "Lessons from the last talk: tell speakers the audience’s level explicitly, book the room until 8 pm, and keep BA2135 — the AV worked well.",
                    "Proposed: a co-working session Tuesday, Nov 17, 4–6 pm; Pera will ask Ayushman to speak; an AI-2027 explainer is on the table.",
                ]},
                {"name": "#phl-panel", "points": [
                    "Working title: “After AGI: What Might a Good Outcome for Humanity Look Like?” David Duvenaud is confirmed and will talk about his MATS mentorship work.",
                ]},
                {"name": "#hackathons", "points": [
                    "The Swarm Alignment Hackathon ran Nov 6–8. Each participant got a $50 OpenRouter key; the hub coordinator asked that every key handed out be logged in the sheet.",
                ]},
                {"name": "#si-main", "points": [
                    "Oscar asked for AI Safety Week volunteers for Tuesday and Wednesday — that’s today and tomorrow, if you want to help between sessions.",
                ]},
            ]},
            {"type": "events", "title": "Your events (from Luma)", "items": [
                {"when": "Nov 10", "time": "Tue", "name": "AI Safety Week, Day 2", "detail": "Three sessions approved; one waitlisted (Loss-of-Control Risk).", "status": "approved"},
                {"when": "Nov 11", "time": "Wed", "name": "AI Safety Week, Day 3", "detail": "Forecasting AI-Enabled Power Concentration Risk, 11:15.", "status": "approved"},
                {"when": "Nov 26", "time": "Thu", "name": "AI Math Capabilities: A Fireside Chat", "detail": "Trajectory Labs, 6–9 pm.", "status": "registered"},
                {"when": "Nov 6–8", "time": "hosted", "name": "Swarm Alignment Hackathon Toronto", "detail": "Wrapped. Ilyass sent the slides to guests on Nov 8; Luma counted 38 registrations before late cancellations.", "status": "done"},
            ]},
         ]},
        {"id": "opps", "new_page": False, "title": "Opportunities", "aside": "So nothing slips past you",
         "blocks": [
            {"type": "opportunities", "ruler_days": 28, "groups": [
                {"title": "Closing in the next two weeks", "items": [
                    {"name": "Frontier AI Governance course", "org": "AI Safety Montréal", "short": "Montréal gov.", "desc": "Five-week part-time course on the BlueDot curriculum, from Nov 17.", "deadline": "2026-11-10", "deadline_short": "Nov 10", "deadline_note": "today", "tags": ["course", "Canada", "low bar"], "url": "aisafetymontreal.org/programs", "on_ruler": False},
                    {"name": "Gen Stream, Cohort 2", "org": "Gen Stream", "short": "Gen Stream", "desc": "Seven-day workshop in Oxford for generalists — operators, builders, communicators — moving into AI safety. Expenses covered; starts Nov 22.", "deadline": "2026-11-11", "deadline_short": "Nov 11", "deadline_note": "tomorrow", "tags": ["workshop", "ops-friendly", "funded"], "url": "genstream.org", "star": True},
                    {"name": "CLR Fundamentals Program", "org": "Center on Long-Term Risk", "short": "CLR Fund.", "desc": "One-month online course from Nov 20: s-risks, model personas, multi-agent safety.", "deadline": "2026-11-16", "deadline_short": "Nov 16", "deadline_note": "Mon", "tags": ["course", "online", "low bar"], "url": "forum.effectivealtruism.org (CLR Fundamentals autumn 2026)", "star": True},
                    {"name": "AGI Strategy course", "org": "AI Safety Montréal", "short": "AGI Strategy", "desc": "One-month part-time course from Nov 23, in English or French.", "deadline": "2026-11-16", "deadline_short": "Nov 16", "deadline_note": "Mon", "tags": ["course", "Canada"], "url": "aisafetymontreal.org/programs"},
                    {"name": "Iliad Intensive (January 2027)", "org": "Iliad", "short": "Iliad", "desc": "Four weeks in Berkeley on foundational alignment research for people with math, physics or CS backgrounds. Expenses covered.", "deadline": "2026-11-16", "deadline_short": "Nov 16", "deadline_note": "Mon", "tags": ["bootcamp", "funded", "math"], "url": "iliad.ac/calendar"},
                    {"name": "GovAI UK Summer Fellowship 2027", "org": "Centre for the Governance of AI", "short": "GovAI UK + DC", "desc": "Three months in London, June 7 – Aug 27, research or applied track. Stipend. Early-career welcome; applications from anywhere.", "deadline": "2026-11-22", "deadline_short": "Nov 22", "deadline_note": "Sun", "tags": ["fellowship", "stipend", "undergrad ok"], "url": "governance.ai/opportunities", "star": True},
                    {"name": "GovAI DC Summer Fellowship 2027", "org": "Centre for the Governance of AI", "desc": "Bipartisan, three months in Washington, aimed at careers in American AI policy. Stipend.", "deadline": "2026-11-22", "deadline_short": "Nov 22", "deadline_note": "Sun", "tags": ["fellowship", "stipend", "US focus"], "url": "governance.ai/post/dc-summer-fellowship-2027", "on_ruler": False},
                    {"name": "AFFINE Superintelligence Alignment Seminar", "org": "AFFINE", "short": "AFFINE · Tarbell · Anthropic Res.", "desc": "Four weeks from Jan 4 on the philosophical foundations of alignment. Stipend.", "deadline": "2026-11-22", "deadline_short": "Nov 22", "deadline_note": "Sun", "tags": ["seminar", "stipend"], "url": "affine.org/program", "on_ruler": False},
                    {"name": "Tarbell Fellowship 2027", "org": "Tarbell Center", "desc": "A year of AI journalism training and a newsroom placement, from June 2027. Stipend.", "deadline": "2026-11-22", "deadline_short": "Nov 22", "deadline_note": "Sun", "tags": ["fellowship", "journalism"], "url": "tarbellcenter.org/fellowship", "on_ruler": False},
                    {"name": "Anthropic Residency", "org": "Anthropic", "desc": "Mentored project placements of 6 weeks to 6 months. Aimed at professors, founders and staff engineers — worth knowing, likely not for now.", "deadline": "2026-11-22", "deadline_short": "Nov 22", "deadline_note": "per aisafety.com", "tags": ["residency", "senior"], "url": "alignment.anthropic.com/2026/anthropic-residency", "on_ruler": False},
                ]},
                {"title": "Opening soon — watch these", "items": [
                    {"name": "Kairos Pathfinder Fellowship, Spring 2027", "org": "Kairos", "desc": "Five months part-time for students who lead university AI-safety or policy groups: mentors, group funding, workshops. Stipend. Starts Dec 6; applications not yet open.", "deadline_short": "soon", "deadline_note": "not open", "tags": ["fellowship", "field-building", "undergrad ok"], "url": "pathfinder.kairos-project.org", "star": True},
                    {"name": "SPAR, Spring 2027", "org": "SPAR", "desc": "Remote, part-time research fellowship (3 months, 5–40 h/week). Explicitly open to undergraduates. Applications open around December; there is an interest form.", "deadline_short": "Dec", "deadline_note": "opens", "tags": ["research", "remote", "undergrad ok"], "url": "sparai.org", "star": True},
                    {"name": "Apart Research sprints", "org": "Apart", "short": "Apart sprint", "desc": "Free weekend hackathons with local sites: AI × Epistemics (Nov 13–15), Threat Intelligence (Dec 4–6), Agent Attribution (Dec 11–13). TAISI could host a Toronto site again.", "deadline": "2026-11-13", "deadline_short": "Nov 13", "deadline_note": "starts", "tags": ["hackathon", "free", "host?"], "url": "apartresearch.com/sprints", "star": True},
                    {"name": "AI Safety Camp 12 · PRISM · LASR Labs", "org": "various", "desc": "Online research programs from Jan 9 (AISC) and Jan 31 (PRISM); LASR’s paid London summer program (£15,000) has a sign-up list.", "deadline_short": "—", "deadline_note": "not open", "tags": ["research"], "url": "aisafety.camp · prism-research.org · lasrlabs.org"},
                ]},
                {"title": "Later, and always open", "items": [
                    {"name": "Oxford Technical AI Governance DPhil studentships", "org": "Oxford AIGI", "desc": "PhD funding starting Oct 2027 — for later.", "deadline": "2026-12-02", "deadline_short": "Dec 2", "deadline_note": "", "tags": ["PhD"], "url": "aigi.ox.ac.uk", "on_ruler": False},
                    {"name": "LawAI Summer Fellowships", "org": "Institute for Law & AI", "desc": "Two months from June 14, Washington or Cambridge; for law students and professionals.", "deadline": "2027-01-29", "deadline_short": "Jan 29", "deadline_note": "", "tags": ["law"], "url": "law-ai.org"},
                    {"name": "Funding for TAISI projects", "org": "rolling", "desc": "EA Infrastructure Fund ($1k–$500k), BlueDot Rapid grants (up to $20k), Coefficient Giving capacity-building fund, Lightcone Commons, Manifund.", "deadline_short": "rolling", "deadline_note": "", "tags": ["grants", "group-friendly"], "url": "funds.effectivealtruism.org · bluedot.org/grants"},
                ]},
            ], "note": "Recently closed, for the record: MATS Winter, Pivotal Q1, ERA Winter, Anthropic Fellows (Jan 2027) and Horizon 2027 (offers expected by end of November). Most dates come from aisafety.com’s listings and were checked on the program’s own page for GovAI, SPAR, Kairos, LASR and Apart; confirm before you apply."},
         ]},
        {"id": "world", "title": "The World", "aside": "Three countries, slowly",
         "blocks": [
            {"type": "region", "region": "indonesia", "kicker": "Region one", "title": "Indonesia",
             "map_points": [{"lon": 106.85, "lat": -6.2, "label": "Jakarta"}, {"lon": 114.6, "lat": -3.0, "label": "Barito Kuala"}],
             "stories": [
                {"headline": "A 313-article employment law is now public", "body": "Manpower Minister Yassierli said on Monday that Law No. 27 of 2026 on Employment Protection can be read through the State Secretariat’s legal-documents network. Its 23 chapters cover equal opportunity, training, informal-sector work, foreign workers, wages, dismissal and labour inspection. Parliament and the government approved it on Oct 6; President Prabowo signed it on Oct 28 and it took effect immediately. Rules under the 2003 Manpower Law and the 2023 Job Creation Law stay in force where they don’t conflict.", "why": "It resets the national framework for workers’ rights.", "outlet": "ANTARA", "date": "Nov 9", "url": "en.antaranews.com/news/441251"},
                {"headline": "Wildfire air operations under review after two helicopter crashes", "body": "A Super Puma helicopter fighting fires crashed in Barito Kuala, South Kalimantan, on Sunday; an Indonesian crew member died and two crew from Australia and New Zealand survived. An army Mi-17 crashed on a wildfire mission in Central Kalimantan earlier in the week. The disaster agency, BNPB, is now reviewing fleet readiness, water-bombing procedures, crew fitness and conditions, while ground firefighting continues.", "why": "Water-bombing from the air is central to Borneo’s fire response.", "outlet": "ANTARA", "date": "Nov 9", "url": "en.antaranews.com/news/441315"},
                {"headline": "Three laws stand between Indonesia and the OECD", "body": "Coordinating Economic Minister Airlangga Hartarto said the government aims to finish three pieces of legislation in 2027: rules on bribing foreign officials, a new Statistics Law and a revised Business Competition Law (the current one dates from 1999). Reviews are complete in 20 of 24 sectors; health still needs work. Full membership is targeted for 2028, and OECD Secretary-General Mathias Cormann visits on Nov 25.", "why": "Joining means rewriting parts of the country’s economic rulebook.", "outlet": "ANTARA", "date": "Nov 9", "url": "en.antaranews.com/news/441331"},
             ]},
            {"type": "region", "region": "canada", "kicker": "Region two", "title": "Canada",
             "map_points": [{"lon": -75.7, "lat": 45.42, "label": "Ottawa"}, {"lon": -122.85, "lat": 49.19, "label": "Surrey", "anchor": "start"}, {"lon": -106.67, "lat": 52.13, "label": "Saskatoon"}],
             "stories": [
                {"headline": "The budget is silent on foreign aid, a first since 2010", "body": "The federal budget tabled on Nov 5 does not mention international assistance or development — the first budget in more than 15 years not to, by The Canadian Press’s count. Aid groups assume last year’s plan to cut $2.7 billion over four years still stands and were relieved there were no new cuts. Foreign Affairs Minister Anita Anand says a foreign-policy update is coming “in a matter of weeks”.", "views": "Co-operation Canada calls the budget “largely silent” on development; the ONE Campaign wants $5.5 billion a year; the government says development remains a priority.", "why": "It shows where Ottawa is putting its money: at home.", "outlet": "The Canadian Press via Global News", "date": "Nov 7", "url": "globalnews.ca/news/12141139"},
                {"headline": "Saskatchewan’s premier: “best budget in a decade”", "body": "Scott Moe praised the budget in Saskatoon on Friday — “but that isn’t saying much” — pointing to a new exemption of up to $15 million in capital gains on eligible Canadian investments and a ten-year plan to end homelessness. He wanted more for municipal infrastructure. The province expects a new up-front write-off to cost it about $400 million a year.", "why": "Provincial reactions shape what the budget becomes in practice.", "outlet": "Global News", "date": "Nov 7", "url": "globalnews.ca/news/12139915"},
                {"headline": "A second storm on the B.C. coast; a third is forecast", "body": "Successive storms hit the South Coast and Vancouver Island on Nov 7–8. A falling tree trapped two vehicles in Surrey and one driver died. BC Hydro has counted more than 380,000 outages since Friday and restored about 317,000. Environment Canada expects a third storm on Monday with prolonged rain.", "why": "Repeated storms are testing the coast’s power grid.", "outlet": "Global News", "date": "Nov 8", "url": "globalnews.ca/news/12141788"},
             ]},
            {"type": "region", "region": "usa", "kicker": "Region three", "title": "United States",
             "map_points": [{"lon": -77.04, "lat": 38.9, "label": "Washington"}, {"lon": -111.1, "lat": 37.1, "label": "Lake Powell"}],
             "stories": [
                {"headline": "After the midterms, the question is prices", "body": "In AP’s reading, voters on Nov 3 told the new Democratic House majority and President Trump that inflation comes first. Consumer prices are up 3.7% on a year ago; the latest report showed 165,000 jobs added and unemployment at 4.1%. The deficit runs about $2 trillion a year and interest on the debt now exceeds $1 trillion — more than defence spending. Trump says he will work with Democrats on some things and veto what he sees as harmful.", "views": "Trump expects fuel prices to fall when the Iran war ends; budget analysts such as Marc Goldwein say rising rates and deficits are the core problem.", "why": "It sets the agenda for the next Congress.", "outlet": "AP via PBS NewsHour", "date": "Nov 8", "url": "pbs.org/newshour (voters demanded economic relief)"},
                {"headline": "Floods give the dry Southwest a rare reprieve", "body": "Late-October storms flooded parts of the Southwest and raised Lake Powell more than 20 feet from its September low — though it is still only a little over a quarter full. Flagstaff’s Upper Lake Mary took in more than 3 billion gallons. Water managers won’t change releases before the spring snowpack; a federal plan to cut Lower Basin use is being challenged in court by Nevada and Arizona.", "why": "A wet month buys time; it doesn’t end the drought.", "outlet": "AP via PBS NewsHour", "date": "Nov 8", "url": "pbs.org/newshour (Lake Powell rises 20 feet)"},
             ]},
            {"type": "region", "kicker": "Not about AI", "title": "Elsewhere & science",
             "stories": [
                {"headline": "A mock Mars crew steps outside after a year", "body": "Four people left a 158-square-metre, 3D-printed habitat at NASA’s Johnson Space Center on Oct 31 after just over a year of simulated Mars life: growing crops, doing geology, “Marswalks”, and messages delayed 13 to 22 minutes, plus a planned two-week blackout. NASA will use the results to plan crewed missions, which it says could come in the early 2030s.", "why": "Isolation, not rockets, may be the hardest part of going to Mars.", "outlet": "Nature", "date": "Nov 9", "url": "nature.com/articles/d41586-026-03588-w"},
                {"headline": "How semaglutide may protect kidneys", "body": "Kidney biopsies from 106 people with diabetic kidney disease, taken before and after treatment, showed better blood flow, less scarring and softer vessels with semaglutide (the drug in Ozempic) than with a placebo. A 2024 trial had already found fewer kidney failures; this smaller study suggests why.", "why": "It points to a direct effect, beyond weight and blood sugar.", "outlet": "Science News", "date": "Nov 9", "url": "sciencenews.org (semaglutide, kidney disease)"},
             ]},
            {"type": "box", "style": "tint", "label": "Bubble check", "paras": [
                "About half of the essays that reached your inbox since Friday were about AI (Zvi, Import AI, Forethought, Bentham’s Bulldog twice, Torchbearer, ControlAI, Decker, the Sentinel roundup). None of today’s eleven news stories is. If you read one non-AI thing this week, the Astral Codex Ten review of Walter Ong’s Orality and Literacy — on how writing changed the way people think — is waiting in your inbox, and is a good candidate for a full printing on a lighter day.",
            ]},
         ]},
        {"id": "essay", "title": "The Essay", "aside": "Printed whole, as the author wrote it",
         "blocks": [
            {"type": "essay", "essay_id": "1a1bb1c55bd40fe7", "kicker": "Homo Economicus · Nov 8",
             "title": "The Least of All Freedoms", "author": "Nicholas Decker", "publication": "Homo Economicus (Substack)",
             "dek": "On human disempowerment — an argument for handing decisions to more intelligent machines.",
             "paras": DECKER, "source_note": "nicholasdecker.substack.com/p/the-least-of-all-freedoms · reprinted from your subscription email",
             "counterpoint": [
                 "This is opinion, not reporting, and note its last line: the post is sponsored by Mechanize, a startup whose business is automating work. That doesn’t make the argument wrong, but it’s worth holding in mind.",
                 "The strongest replies go roughly like this. First, error correction: Karl Popper argued that democracy’s value is not that it picks good rulers, but that it lets you remove bad ones without bloodshed. A judge you cannot remove loses that, however wise. Second, the argument assumes the machine’s idea of “wiser” matches ours — which is the alignment problem itself, and a handover may not be reversible if it’s wrong. Third, courts work as Decker says partly because they can be overruled — by amendments and appointments — so the analogy cuts both ways.",
                 "A question to carry today, given the Post-AGI session at 1:30: what would you need to see before trusting a judge you could never remove?",
             ]},
         ]},
        {"id": "stand", "new_page": False, "title": "The Newsstand", "aside": "Everything else that arrived, in a line or two",
         "blocks": [
            {"type": "newsstand", "items": [
                {"essay_id": "1a1bb1c55bd40fe7", "pub": "Homo Economicus", "title": "The Least of All Freedoms", "mode": "in full", "summary": "Printed on the previous pages."},
                {"essay_id": "1a1c163db54ba802", "pub": "Forethought", "title": "Two Kinds of Test-Time Scaling", "mode": "summary", "summary": "Some models keep improving with more thinking far past the most compute they used per task in training — “compute extrapolation”. The author argues it probably began around late 2025 through context compaction, speeds up the most impressive capabilities, makes dangerous-capability evaluations open-ended (you can only rule out danger below a spending budget), and moves races to inference spending. The evidence is admittedly circumstantial. About 3,800 words; a candidate for full printing."},
                {"essay_id": "1a1b7deb2c081195", "pub": "Noahpinion", "title": "Why I’m becoming a China bear", "mode": "summary", "summary": "A long-time China bull turns bearish on Chinese hegemony: the subsidised manufacturing push is meeting saturated export markets and weak domestic demand after the property bust; infrastructure building has plateaued; Xi is turning inward. The main argument, about AI, sits behind the paywall."},
                {"essay_id": "1a1c0c7407f83360", "pub": "Don’t Worry About the Vase", "title": "AI R&D Is Accelerating Towards Potential RSI in 2027", "mode": "blurb", "summary": "Zvi on METR’s report about how much AI is speeding up AI research at Anthropic, and how close that brings recursive self-improvement."},
                {"essay_id": "1a1c1d7ea4b49307", "pub": "Sentinel Global Risks Watch", "title": "Weekly risks roundup", "mode": "blurb", "summary": "Anthropic and METR warnings of faster AI progress, and the US midterms."},
                {"essay_id": "1a1c08693dc9291f", "pub": "Import AI 480", "title": "Self-sustaining space economies; AI for science", "mode": "blurb", "summary": "Jack Clark’s weekly research digest, opening on when we’ll have robots on the Moon."},
                {"essay_id": "1a1c03f311b75abb", "pub": "ChinAI #381", "title": "China’s venture capital market is defying common sense", "mode": "blurb", "summary": "A translated, sobering take from a long-time observer of Chinese VC."},
                {"essay_id": "1a1bfff966d27820", "pub": "Slow Boring", "title": "The rise of the Hispanic moderate", "mode": "blurb", "summary": "Matthew Yglesias argues new leadership could let a new political majority emerge."},
                {"essay_id": "1a1bd77f3e6cfc5b", "pub": "Persuasion", "title": "The Midterms Just Made the World More Dangerous", "mode": "blurb", "summary": "Francis Fukuyama: Trump’s repudiation tells Xi, Putin and Kim their window to act is closing. Opinion."},
                {"essay_id": "1a1c0d360df73dd5", "pub": "Persuasion", "title": "The True Believer", "mode": "blurb", "summary": "A profile of the loyalist who becomes the president’s most powerful aide."},
                {"essay_id": "1a1b2c85152553f5", "pub": "Astral Codex Ten", "title": "Your Book Review: Orality and Literacy", "mode": "saved", "summary": "Contest finalist #15, on Walter Ong’s book about how writing reshapes thought. Long; held for a lighter day."},
                {"essay_id": "1a1c1217386b5aa2", "pub": "Bentham’s Newsletter", "title": "The Scariest Recent AI Development", "mode": "blurb", "summary": "An argument that AGI might be imminent. (Also from him on Saturday: a defence of Dario Amodei against his critics.)"},
                {"essay_id": "1a1b7259af5586af", "pub": "Torchbearer Community", "title": "The advocacy gap in international AI verification", "mode": "blurb", "summary": "Why verification mechanisms for global AI agreements are both possible and politically feasible."},
                {"essay_id": "1a1c162ac8d53883", "pub": "Visual Capitalist", "title": "The world’s biggest economies vs. debt in 2026", "mode": "blurb", "summary": "The US leads on size; Sudan tops debt-to-GDP. A chart worth a look on screen."},
                {"essay_id": "1a1b5b2f462b6edc", "pub": "Yascha Mounk", "title": "Martin Wolf on democratic capitalism after Trump", "mode": "blurb", "summary": "A 76-minute conversation: can democracy recover from populism, is there an AI bubble, and could France spark the next euro crisis?"},
            ]},
         ]},
        {"id": "colophon", "in_index": False, "title": "About This Paper", "aside": "Issue zero is a proof",
         "blocks": [
            {"type": "colophon", "parts": [
                {"title": "How today’s issue was made", "paras": [
                    "Your Google Calendar; Gmail labels News, UofT, Quercus and Luma, plus unread mail outside them; all eleven channels you’ve joined in the TAISI Slack; ANTARA, The Canadian Press, Global News, CTV, AP via PBS NewsHour, Nature and Science News for the world pages; aisafety.com and the programs’ own pages for opportunities.",
                ]},
                {"title": "House rules", "paras": [
                    "Plain headlines, no “breaking”, no outrage words. Every story says why it matters, and contested ones show both sides. Opinion is labelled as opinion. Numbers come with context. The paper ends — that’s the point.",
                ]},
                {"title": "Not in this issue yet", "paras": [
                    "Todoist (needs connecting), Quercus and UofT mail (forwarding started yesterday), your other two Slack workspaces, Discord, Toronto event discovery on Luma, and photographs — those arrive with the cloud fetcher.",
                ]},
                {"title": "Printing", "paras": [
                    "Print print-booklet.pdf double-sided, flipping on the short edge. Fold the stack in half and the pages fall in order.",
                ]},
            ]},
         ]},
    ],
}

out = Path(__file__).with_name("issue.json")
out.write_text(json.dumps(issue, indent=1, ensure_ascii=False))
print(out)
