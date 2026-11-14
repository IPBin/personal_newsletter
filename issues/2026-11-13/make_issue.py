"""Issue No. 4 — Friday, November 13, 2026. Starts from yesterday's issue.json."""
import json, copy
from pathlib import Path
HERE = Path(__file__).parent
TMP = Path("/tmp/s")
d = json.load(open(HERE.parent / "2026-11-12" / "issue.json"))
AST = json.load(open(TMP / "asteriskmag.json")); ACX = json.load(open(TMP / "acx.json"))

d["date"] = "2026-11-13"; d["date_long"] = "Friday, November 13, 2026"; d["weekday"] = "Friday"
d["number"] = "4"; d["edition"] = "Morning edition"; d["weather_word"] = "Cold & cloudy"
d["weather"] = {"daily": [
 {"date": "2026-11-13", "day_of_week": "Friday", "high": 4, "low": 0, "precipitation_chance": 1, "precipitation_type": "", "summary": "cloudy"},
 {"date": "2026-11-14", "day_of_week": "Saturday", "high": 7, "low": 0, "precipitation_chance": 17, "precipitation_type": "rain", "summary": "cloudy, small chance of rain"},
 {"date": "2026-11-15", "day_of_week": "Sunday", "high": 7, "low": 4, "precipitation_chance": 2, "precipitation_type": "", "summary": "cloudy"},
 {"date": "2026-11-16", "day_of_week": "Monday", "high": 10, "low": 6, "precipitation_chance": 0, "precipitation_type": "", "summary": "mild"},
 {"date": "2026-11-17", "day_of_week": "Tuesday", "high": 12, "low": 5, "precipitation_chance": 0, "precipitation_type": "", "summary": "mild"}]}

f = d["front"]
f["image"]["caption"] = "The old road from Edo to Kyoto, drawn by Katsushika Hokusai around 1818. Today’s back page is the fourth stop on that road, Kanagawa."
f["lede"] = ["Nothing is on your calendar today. Expect cloud and about 4°. Two PHLB18 items are still late, and reading response 6 earns nothing after Monday. The BlueDot course closes Sunday and the CLR program closes Monday."]
f["today"] = [
 {"time": "All day", "what": "Nothing on your calendar", "where": "A free day to catch up"},
 {"time": "Today", "what": "Apart’s AI × Epistemics sprint starts", "where": "Online · see Opportunities", "dim": True}]
f["todos"] = [
 {"topic": "Academics", "items": [
   {"text": "PHLB18 reading response 6 is late. It earns half marks until Mon Nov 16, then nothing.", "src": "Todoist", "urgent": True},
   {"text": "PHLB18 Scaffolding 2 is late. It loses 20% for every 3 days. It stays open to Dec 8.", "src": "Todoist"},
   {"text": "Todoist still lists the MGEA01 Chapter 11 quiz and GGRA30 Practical 7 as overdue. Check if they are done. Only your best 6 of 9 practicals count.", "src": "Todoist · QUERCUS_CONTEXT"},
   {"text": "COPB50 informational interview: due Sunday.", "src": "Todoist"},
   {"text": "ENGA10: a 500-word discussion on The Last Laugh earns one extra point on the final.", "src": "Quercus"}]},
 {"topic": "TAISI", "items": [
   {"text": "Upload your receipts to HCB, if you haven’t.", "src": "#taisi-team"},
   {"text": "Shivam’s cohort, Mon Nov 16: order the kosher meal.", "src": "Todoist"}]},
 {"topic": "Misc", "items": [
   {"text": "Read the UTSC Registrar’s check-in email (Nov 11).", "src": "UofT mail", "urgent": True}]}]
f["brief"] = [{"where": "Essays", "text": "How we came to talk about our lives like video games; should AI workers unionize?"},
              {"where": "World", "text": "Indonesia picks a new vice president on Dec 2; fires in Kalimantan; Ethiopia’s Tigray."}]

S = {s["id"]: s for s in d["sections"]}
desk = S["desk"]["blocks"]
desk[0]["items"] = [
 {"what": "Monday is the last day for PHLB18 reading response 6.", "detail": "It earns half marks until Nov 16, then is not accepted. Scaffolding 2 loses 20% for every 3 days it is late, so handing it in soon costs less. It closes Dec 8.", "src": "Todoist · QUERCUS_CONTEXT"},
 {"what": "Two course windows close this weekend.", "detail": "BlueDot’s Frontier AI Governance course: apply by Nov 15. CLR’s Fundamentals Program closes Monday, Nov 16 at 11:59 pm GMT. Both pages were checked today.", "src": "bluedot.org · longtermrisk.org"},
 {"what": "Check two quizzes in Todoist.", "detail": "The MGEA01 Chapter 11 quiz (due Thursday 7 pm) and GGRA30 Practical 7 (closed Wednesday) still show as overdue there. They may just need ticking off.", "src": "Todoist"}]
desk[1]["items"] = [
 {"time": "Fri", "what": "Apart epistemics sprint starts. AI Safety Camp posts its project list (the site says Nov 14).", "where": "online · see Opportunities"},
 {"time": "Sat", "what": "Marches for an AI treaty", "where": "cities in the US, Canada and France · noted in Astral Codex Ten", "dim": True},
 {"time": "Sun", "what": "COPB50 informational interview due; BlueDot closes", "where": "Nov 15"},
 {"time": "Mon", "what": "PHLB18 lecture 10–12 (IA 2150) and tutorial 1–2 (HW 402); reading response due; CLR closes; Shivam’s cohort food", "where": "Nov 16"},
 {"time": "Wed", "what": "GGRA30 lecture 11–1 (HL B101); ENGA10 lecture 1–3 (AC 223), film: Modern Times; GGRA30 practical 4–5 (BV 469); Practical 8 quiz", "where": "Nov 18"},
 {"time": "Thu", "what": "MGEA01 lecture", "where": "7:00–10:00 pm · IC 130 · Nov 19"}]
desk[2]["items"] = [
 {"when": "Fri Nov 27", "time": "5:30–7:30 pm", "name": "After AGI: What Might a Good Outcome for Humanity Look Like?", "detail": "Jackman Humanities Building, Toronto. Hosted by TAISI. You registered yesterday.", "status": "registered"}]
desk[3]["title"] = "TAISI Slack · since Thursday"
desk[3]["channels"] = [
 {"name": "#colloquium", "points": ["Pera K asked to meet before 7 or at 11. Joseph Kostousov and Ayushman Gupta both said 11 works. The day is not clear from the messages, so check the channel."]},
 {"name": "Other channels", "points": ["No other new messages found."]}]

o = S["opps"]["blocks"][0]
o["intro"] = "Picked for a second-year CS and Public Policy student on TAISI’s operations team. ★ = strong fit. Each item says why. Today I re-checked the BlueDot, CLR and AI Safety Camp pages. The rest were last checked Nov 9."
for g in o["groups"]:
    for it in g["items"]:
        if it["name"].startswith("Apart: AI × Epistemics"): it["deadline_note"] = "starts today"
        if it["name"].startswith("Frontier AI Governance"): it["deadline_note"] = "Sun; closes in 2 days"
        if it["name"].startswith("AI Safety Camp"): it["desc"] = it["desc"].replace("The project list goes up Nov 13, when team applications open.", "The project list goes up about Nov 13–14, when team applications open.")
        if it["name"].startswith("AI Safety Camp"): it["deadline_note"] = "Sun Nov 29; team applications open about Nov 13–14"

W = S["world"]["blocks"]
ind, can, usa, wd, sci, bub = W[0], W[1], W[3], W[4], W[5], W[6]
for r in (ind, can, usa, wd, sci): r.pop("chart", None)

ind["blurb"] = "A date for the new vice president, fires in Kalimantan, and a budget deficit by design."
ind["stories"] = [
 {"tag": "Politics", "headline": "Indonesia will choose a new vice president on December 2", "lead": True,
  "paras": ["The People’s Consultative Assembly (MPR), which holds the vote, will meet on Wednesday, December 2 to elect and swear in a successor to Gibran Rakabuming Raka. He resigned on Thursday. Speaker Ahmad Muzani said the law gives the MPR 60 days.",
            "President Prabowo must name two candidates within 14 days of the MPR’s request. By law they must come from the parties that backed the winning ticket in 2024. A minister said the president has full authority to pick the two."],
  "why": "Until then, the president holds the top two jobs’ powers alone.", "outlet": "ANTARA", "date": "Nov 13", "url": "https://en.antaranews.com/news/442383/indonesias-mpr-to-elect-new-vice-president-on-december-2"},
 {"tag": "Fires", "headline": "Forest fires fall in most places but rise in East Kalimantan and East Nusa Tenggara", "paras": ["The national disaster agency counts 283 hotspots covering 764 hectares. Hotspots in South Papua fell 84% from the day before. In East Kalimantan they rose 77%, and the burning area in East Nusa Tenggara rose 21%."],
  "why": "Smoke from fires harms health far from where they burn.", "outlet": "ANTARA", "date": "Nov 13", "url": "https://en.antaranews.com/news/442427/fires-decline-in-most-regions-e-kalimantan-and-ntt-remain-concerns"},
 {"tag": "Budget", "headline": "The finance ministry says a budget deficit is planned, not a loss", "paras": ["A ministry official said the state budget is “designed to run a deficit,” because spending is meant to be higher than income. Through October the deficit was 1.47% of GDP. The plan for the full year is 2.85%.",
            "Income was Rp2,618 trillion (about US$143.7 billion), up 23.9% from a year ago. Spending was Rp2,997 trillion (about US$164.5 billion), up 15.6%."],
  "why": "The words matter: a planned deficit is borrowing the government chose.", "outlet": "ANTARA", "date": "Nov 13", "url": "https://en.antaranews.com/news/442375/finance-ministry-says-state-budget-deficit-is-planned-not-a-loss"},
 {"tag": "Energy", "headline": "Indonesia checks if it has enough palm oil for its B50 fuel plan", "paras": ["B50 is the next step after B35 and B40: diesel mixed with more palm-oil fuel. Officials say it would cut diesel imports and ease the cost of fuel subsidies. They are studying whether there will be enough palm oil in 2027.",],
  "views": "An economist, Achmad Nur Hidayat, ran a model for 2027–2030. It showed diesel imports falling by up to 46.8 million kiloliters. But palm oil exports could drop, and the export fee that pays for the fuel support might run short. He suggests a blend level that can change with prices.",
  "why": "The same palm oil feeds cars, exports and food.", "outlet": "ANTARA", "date": "Nov 13", "url": "https://en.antaranews.com/news/442359/government-studies-raw-material-sufficiency-for-b50-in-2027"}]
IDN = {"type": "numbers", "title": "Indonesia’s budget, through October", "items": [{"n": "1.47%", "label": "deficit so far, of GDP"}, {"n": "2.85%", "label": "planned for the year"}, {"n": "+23.9%", "label": "income vs last year"}], "source": "Finance Ministry, via ANTARA, Nov 13"}

can["blurb"] = "Student loans stop at career colleges, a PhD first, and venison for food banks."
can["stories"] = [
 {"tag": "Education", "headline": "A career college lays off staff as Ontario freezes student loans", "lead": True,
  "paras": ["Ontario has barred students at all 242 private career colleges from OSAP loans while it investigates fraud. The ban began with five colleges in July and grew in October. Computek College in Toronto, Ajax and Markham says its income stopped. It made layoffs on Monday for the first time in 35 years.",
            "On Thursday, Minister Nolan Quinn said a bill will be introduced Monday to add oversight. He said the problems are “far more widespread than first suspected.”"],
  "views": "Computek’s chairman says the school is audited each year and supports a crackdown, but wants to be inspected first so students can return. The government says it found “coordinated, sophisticated” efforts to take advantage of students and taxpayers.",
  "why": "Students who relied on loans now struggle to pay rent and food.", "outlet": "Global News", "date": "Nov 13", "url": "https://globalnews.ca/news/12148797/ontario-career-college-funding-stalls/"},
 {"tag": "Languages", "headline": "A 73-year-old teacher is the first graduate of McGill’s Indigenous languages PhD", "paras": ["Mary Onwá Tekahawáhkwen Macdonald, from the Mohawk community of Akwesasne, finished in three years. The usual time is five. She taught the Mohawk language, Kanyen’kéha, for 45 years before she retired at 70 to study.", "The program began in 2023 for people who speak an Indigenous language that is at risk. She hopes to stay at McGill as an elder in residence."],
  "why": "Languages survive when people are trained to teach them.", "outlet": "Global News", "date": "Nov 13", "url": "https://globalnews.ca/news/12149031/elder-first-graduate-mcgill-indigenous-languages-phd-program/"},
 {"tag": "Food", "headline": "Nova Scotia gives $30,000 so Truro’s deer cull can feed food banks", "paras": ["The one-time grant pays to process meat from Truro’s yearly deer cull at a licensed facility. It then goes to food banks across the province through Feed Nova Scotia. The 2026 hunt is expected to give about 1,200 kg, or roughly 12,000 meals.", "The Hunters Helping the Hungry program has given wild game to food banks for more than 20 years."],
  "why": "A cull that already happens now also feeds people.", "outlet": "Global News", "date": "Nov 12", "url": "https://globalnews.ca/news/12147809/hunters-helping-the-hungry-truro-deer-cull/"}]

usa["blurb"] = "Insulin caps in red states, a plan to shrink food aid, and who voted in the South."
usa["stories"] = [
 {"tag": "Health", "headline": "Twenty-nine states now cap what patients pay for insulin", "lead": True,
  "paras": ["North Dakota, a Republican-led state, limits insulin to $25 a month for state-regulated plans. About a fifth of the roughly 40 million Americans with diabetes use insulin. Average yearly out-of-pocket costs for people with private insurance went from $470 in 2018 to $220 in 2025.",
            "Colorado began in 2019. In 2022, a federal law capped insulin at $35 a month for Medicare. An attempt to extend that to private insurance failed in Congress after Republican opposition."],
  "why": "A rare issue where both parties agreed the market was not working.", "outlet": "NPR (KFF Health News)", "date": "Nov 13", "url": "https://www.npr.org/2026/11/13/nx-s1-6032717/diabetes-insurance-insulin-price"},
 {"tag": "Food aid", "headline": "A proposed rule could cut about 6.3 million people from SNAP", "paras": ["The Agriculture Department wants to stop some people who get benefits from the TANF program from qualifying for SNAP, the food aid program, automatically. It estimates 6.3 million people could lose eligibility by 2029. About 5.5 million have already lost benefits in the past year.",
            "The public can comment until next month. If approved, the rule would take full effect in about two years."],
  "views": "The administration says it is closing a loophole. A former Agriculture official, Stacy Dean, says it would remove many working-poor people. A left-leaning research group says the move ignores voters’ wish for lower costs.",
  "why": "Being on SNAP also helps children get free school meals.", "outlet": "PBS NewsHour (AP)", "date": "Nov 12", "url": "https://www.pbs.org/newshour/politics/trump-administration-plans-to-make-it-harder-to-get-grocery-assistance"},
 {"tag": "Elections", "headline": "Who showed up explains Democrats’ wins in the South, NPR finds", "paras": ["In six southern states, turnout fell 19% from 2024 in counties Kamala Harris won. It fell 26% in counties Donald Trump won. Those six states swung 22 points toward Democrats, compared with 14.5 points nationwide.",
            "In Mississippi, Democrat Scott Colom is ahead by just over 5,600 votes as final ballots are counted."],
  "why": "Small shifts in who votes can flip close races.", "outlet": "NPR", "date": "Nov 13", "url": "https://www.npr.org/2026/11/13/nx-s1-6038701/midterm-election-voter-turnout-south"}]
TURN = {"type": "numbers", "title": "Turnout drop vs 2024, six southern states", "items": [{"n": "−19%", "label": "counties Harris won"}, {"n": "−26%", "label": "counties Trump won"}, {"n": "22 pts", "label": "swing to Democrats (US: 14.5)"}], "source": "NPR analysis, Nov 13"}

wd["blurb"] = "Talks on Ukraine, a hacking scheme, Ethiopia’s Tigray, and the Pope in Peru."
wd["stories"] = [
 {"tag": "War", "headline": "US envoys say Europe will join the next round of Ukraine peace talks", "paras": ["Jared Kushner and Steve Witkoff, envoys of the US, met Russia’s Vladimir Putin in Moscow and then Ukraine’s Volodymyr Zelensky in Dublin on Thursday. Kushner said Putin is “willing to give it a try” on having EU delegates at the table. Zelensky welcomed it.",
            "Putin said Russia’s demand for territory has not changed. Both sides did agree to another prisoner swap, the largest yet."],
  "why": "Past talks in Abu Dhabi ended with no breakthrough.", "outlet": "BBC", "date": "Nov 13", "url": "https://www.bbc.co.uk/news/articles/ckn80j9jv3jxo"},
 {"tag": "Ethiopia", "headline": "In Tigray, it is neither war nor peace", "paras": ["Fighting began in late September between the TPLF, which ran Tigray for decades, and Ethiopia’s army. Federal forces took the capital, Mekelle, in under two weeks. Hundreds of people are reported to have died.",
            "Officials say the war is over. Residents describe no work and fear about what comes next."],
  "why": "A 2022 peace deal ended an earlier two-year war here.", "outlet": "BBC", "date": "Nov 13", "url": "https://www.bbc.co.uk/news/articles/cm3egjgvp794o"},
 {"tag": "Crime", "headline": "The FBI says North Korean hackers used fake video calls to steal $400 million", "paras": ["The scheme, called FaceStealer, hit more than 900 people in 18 months, mostly in crypto work. Hackers invite targets to a fake meeting, play clips of past victims, then ask them to “fix” the audio with a link that installs malware.",
            "The FBI says the money funds North Korea’s weapons program."],
  "why": "Even careful people can be fooled by a call that looks real.", "outlet": "BBC", "date": "Nov 13", "url": "https://www.bbc.co.uk/news/articles/cqdj1ellpd70o"},
 {"tag": "Peru", "headline": "Pope Leo calls for an end to “machismo” in Peru", "paras": ["Pope Leo XIV, who is Peruvian, spoke in Lima on Thursday. He demanded that women be protected and respected, and told bishops to answer victims of clergy abuse with truth and justice. About 40,000 people sang with him in Plaza Mayor.",
            "He had lung cancer surgery last month. He climbed stairs quickly and joked about people who doubted he would come."],
  "why": "A pope speaking in his home country, about women’s safety.", "outlet": "PBS NewsHour (AP)", "date": "Nov 12", "url": "https://www.pbs.org/newshour/world/after-emotional-return-pope-leo-denounces-machismo-in-peru-and-demands-respect-for-women"}]

sci["blurb"] = "How phone data traced Ebola, and a space mission to twin asteroids."
sci["stories"] = [
 {"tag": "Health", "headline": "Phone data show how Ebola spread for weeks before it was found", "lead": True,
  "paras": ["Researchers used anonymous phone data and test records to map the start of the Bundibugyo Ebola outbreak in Congo. The first confirmed case, found May 15, had symptoms by April 25.",
            "There are now more than 10,000 confirmed cases and 5,198 deaths."],
  "why": "Finding a disease early is the best way to stop it.", "outlet": "Nature", "date": "Nov 12", "url": "https://www.nature.com/articles/d41586-026-03666-z"},
 {"tag": "Space", "headline": "Europe’s Hera spacecraft reaches a pair of asteroids", "paras": ["On Nov 4, Hera came within 30 km of Didymos and its small moon Dimorphos, after more than two years of travel. It is the first time scientists study two asteroids that travel together. In 2022 NASA crashed a spacecraft into Dimorphos, which shortened its orbit by more than half an hour."],
  "why": "It tests how we might push away a dangerous asteroid.", "outlet": "Science News", "date": "Nov 12", "url": "https://www.sciencenews.org/article/europe-hera-mission-double-asteroid"}]
drop = {"Indonesia checks if it has enough palm oil for its B50 fuel plan","Pope Leo calls for an end to “machismo” in Peru","Nova Scotia gives $30,000 so Truro’s deer cull can feed food banks"}
for r in (ind, can, wd): r["stories"] = [x for x in r["stories"] if x["headline"] not in drop]
wd["blurb"] = "Talks on Ukraine, a hacking scheme, and Ethiopia’s Tigray."
can["blurb"] = "Student loans stop at career colleges, and a PhD first."
usa["stories"] = usa["stories"][:2]
usa["blurb"] = "Insulin caps in red states, and a plan to shrink food aid."
sci["stories"] = sci["stories"][:1]
sci["blurb"] = "How phone data traced Ebola."
W[:] = [ind, can, usa, wd, sci, bub]
bub["paras"] = ["Of 12 newsletters since yesterday, 5 were about AI. No news story today is."]

# ---------------- essays
E = S["essays"]["blocks"]
base = copy.deepcopy(E[0])
ap = [x.replace("alleged 2 30","alleged 230").replace(" 1 But more"," But more") for x in AST["paras"][2:38]]
ast = dict(base); ast.update({"essay_id": "asterisk-playable-characters", "optional": False, "priority": 9, "new_page": False,
  "kicker": "Asterisk · Nov 12 · Essay", "title": "We are all playable characters", "author": "Hannah Kim", "publication": "Asterisk",
  "dek": "A philosopher asks why we now talk about our lives with game words like “side quest” and “NPC,” and what is lost and gained.",
  "paras": ap, "source_note": "asteriskmag.substack.com/p/we-are-all-playable-characters · from Asterisk Issue 16 · a subscribe line, the author line and one footnote are left out",
  "counter_label": "In plain words, and the other side",
  "counterpoint": ["The short version: People used to see their lives as a story: one thing leads to the next, and the meaning shows up at the end. Now many people use game ideas instead: quests, levels, roles. Kim says character types like “girlboss” are easy to try on and give clear next steps. But they also tell you what counts as success, and that may shrink who we are.",
                   "The other side. This is one philosopher’s view, and it builds on other thinkers like C. Thi Nguyen. She ends unsure whether this is an upgrade or a downgrade. A reader might say game words are just slang, like old terms for types of people, and do not change how anyone lives. Or that stories and games can work together."]})
acp = [p.replace(" 4 5"," ") for i, p in enumerate(ACX["paras"]) if i not in (0, 17) and i < 23]
acx = dict(base); acx.update({"essay_id": "acx-ai-employee-union", "optional": False, "priority": 7, "new_page": False,
  "kicker": "Astral Codex Ten · Nov 12 · Opinion", "title": "AI company employees should unionize", "author": "Scott Alexander", "publication": "Astral Codex Ten",
  "dek": "A blogger says safety-minded workers at AI companies could organize, and explains how the law could help.",
  "paras": acp, "source_note": "astralcodexten.com/p/ai-company-employees-should-unionize · the section numbers and the footnotes at the end are left out",
  "counterpoint": ["The short version: Scott Alexander says people at AI companies who worry about safety should not only quit or blow the whistle. They can band together, even without a formal union. Because skilled AI researchers are so rare, a small group threatening to walk could win real talks about safety. He points to a legal group, Psst, for those who want to speak out, and says to act soon.",
                   "The other side. He writes as a supporter of AI safety, and his case rests on guesses about how hard it is to replace these workers and about how fast AI will advance. He admits some safety actions may not be protected by law. Others may say a union would slow useful work, or that companies would respond by hiring different people. Several claims come from his contacts, not from public records."]})
S["essays"]["blocks"] = [ast, acx] + [b for b in E[2:] if b["type"] == "box"]

ns = S["stand"]["blocks"][0]
ns["items"] = [
 {"essay_id": "asterisk-playable-characters", "pub": "Asterisk", "author": "Hannah Kim", "title": "We are all playable characters", "mode": "in full", "summary": "Printed in full in the Essays.", "hide_if_full": True,
  "fallback": ["Essay. A philosopher says people now describe their lives with game words, such as quests and NPCs, instead of as one story. Character types are easy to try on, but they may also define success for us."]},
 {"essay_id": "acx-ai-employee-union", "pub": "Astral Codex Ten", "author": "Scott Alexander", "title": "AI company employees should unionize", "mode": "in full", "summary": "Printed in full in the Essays.", "hide_if_full": True,
  "fallback": ["Opinion. The writer says safety-minded AI workers could organize, with or without a formal union, and that their rare skills give them power. Keep in mind: several claims come from his contacts."]},
 {"essay_id": "persuasion-double-down", "pub": "Persuasion", "author": "Andrew Piper", "title": "Double Down on College", "mode": "summary",
  "paras": ["Opinion, from Wednesday; only the free part is public. The writer asked an AI tool to price a bare-bones humanities college with 120 students and eight professors paid $125,000 each. He got $20,389 per student a year. He says the numbers show that cutting everything but teaching does not make college cheap. Keep in mind: it is a rough model, and he says you can quibble with every number."]},
 {"essay_id": "newcritic-good-game", "pub": "The New Critic", "author": "Overlocked", "title": "Good Game, Well Played", "mode": "summary",
  "paras": ["Essay; only the start is free. A 27-year-old lawyer from Auckland, writing as “Overlocked,” says games are like art: they change what you notice. He writes about the esport League of Legends and about flying in to see a semifinal at the World Championship, where a star player’s team had been “cursed.”"]},
 {"essay_id": "slowboring-moderate", "pub": "Slow Boring", "author": "Matthew Yglesias", "title": "What a moderate looks like", "mode": "summary",
  "paras": ["Opinion; only the free part is public. Yglesias says calling Republican gerrymanders “dumb” is wrong. They are built to save seats in a mildly bad year, not a very bad one. He also answers a reader on whether Texas politician James Talarico is a moderate. Keep in mind: he is a centrist Democrat-leaning columnist."]}]

d["back"] = {"src": "assets/art/processed/back-04-kanagawa.png", "kicker": "The Road · Stop 4 of 55", "title": "Kanagawa · Hiroshige",
  "caption": "Kanagawa was the fourth town on the road from Edo. The picture shows a row of inns on a hillside above the bay, with travellers on the road and sailing boats on the water. Hiroshige made 55 prints of the road, and this paper shows one each issue. Turn the page sideways to see it the right way up.",
  "credit": "Public domain. Library of Congress, via Wikimedia Commons."}

d["email_notes"] = [
 "Issue No. 4, Friday Nov 13. Gmail, Calendar, Slack, Todoist and the network all worked. The Quercus calendar feed is not set up; school dates come from Todoist, Quercus mail and QUERCUS_CONTEXT.md.",
 "Weather: Open-Meteo for Fri to Tue.",
 "Opportunities: it is not Monday, so the list is carried over. I re-checked the BlueDot (apply by Nov 15), CLR (Mon Nov 16, 23:59 GMT) and AI Safety Camp pages today. AI Safety Camp says team applications open Nov 14 (it also calls that day Friday, but Nov 14 is a Saturday), so check the site. Nothing new reached the inbox or Slack.",
 "School: Todoist still shows the MGEA01 Chapter 11 quiz and GGRA30 Practical 7 as overdue, so I do not know if you did them. PHLB18 reading response 6 earns half marks until Nov 16. ENGA10 posted a new discussion (500 words on The Last Laugh for one extra point on the final), the Mrs Dalloway notes, and the film link for Modern Times (Lecture 9, Nov 18). ThriveUTSC asks for an artifact for the Nov 25 and 26 classes. The UTSC Registrar’s “Academic Probation Check-in” (Nov 11) is still worth reading; I did not copy details into the paper.",
 "Slack: only #colloquium had new messages (a meeting time of 11). A DM thread with Joseph Kostousov about a call was not read or printed.",
 "Essays: Hannah Kim (Asterisk) is printed in full (free). Scott Alexander is printed in full minus the footnotes. There was no room for a Newsstand today. Persuasion (Double Down on College), The New Critic and Slow Boring were paywalled, so I only had their free parts and left them out. Left out: Noahpinion’s podcast, the OWID Brief, ControlAI, AI Frontiers, Epoch’s Gradient Updates, Zvi, Bentham’s short notes, Visual Capitalist and the Rutger Bregman welcome emails.",
 "News: CBC was blocked, so Canada comes from Global News. I did not print the Microsoft outage because it was mostly about AI services, or the Jensen Huang story, which is AI-related. I read but cut for space: the Pope Leo in Peru story, the Hera asteroid story, the Truro deer-cull story, NPR on turnout in the South, ANTARA on the B50 fuel plan, ANTARA on palm-oil tracing before EU rules, BYD and local content, and the Somalia aid-cuts report.",
 "Art: Hiroshige’s Kanagawa. The Wikimedia copy was resized and lightly smoothed to keep the PDF small.",
]
d["credits"] = ["Front page band: Katsushika Hokusai, Famous Places on the Tōkaidō in One View (c. 1818). UBC Library, no known copyright restrictions.",
  "Back page: Utagawa Hiroshige, Kanagawa, from the Fifty-three Stations of the Tōkaidō. Library of Congress (LCCN 2008660614), public domain.",
  "Maps: Natural Earth data via world-atlas. Weather: Open-Meteo."]
ns["items"] = [x for x in ns["items"] if x["essay_id"] not in ("newcritic-good-game","slowboring-moderate","persuasion-double-down")]
(HERE / "issue.json").write_text(json.dumps(d, indent=1, ensure_ascii=False))
print("ok")
