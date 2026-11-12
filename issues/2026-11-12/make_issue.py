"""Issue No. 3 — Thursday, November 12, 2026. Starts from yesterday's issue.json and swaps in today's content."""
import json, copy
from pathlib import Path
HERE = Path(__file__).parent
TMP = Path("/tmp/claude-0/s")
d = json.load(open(HERE.parent / "2026-11-11" / "issue.json"))
YG = json.load(open(TMP / "yg.json")); BB = json.load(open(TMP / "bb.json"))

d["date"] = "2026-11-12"; d["date_long"] = "Thursday, November 12, 2026"; d["weekday"] = "Thursday"
d["number"] = "3"; d["edition"] = "Morning edition"; d["weather_word"] = "Drizzle, then cloudy"
d["weather"] = {"daily": [
 {"date": "2026-11-12", "day_of_week": "Thursday", "high": 7, "low": 3, "precipitation_chance": 54, "precipitation_type": "rain", "summary": "light rain"},
 {"date": "2026-11-13", "day_of_week": "Friday", "high": 4, "low": 0, "precipitation_chance": 18, "precipitation_type": "", "summary": "mostly cloudy"},
 {"date": "2026-11-14", "day_of_week": "Saturday", "high": 6, "low": 1, "precipitation_chance": 21, "precipitation_type": "", "summary": "mostly cloudy"},
 {"date": "2026-11-15", "day_of_week": "Sunday", "high": 8, "low": 5, "precipitation_chance": 1, "precipitation_type": "", "summary": "mostly cloudy"}]}

# ---------------- front
f = d["front"]
f["image"]["caption"] = "The old road from Edo to Kyoto, drawn by Katsushika Hokusai around 1818. Today’s back page is the third stop on that road, Kawasaki."
f["lede"] = ["Today is lighter at school. The MGEA01 Achieve quiz is due at 7 tonight, and the lecture runs from 7 to 10. The GGRA30 Practical 7 quiz closed last night. Expect drizzle and about 7° today. Two PHLB18 items are still late. Sign-ups for the BlueDot and CLR courses close this weekend."]
f["today"] = [
 {"time": "All day", "what": "Pay off the credit card", "where": "Your Todoist date"},
 {"time": "7:00 pm", "what": "MGEA01 Achieve quiz, Chapter 11, due", "where": "On Achieve"},
 {"time": "7:00", "what": "MGEA01 lecture", "where": "IC 130 · until 10:00"}]
f["todos"] = [
 {"topic": "Academics", "items": [
   {"text": "MGEA01 Achieve quiz, Chapter 11, is due tonight at 7.", "src": "Todoist", "urgent": True},
   {"text": "GGRA30 Practical 7 quiz closed last night. Only your best 6 of 9 practicals count.", "src": "Todoist · QUERCUS_CONTEXT"},
   {"text": "PHLB18 reading response 6 is late. It earns half marks until Nov 16, then nothing.", "src": "Todoist", "urgent": True},
   {"text": "PHLB18 Scaffolding 2 is late. It loses 20% for every 3 days. It stays open to Dec 8.", "src": "Todoist"},
   {"text": "COPB50 informational interview: due Sunday.", "src": "Todoist"}]},
 {"topic": "TAISI", "items": [
   {"text": "Upload your receipts to HCB, if you haven’t.", "src": "#taisi-team"},
   {"text": "Shivam’s cohort, Mon Nov 16: order the kosher meal too.", "src": "Todoist"}]},
 {"topic": "Misc", "items": [
   {"text": "Pay off the credit card today.", "src": "Todoist", "urgent": True},
   {"text": "Read the UTSC Registrar’s check-in email (Nov 11).", "src": "UofT mail"}]}]
f["brief"] = [{"where": "Essays", "text": "Why voters are so angry about prices; a new idea called “broadtermism”."},
              {"where": "World", "text": "Indonesia’s vice president resigns; Kyiv’s blackouts; a surprise in Mississippi."}]

S = {s["id"]: s for s in d["sections"]}
# ---------------- desk
desk = S["desk"]["blocks"]
desk[0]["items"] = [
 {"what": "Two school deadlines tonight.", "detail": "The MGEA01 Achieve quiz (Chapter 11) is due at 7 pm. The lecture starts at 7 in IC 130. The credit card payment is also due today in Todoist.", "src": "Todoist · QUERCUS_CONTEXT"},
 {"what": "Two PHLB18 items are late.", "detail": "Reading response 6 gets half marks until Nov 16, then is not accepted. Scaffolding 2 loses 20% for every 3 days it is late, so handing it in soon costs less. It closes Dec 8.", "src": "Todoist · QUERCUS_CONTEXT"},
 {"what": "Two course windows close this weekend.", "detail": "BlueDot’s governance course closes Sunday, Nov 15. CLR’s course closes Monday, Nov 16 at 11:59 pm GMT. Both are below.", "src": "bluedot.org · longtermrisk.org"}]
desk[1]["items"] = [
 {"time": "Thu", "what": "MGEA01 lecture, then Achieve quiz Ch. 11 due 7 pm", "where": "7:00–10:00 pm · IC 130"},
 {"time": "Fri", "what": "Apart epistemics sprint starts; AI Safety Camp project list goes up", "where": "online · see Opportunities"},
 {"time": "Sat", "what": "Marches for an AI treaty", "where": "cities in the US, Canada and France · noted in Astral Codex Ten", "dim": True},
 {"time": "Sun", "what": "COPB50 informational interview due; BlueDot closes. The International Development Conference’s online workshop was cancelled.", "where": "Nov 15"},
 {"time": "Mon", "what": "PHLB18 lecture 10–12 (IA 2150) and tutorial 1–2 (HW 402); reading response 7 due; CLR closes; Shivam’s cohort food", "where": "Nov 16"},
 {"time": "Wed", "what": "GGRA30 lecture 11–1 (HL B101); ENGA10 lecture 1–3 (AC 223); GGRA30 practical 4–5 (BV 469); Practical 8 quiz", "where": "Nov 18"}]
desk[2]["items"] = [
 {"when": "Nov 9–11", "time": "6 pm", "name": "The Hinton Lectures 2026.", "detail": "Paul Christiano, three evenings. Wednesday’s recording is now online, and so is Tuesday’s, from the organizers’ emails.", "status": "registered"}]
desk[3]["title"] = "TAISI Slack · since Wednesday"
desk[3]["channels"] = [
 {"name": "#taisi-team · ideas for TAISI", "points": ["Pera K sent a list of ideas late Wednesday night. One asks how TAISI can attract busy, high-skill people. Referrals through professors could feel less like a sales pitch. Another asks if TAISI has time to match people to opportunities one by one.", "Pera also said personal coaching helped them, and offered to help improve the branding and website before the end of the year."]},
 {"name": "#hackathons", "points": ["Caitlin Mah said a plan being discussed is close to a policy hackathon she ran last summer, and offered to advise."]},
 {"name": "Other channels", "points": ["No other new messages."]}]

# ---------------- opportunities (carried over; Monday is the day for full re-checks)
o = S["opps"]["blocks"][0]
o["intro"] = "Picked for a second-year CS and Public Policy student on TAISI’s operations team. ★ = strong fit. Each item says why. Most dates were last checked on each program’s own page on Nov 9. CLR’s date was checked again today."

# ---------------- world
W = S["world"]["blocks"]
ind, can, usa, wd, sci, bub = W[0], W[1], W[2], W[3], W[4], W[5]
for r in (ind, can, usa, wd, sci): r.pop("chart", None)

ind["blurb"] = "The vice president resigns, the rupiah slips, and a plan to find TB sooner."
ind["stories"] = [
 {"tag": "Politics", "headline": "Indonesia’s vice president resigns", "lead": True,
  "paras": ["Vice President Gibran Rakabuming Raka gave his resignation to parliament on Thursday. President Prabowo Subianto said he accepted it “with a heavy heart.” Lawmakers in the upper house now have 60 days to fill the job. They will choose from two people the president names.",
            "The Supreme Court had ruled that there was no proof Gibran finished senior high school, a rule for the job. More than 100 lawmakers had backed a move that could have led to impeachment. Impeachment is a vote to remove an official."],
  "views": "Gibran has said his university studies show he finished high school. Prabowo said school systems abroad differ from Indonesia’s. The BBC also reports a growing split between Prabowo and Gibran’s father, former president Joko Widodo.",
  "why": "Yesterday’s paper said the House was moving to impeach him. Now the president must pick a successor.",
  "outlet": "BBC", "date": "Nov 12", "url": "https://www.bbc.co.uk/news/articles/cmvgxgz87qqro"},
 {"tag": "Money", "headline": "A minister says the rupiah’s dip is not like 1998", "paras": ["A deputy economy minister, Dradjad Hari Wibowo, said the rupiah’s swings come from politics and are different from the 1998 Asian financial crisis. On Thursday morning the rupiah fell 0.27%, to Rp18,198 per US dollar.", "Bank Indonesia, the central bank, also points to expected US interest rate rises, a possible lower ranking for Indonesia’s stock market by MSCI, and year-end dollar buying."],
  "why": "A weaker rupiah makes imports and foreign debt cost more.", "outlet": "ANTARA", "date": "Nov 12", "url": "https://en.antaranews.com/news/442087/indonesia-says-rupiah-turbulence-unlike-1998-financial-crisis"},
 {"tag": "Health", "headline": "Indonesia is sending 5,600 TB testing machines to health centers", "paras": ["Deputy Health Minister Benjamin Paulus Octavianus said the machines will go to every community health center. Java gets them in November and the rest of the country in December. The ministry will also buy more than 1,000 X-ray units, plus light 3-kilogram portable X-rays that work without power lines.",],
  "why": "TB spreads in crowded homes. Finding it early helps stop that.", "outlet": "ANTARA", "date": "Nov 12", "url": "https://en.antaranews.com/news/442131/indonesia-expands-tb-screening-with-5600-new-diagnostic-tools"}
]
PALM = {"type": "numbers", "title": "Palm oil, Jan–Oct 2026", "items": [{"n": "$28.84B", "label": "export earnings, up 60%"}, {"n": "23.8M t", "label": "tons exported, up 6%"}, {"n": "5.15%", "label": "of the economy in Q3"}], "source": "Economy Minister Airlangga Hartarto, via ANTARA, Nov 12"}

can["blurb"] = "A car plant meeting, and fewer foreign students."
can["stories"] = [
 {"tag": "Jobs", "headline": "Ottawa, Ontario and Unifor meet Stellantis about the Brampton plant", "lead": True,
  "paras": ["The meeting is on Thursday in downtown Toronto. Stellantis has sold its idle Brampton car plant to a Canadian defence maker. That could leave thousands of workers without jobs. Prime Minister Carney said Ottawa will “enforce our rights” to protect them.",
            "A 2023 deal promised Stellantis $1.5 billion from Ottawa and Ontario over ten years. It also asked the company to keep its Ontario operations through 2035, including Brampton. Stellantis says it has offered to pay back the government money for the Brampton retooling."],
  "why": "Public money was given on a promise to keep jobs. The meeting asks if that promise still stands.", "outlet": "Global News", "date": "Nov 12", "url": "https://globalnews.ca/news/12147000/ford-feds-unifor-set-for-high-stakes-meeting-with-stellantis/"},
 {"tag": "Universities", "headline": "Atlantic universities have lost almost half their international students", "paras": ["A researcher at Memorial University wrote that international enrolment in the four Atlantic provinces fell by 3,020 students, or 18%, in the past year. Since the federal limits began in January 2024, it is down almost 48%.",
            "Ottawa had expected drops of no more than 10% in these provinces. Instead, new study permit approvals fell by at least 59%. New international enrolment rose 14% this fall."],
  "views": "The writer says the cap is not the only cause. Applications, money pressures and Canada’s appeal also matter. This is analysis by a university researcher, from The Conversation.",
  "why": "Smaller universities depend on these students’ fees to run programs.", "outlet": "The Conversation", "date": "Nov 11", "url": "https://theconversation.com/canadas-international-student-cap-hit-atlantic-universities-hard-heres-why-it-matters-295649"}]
STUD = {"type": "numbers", "title": "Atlantic Canada, international students", "items": [{"n": "−48%", "label": "since Jan 2024"}, {"n": "−18%", "label": "in the past year"}, {"n": "+14%", "label": "new students this fall"}], "source": "The Conversation (Memorial University researcher), Nov 11"}

usa["blurb"] = "A Senate upset in Mississippi, secret bill text, and a rule on college accreditation."
usa["stories"] = [
 {"tag": "Elections", "headline": "Democrat Scott Colom wins the Senate race in Mississippi", "lead": True,
  "paras": ["The Associated Press called the race for Colom, a Democrat, over Republican Senator Cindy Hyde-Smith. He was about 5,000 votes ahead. Mississippi has not elected a Democrat to the Senate since 1982. Colom is the first Black senator from the state since Reconstruction, the years after the Civil War.",
            "Colom began his run in late 2025, and it was seen as a long shot. Hyde-Smith was said to be the likely winner for much of the campaign. NPR reports she called to concede."],
  "why": "It was the closest Senate race this year, in a state few expected to flip.", "outlet": "NPR", "date": "Nov 11", "url": "https://www.npr.org/2026/11/11/nx-s1-6037840/democrat-scott-colom-wins-the-closest-senate-race-in-the-country"},
 {"tag": "Congress", "headline": "Advocates want the Senate to post bill text online before votes", "paras": ["A group from both parties sent a letter asking Senate leaders to post the text of bills and amendments online as soon as senators get it. Right now the text is not always public before a vote. Daniel Schuman, an author of the letter, says problems can “sneak through.”",
            "He gave one example. In 2013, Congress quietly repealed parts of a popular law on lawmakers’ financial disclosure and insider trading."],
  "why": "People can only judge a law if they can read it before it passes.", "outlet": "NPR", "date": "Nov 12", "url": "https://www.npr.org/2026/11/12/nx-s1-6037381/senate-legislation-public-review"},
 {"tag": "Education", "headline": "A new rule gives the Education Department more say over college accreditors", "paras": ["Accreditors are nonprofit groups that check colleges. Their approval lets a school get federal loans and grants. The Education Department finalized a rule that takes effect in July. President Trump has called it his “secret weapon” on higher education.",
            "Accreditors must now look at schools’ policies on “intellectual diversity,” meaning exposure to a range of viewpoints."],
  "views": "Bob Shireman, a former Obama-era Education Department official, warns the rule lets the government “meddle” in colleges. The department says its changes will help new ideas and lower costs.",
  "why": "A school that loses its accreditation can lose access to federal student aid.", "outlet": "NPR", "date": "Nov 12", "url": "https://www.npr.org/2026/11/12/nx-s1-6027967/accreditation-trump-higher-education"}]

wd["blurb"] = "Talks over Ukraine, Kyiv’s blackouts, a Gaza hospital strike, Ebola in Kenya, and a boy found alive."
wd["stories"] = [
 {"tag": "War", "headline": "Russia and Ukraine agree to swap prisoners, but talks bring no big step", "paras": ["Two days of talks in Abu Dhabi, led by the US, ended on Wednesday with no major breakthrough. Both sides said they would hold a large exchange of prisoners of war. It was their first meeting in nine months.",
            "Jared Kushner, President Trump’s son-in-law, said the numbers would be fixed on Thursday. The BBC reports US envoys are meeting the Russian and Ukrainian leaders on Thursday."],
  "why": "Big gaps remain on land and on security promises after any deal.", "outlet": "PBS NewsHour (AP)", "date": "Nov 11", "url": "https://www.pbs.org/newshour/world/russia-and-ukraine-agree-to-a-large-prisoner-exchange-as-talks-end-with-no-major-breakthrough"},
 {"tag": "Winter", "headline": "Ukrainians face long power cuts as Russia hits the grid", "paras": ["In Kyiv, some families get only four or five hours of power a day, at changing times. Some have gone up to 20 hours without it. The cuts began earlier this year than last winter.",
            "Officials fear life becomes very hard if power cannot be kept on at least four hours a day. Ukraine has answered by hitting Russian oil refineries."],
  "why": "Without power, water pumps and lifts stop, and homes get cold.", "outlet": "BBC", "date": "Nov 12", "url": "https://www.bbc.co.uk/news/articles/cr1ewpd95d21o"},
 {"tag": "Gaza", "headline": "An Israeli strike on a Gaza hospital kills six people", "paras": ["Gaza’s Health Ministry says the strike hit the surgical wing of Nasser Hospital in Khan Younis overnight. Six people died, including a surgeon, and at least 28 were hurt. Israel’s military says it hit a Hamas commander and other militants, and gave no proof. It says Hamas used the hospital as a base.",],
  "views": "The two sides disagree on whether the hospital was a legitimate target. The reports come from Gaza’s health authorities and the Israeli military, and NPR could not check them itself.",
  "why": "Nasser is one of the few Gaza hospitals still working.", "outlet": "NPR", "date": "Nov 12", "url": "https://www.npr.org/2026/11/12/nx-s1-6038339/israeli-strike-gaza-hospital"},
 {"tag": "Health", "headline": "Kenya releases its last Ebola patient", "paras": ["Seven people recovered in Kenya, and the last one left hospital on Wednesday. The country now starts a 42-day count. If no new case appears, it can be declared Ebola-free. All 135 people who had contact with patients finished 21 days of watching. In Congo, more than 5,000 people have died since May.",],
  "why": "It shows the virus can be stopped from spreading when contacts are tracked.", "outlet": "BBC", "date": "Nov 11", "url": "https://www.bbc.co.uk/news/articles/cwe9kzv0g0v7o"},
 {"tag": "Rescue", "headline": "A teenager missing six days in the Australian bush is found alive", "paras": ["William, 17, went missing last Friday while camping in bushland about 180 km east of Melbourne. He was found on Thursday and winched to safety with only a few scratches. His mother said he stayed in one spot and waited to be rescued."],
  "why": "Staying put is the usual advice when lost, and here it worked.", "outlet": "BBC", "date": "Nov 12", "url": "https://www.bbc.co.uk/news/articles/ckvg25zmppglo"}]

sci["blurb"] = "Children’s fingerprints on 15,000-year-old clay."
sci["stories"] = [
 {"tag": "Archaeology", "headline": "Stone Age children left fingerprints on clay figures", "lead": True,
  "paras": ["Archaeologists in Israel studied clay figurines made 15,000 to 11,600 years ago by the Natufian people. They found about 150 fragments of sculptures. Around 60 had fingerprints. The spacing of the ridges suggests most were made by women and children, some younger than 10.",
            "One tiny human figure carried both adult and child prints. The lead researcher thinks an adult was teaching a child. The figures are small, and the purpose is unclear."],
  "why": "Children’s share of early art was hard to see until now.", "outlet": "Science News", "date": "Nov 11", "url": "https://www.sciencenews.org/article/stone-age-children-made-art-clay-sculpt"}
]
W[:] = [ind, can, STUD, usa, wd, sci, bub]
bub["paras"] = ["Of the eight newsletters since last night, three were about AI. No news story today is. For something different, read the Stone Age story."]

# ---------------- essays
E = S["essays"]["blocks"]
base = copy.deepcopy(E[0])
yg_idx = [i for i in range(len(YG)) if i not in (0, 1, 12, 38, 51, 52)]
yg = dict(base); yg.update({"essay_id": "slowboring-gasoline", "optional": False, "priority": 9, "new_page": False, "kicker": "Slow Boring · Nov 12 · Opinion",
  "title": "Gasoline isn’t really that expensive", "author": "Matthew Yglesias", "publication": "Slow Boring",
  "dek": "A columnist asks why voters are so angry about prices when the numbers are not as bad as in past years.",
  "paras": [YG[i] for i in yg_idx], "source_note": "slowboring.com/p/gasoline-isnt-really-that-expensive · a podcast plug, two subscribe lines and a footer are left out",
  "counter_label": "In plain words, and the other side",
  "counterpoint": ["The short version: Yglesias says voters are furious about the cost of living, yet inflation is 3.7%, well below the 1970s and the 2021–22 peak, and jobs are plentiful. His guess is that people feel betrayed. After the price jump, neither party made fighting inflation a top goal, and Trump promised prices would fall, which could not happen. He also says anger is about the same in every state, whatever local gas prices are.",
                  "The other side. He calls this a theory based on “vibes rather than data,” and says he is “not that sure.” He writes as a centrist Democrat-leaning columnist who wants his party to change its plans. A reader who disagrees might say that an average price rise hides big jumps in some costs, such as food, which he himself notes with beef. The study he cites checks one effect, gas prices and votes, so it does not settle why people are angry."]})
bb = dict(base); bb.update({"essay_id": "benthams-broadtermism", "optional": False, "priority": 6, "new_page": False, "kicker": "Bentham’s Newsletter · Nov 12 · Opinion",
  "title": "Broadtermism", "author": "Bentham’s Bulldog", "publication": "Bentham’s Newsletter",
  "dek": "A philosopher-blogger argues that what matters most may be far away in space, just as it may be far away in time.",
  "paras": BB, "source_note": "benthams.substack.com/p/broadtermism",
  "counterpoint": ["The short version: Longtermism says the future is so long that most people who will ever live are not born yet, so their lives matter a lot to us. The writer says the same logic works for space. The universe is huge, so most of what matters may be far from Earth. He says this means we should work out compromises about Earth, and spread good values for the far future.",
                   "The other side. This is one person’s argument, with the logic in a few steps, and it rests on guesses. We know almost nothing about whether people or other life will live far away, or whether we can affect them. Critics of longtermism say that very large, uncertain numbers can be used to justify nearly anything, and that people close to us have a stronger claim on our help. The writer also says he finds the view “pretty intuitive,” which is not the same as a proof."]})
S["essays"]["blocks"] = [yg, bb] + [b for b in E[2:] if b["type"] == "box"]

# ---------------- newsstand
ns = S["stand"]["blocks"][0]
ns["items"] = [
 {"essay_id": "benthams-broadtermism", "pub": "Bentham’s Newsletter", "author": "Bentham’s Bulldog", "title": "Broadtermism", "mode": "in full", "summary": "Printed in full in the Essays.", "hide_if_full": True,
  "fallback": ["Opinion, from Thursday. The writer says that if the far future matters most, then what happens far away in space may matter most too. He says this means we should accept compromises about Earth and care more about spreading good values."]},
 {"essay_id": "persuasion-pluralism", "pub": "Persuasion", "title": "Campuses Need More Pluralism, Not Less", "mode": "summary",
  "paras": ["Opinion, from Wednesday; only the free part is public. A faculty group called “Uncivil” says programs that teach students to talk across differences are a plot backed by billionaires. The writer runs one of them and says they teach skills democracy needs. Keep in mind: he defends his own kind of program."]},
 {"essay_id": "canadian-ai-registry", "pub": "Substack (Ilyass)", "title": "The Canadian AI Registry for Incident Tracking", "mode": "summary",
  "paras": ["A proposal for the government’s call for views on AI openness. The writer wants one national registry where companies confidentially report AI accidents and near misses, with only anonymous, combined data made public. Keep in mind: it is one person’s proposal, not a government plan."]}]

S["stand"]["blocks"] = [ns]
# ---------------- back page
d["back"] = {"src": "assets/art/processed/back-03-kawasaki.png", "kicker": "The Road · Stop 3 of 55", "title": "Kawasaki · Hiroshige",
  "caption": "Kawasaki was the third town on the road from Edo. The picture shows a boat full of travellers crossing a river, with Mount Fuji far away in the distance. Hiroshige made 55 prints of the road, and this paper shows one each issue. Turn the page sideways to see it the right way up.",
  "credit": "Public domain. Library of Congress, via Wikimedia Commons."}

# ---------------- notes for Pio (email only)
d["email_notes"] = [
 "Issue No. 3, Thursday Nov 12. Gmail, Calendar, Slack and Todoist all worked. The Quercus calendar feed is not set up; school dates come from Todoist, the Quercus mail and QUERCUS_CONTEXT.md.",
 "Weather: Open-Meteo said its daily limit was reached, so the first three days come from wttr.in (Thursday to Saturday) and Sunday is carried from yesterday’s Open-Meteo forecast. There are four days, not five. Treat Sunday as rough.",
 "Opportunities: it is not Monday, so the list is carried over from yesterday. I re-checked CLR’s page today (deadline Mon Nov 16, 23:59 GMT). Nothing new reached the inbox or Slack. BlueDot’s page shows an AGI Strategy course closing Nov 29; the Frontier AI Governance date (Nov 15) is carried over from earlier checks.",
 "School: the GGRA30 Practical 7 quiz closed last night at 7 pm. Todoist still lists it, so I could not tell if you did it. Only your best 6 of 9 practicals count. MGEA01 also sent a note about make-up midterm information; it only matters if you missed the Oct 15 midterm. The UTSC Registrar sent an “Academic Probation Check-in” on Nov 11. I only put a one-line reminder in the paper and did not copy any details. It lists deadlines and services, so it is worth reading.",
 "Slack: in a DM, you and Joseph Kostousov were setting up a call about your path in AI safety. I left it out of the paper because it is a private chat. The date was not final in what I read.",
 "Left out and why: Matthew Yglesias is printed in full (the post is free). The Epoch Brief, Zvi’s Claude post, the Bentham live-video note and Visual Capitalist were left out for space or as video or podcast items. The Persuasion piece is paywalled after a few paragraphs, so the summary covers only the free part. The Ilyass proposal and the Epoch Brief are about AI, which is fine in essays and the Newsstand but not in World or Science. The Science story is from Science News and is not about AI. I did not use Nature’s cactus story because the page would not load its text. I read but cut for space: the ANTARA palm-oil story (exports up 60% to $28.84 billion, Jan–Oct), the Global News story on Russian players barred from the World Juniors, and a Quanta piece on the metabolism-first idea of life’s origin.",
 "Canada: CBC was blocked. The Stellantis story comes from Global News. Its page did not show the name of the defence company, so the paper says “a Canadian defence maker.” The 2023 deal figures are from the same story.",
 "Spain’s general strike, which was printed yesterday, was not repeated. BBC says clashes broke out in Barcelona on Wednesday night.",
]
d["credits"] = ["Front page band: Katsushika Hokusai, Famous Places on the Tōkaidō in One View (c. 1818). UBC Library, no known copyright restrictions.",
  "Maps: Natural Earth data via world-atlas. Weather: wttr.in and Open-Meteo."]
(HERE / "issue.json").write_text(json.dumps(d, indent=1, ensure_ascii=False))
print("ok")
