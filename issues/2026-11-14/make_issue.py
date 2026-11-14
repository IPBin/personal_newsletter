"""Issue No. 5, Saturday Nov 14, 2026. Starts from yesterday's issue.json and replaces the content."""
import json, re, copy
R = "/home/user/personal_newsletter/"
d = json.load(open(R + "issues/2026-11-13/issue.json"))
d["date"] = "2026-11-14"; d["date_long"] = "Saturday, November 14, 2026"; d["weekday"] = "Saturday"
d["number"] = "5"; d["weather_word"] = "Cool & dry"
def wd(date, dow, hi, lo, pc, summ): return {"date": date, "day_of_week": dow, "high": hi, "low": lo, "precipitation_chance": pc, "precipitation_type": "", "summary": summ}
d["weather"] = {"daily": [wd("2026-11-14","Saturday",7,2,5,"cloudy"), wd("2026-11-15","Sunday",6,2,0,"mostly sunny"),
  wd("2026-11-16","Monday",9,5,5,"cloudy"), wd("2026-11-17","Tuesday",10,3,0,"dry"), wd("2026-11-18","Wednesday",10,4,0,"dry")]}

# ---------------- front
f = d["front"]
f["image"]["caption"] = "The old road from Edo to Kyoto, drawn by Katsushika Hokusai around 1818. Today’s back page is the fifth stop on that road, Hodogaya."
f["lede"] = ["Nothing is on your calendar today. Expect cloud and about 7°, with sun tomorrow. Three things close this weekend or Monday: the BlueDot course, the Apart sprint and the CLR program. Reading response 6 for PHLB18 earns nothing after Monday."]
f["today"] = [
 {"time": "All day", "what": "Nothing on your calendar", "where": "A free day to catch up"},
 {"time": "Tonight", "what": "Colloquium call, 11 pm", "where": "Slack #colloquium · if tonight is the night"},
 {"time": "Sunday", "what": "Apart sprint entries due 11:59 pm", "where": "Online · see Opportunities", "dim": True}]
f["todos"] = [
 {"topic": "Academics", "items": [
  {"text": "PHLB18 reading response 6 is late. It earns half marks until Mon Nov 16, then nothing.", "src": "Todoist", "urgent": True},
  {"text": "PHLB18 Scaffolding 2 is late (due Nov 2). It loses 20% for every 3 days. It stays open to Dec 8.", "src": "Todoist · QUERCUS_CONTEXT"},
  {"text": "MGEA01: the Chapter 12 quiz is due Thu Nov 19, 7 pm.", "src": "Quercus"}]},
 {"topic": "TAISI", "items": [
  {"text": "Late since Friday: write the Writing Desk proposal, decide what to do with the hackathon, send TAISI ideas to Joseph.", "src": "Todoist", "urgent": True},
  {"text": "Due today: IDS IDC brainstorming, the BlueDot course, your Substack.", "src": "Todoist"},
  {"text": "Shivam’s cohort, Mon Nov 16: order the kosher meal.", "src": "Todoist"}]},
 {"topic": "Misc", "items": [
  {"text": "Robarts room 2H is booked Sat Nov 28, 11:30 to 2:30.", "src": "UofT Libraries"}
  ]}]
f["brief"] = [{"where": "Essays", "text": "Do veterans’ benefits rest on weak science? How sure should we be about hard questions?"},
  {"where": "World", "text": "Why US flights stopped; Alberta’s separatism rift; cash found in Hungary; Uganda’s army."}]

# ---------------- desk
desk = [s for s in d["sections"] if s["id"] == "desk"][0]["blocks"]
desk[0]["items"] = [
 {"what": "Monday is the last day for PHLB18 reading response 6.", "detail": "It earns half marks until Nov 16, then is not accepted. Scaffolding 2 loses 20% for every 3 days it is late, so handing it in soon costs less. It closes Dec 8.", "src": "Todoist · QUERCUS_CONTEXT"},
 {"what": "Three course windows close this weekend and Monday.", "detail": "BlueDot’s Frontier AI Governance course: apply by Nov 15. Apart’s epistemics sprint: entries due Sunday 11:59 pm (anywhere on Earth). CLR’s Fundamentals Program: Monday Nov 16, 11:59 pm GMT.", "src": "bluedot.org · apartresearch.com · longtermrisk.org"},
 {"what": "Three TAISI to-dos went late on Friday.", "detail": "The Writing Desk proposal, the hackathon decision, and your TAISI ideas for Joseph. Joseph also wanted a call about colloquiums “Saturday night”.", "src": "Todoist · #colloquium"}]
desk[1]["title"] = "This week and beyond"
desk[1]["items"] = [
 {"time": "Sat", "what": "Free day. Apart sprint is live. AI Safety Camp is taking team applications.", "where": "Nov 14 · online · see Opportunities"},
 {"time": "Sun", "what": "BlueDot closes. Apart entries due 11:59 pm.", "where": "Nov 15"},
 {"time": "Mon", "what": "PHLB18 lecture 10–12 (IA 2150) and tutorial 1–2 (HW 402); reading response due; CLR closes; Shivam’s cohort food", "where": "Nov 16"},
 {"time": "Wed", "what": "GGRA30 lecture 11–1 (HL B101); ENGA10 lecture 1–3 (AC 223), film: Modern Times; film studies mix and mingle 3:30 (HW 404); GGRA30 practical 4–5 (BV 469); Practical 8 quiz", "where": "Nov 18"},
 {"time": "Thu", "what": "MGEA01 lecture 7–10 pm (IC 130); Chapter 12 quiz due 7 pm", "where": "Nov 19"},
 {"time": "Fri", "what": "After AGI event, TAISI (registered); Robarts room the next day", "where": "Nov 27 · Sat Nov 28 11:30–2:30", "dim": True}]
desk[2]["items"] = [{"when": "Fri Nov 27", "time": "5:30–7:30 pm", "name": "After AGI: What Might a Good Outcome for Humanity Look Like?", "detail": "Jackman Humanities Building, Toronto. Hosted by TAISI. You are registered.", "status": "registered"}]
desk[3]["title"] = "TAISI Slack · since Thursday"
desk[3]["channels"] = [
 {"name": "#colloquium", "points": ["Joseph, Pera and Ayushman agreed to meet at 11 pm. Joseph earlier asked to talk about colloquiums on Saturday night, so this may be tonight.", "Joseph suggested a speaker event with Thomas from METR. Pera prefers Nov 30 to Dec 4."]},
 {"name": "#taisi-team", "points": ["Ilyass needs someone who manages the hacker club to send a Wise money transfer for a hackathon speaker’s talk. Joseph said he can do it.", "Joseph asked Elizabeth to delete an old event so people are not confused."]},
 {"name": "Other channels", "points": ["No other new messages found."]}]

# ---------------- opportunities
opp = [b for s in d["sections"] if s["id"] == "opps" for b in s["blocks"]][0]
cs = opp["groups"][0]["items"]
cs[0]["desc"] = "A free online weekend sprint, Nov 13 to 15. Teams build a test, dataset or tool about how AI changes what people believe. $2,000 in prizes. Entries are due Sunday, Nov 15, 11:59 pm anywhere on Earth."
cs[0]["deadline"] = "2026-11-15"; cs[0]["deadline_short"] = "Nov 15"; cs[0]["deadline_note"] = "Sun 11:59 pm AoE; live now"
cs[1]["deadline_note"] = "Sun; closes tomorrow"
cs[2]["deadline_note"] = "Mon, 23:59 GMT; checked today"
for it in cs:
    if it["name"].startswith("AI Safety Camp"):
        it["deadline_note"] = "Sun Nov 29; team applications opened Nov 13"
opp["intro"] = "Picked for a second-year CS and Public Policy student on TAISI’s operations team. ★ = strong fit. Each item says why. Today I re-checked the CLR, Apart and AI Safety Camp pages. The rest were last checked Nov 9."

drop_names = ("Apart: Threat Intelligence", "Apart: Agent Attribution", "Vector Institute", "UTSC summer research")
for g in opp["groups"]:
    g["items"] = [i for i in g["items"] if not i["name"].startswith(drop_names)]
opp["groups"] = [g for g in opp["groups"] if not g["title"].startswith("For TAISI")]
opp["note"] = "Left out to save space: the TAISI grants line, Apart’s Dec 4 and Dec 11 hackathons, the Vector Institute internship (not open) and the UTSC summer award (likely Feb). They are in this morning’s email. Always check dates on the program’s own site."
# ---------------- world
world = [s for s in d["sections"] if s["id"] == "world"][0]
def S(tag, head, paras, why, outlet, date, url, views=None, lead=False):
    x = {"tag": tag, "headline": head, "paras": paras, "why": why, "outlet": outlet, "date": date, "url": url}
    if views: x["views"] = views
    if lead: x["lead"] = True
    return x
AN = "https://en.antaranews.com/news/"
indo = [
 S("Jobs", "The government has not yet paid the fourth-quarter wage subsidy", [
  "Manpower Minister Yassierli said the payment is still under administrative review at the Finance Ministry. Nothing has been paid out yet. He told people to wait and to beware of fraud.",
  "The plan is Rp300,000 a month for October to December, paid as one lump sum of Rp900,000. It targets about 13.3 million workers who earn Rp3.5 million a month or less. It would cost almost Rp12 trillion."],
  "Fake “subsidy” messages spread when people are waiting for money.", "ANTARA", "Nov 14", AN+"442639/q4-wage-subsidy-still-in-administrative-review-manpower-minister", lead=True),
 S("Forests", "Community-run forests have the fewest fires, the forestry minister says", [
  "Raja Juli Antoni said village forests, community forests and customary (traditional) forests burn the least. He said communities who hold the land protect it better. This is the minister’s view; he did not give fire figures.",
  "By October, the ministry had issued 11,364 permits covering 8.47 million hectares. They reach 1.43 million families."],
  "The government is giving more forest land to local people, and says this also guards against fires.", "ANTARA", "Nov 14", AN+"442635/social-forestry-areas-see-fewest-fires-forestry-minister"),
 S("Trade", "Indonesia widens its rule on keeping export money at home", [
  "Mining exporters with at least 10% investment from seven listed countries or regions must keep at least 30% of export earnings in approved banks for at least three months. The banks now include 11 private and foreign-backed ones, such as HSBC and JPMorgan, plus five state banks.",
  "A new state company, PT Danantara Sumberdaya Indonesia, will handle the paperwork for coal, vegetable oil and ferroalloy exports. Full operation is planned for January 1, 2027."],
  "The rule keeps more foreign money in Indonesian banks, which can help the rupiah.", "ANTARA", "Nov 13", AN+"442615/indonesia-expands-foreign-exchange-earnings-policy-for-exporters"),
 S("Health", "A ministry uses family data to target child stunting in Boyolali", [
  "Stunting means a child is too short for their age because of long-term poor nutrition. In Boyolali, Central Java, it reached 24.5% in 2024, even though the area has plenty of milk, meat and tempeh.",
  "The ministry signed a data deal with the district on Thursday. It lists 22,514 families at risk. Officials say they will focus on a child’s first 1,000 days and on teen health education."],
  "Better data lets help reach the right families.", "ANTARA", "Nov 14", AN+"442663/ministry-integrates-family-data-for-better-stunting-program")]
G = "https://globalnews.ca/news/"
can = [
 S("Politics", "Alberta’s premier will call UCP officials who refuse to sign a pledge on separatism", [
  "Danielle Smith said she will phone the party officials who will not sign a new code of conduct. It says they will respect last month’s referendum. About 75% of voters said Alberta should stay in Canada and not hold a second, binding vote on leaving.",
  "Fifteen of the party’s 87 local association presidents wrote that they will not sign. They say it limits free speech. Smith says members can think what they like, but party spokespeople must reflect party policy."],
  "A governing party is deciding how much open disagreement it will allow.", "Global News", "Nov 13", G+"12150519/ucp-officials-alberta-separatism-pledge/",
  views="Not everyone agrees. Smith says a party must speak with one voice to win elections. The 15 presidents say the party board cannot punish a political view.", lead=True),
 S("Jobs", "Stelco will bring back 175 laid-off workers in Hamilton on December 1", [
  "The steelmaker said higher customer demand lets it restart its finishing operations. Workers will be paid retroactively for the time they were laid off. Restarting will take several weeks.",
  "Stelco’s US owner, Cleveland-Cliffs, announced the layoffs in September. Ottawa said that broke promises made when it approved the 2024 sale, and warned the firm could be forced to sell."],
  "Federal conditions on a foreign takeover were tested, and jobs came back.", "Global News", "Nov 13", G+"12149822/stelco-layoff-recall/"),
 S("Housing", "A Saskatoon group will fight an order to clear a tent camp", [
  "The city ordered Station 20 West to remove more than 15 tents and structures by November 30. It calls them a nuisance. The group, which helps people find housing and work, says it will appeal.",
  "Its board director said moving people out would only shift the problem. The city said the property owner must follow the bylaw."],
  "Cities and charities disagree over who must deal with encampments.", "Global News", "Nov 13", G+"12150007/appeal-encampment-cleanup-saskatoon-station-20/")]
usa = [
 S("Travel", "A rare nationwide ground stop halted US flights for about four hours", [
  "The Federal Aviation Administration stopped flights at all US airports on Friday. By 9 pm ET, more than 8,000 flights were delayed and 7,000 cancelled, according to FlightAware.",
  "Transportation Secretary Sean Duffy blamed old equipment, including “1980s little copper lines.” Pressed on why it failed that day, he had no ready answer. Homeland Security Secretary Markwayne Mullin said there was no sign of an attack."],
  "Aviation relies on old systems, and the cause is still not fully explained.", "NPR", "Nov 13", "https://www.npr.org/2026/11/13/nx-s1-6040403/faa-nationwide-groundstop-airports", lead=True),
 S("Courts", "The Supreme Court will hear Trump’s ban on asylum at the southern border", [
  "The order calls the border an “invasion” and blocks asylum applications. Lower courts found it illegal. The justices will hear the case in the spring and rule by the end of June.",
  "The government says border encounters fell 93% after the order. Rights groups say crossings were already falling, and that the president cannot stop people from applying."],
  "The case tests how far a president can limit a right written into law.", "PBS NewsHour (AP)", "Nov 13", "https://www.pbs.org/newshour/politics/supreme-court-will-consider-trumps-executive-order-suspending-asylum-access-at-the-southern-border",
  views="Not everyone agrees. Solicitor General D. John Sauer calls the limits critical. The ACLU says they unlawfully remove protections."),
 S("Housing", "US home sales fall to their lowest in more than 16 years", [
  "Existing-home sales were 3.75 million (a yearly pace) in October, down 8.8% from a year earlier, says the National Association of Realtors. The average 30-year mortgage rate is 7%.",
  "Prices are falling in some places but are still out of reach for many buyers. Some sellers are holding back."],
  "High loan costs freeze both buying and selling.", "PBS NewsHour", "Nov 13", "https://www.pbs.org/newshour/show/increasing-cost-of-housing-squeezes-americans-out-of-market")]
B = "https://www.bbc.co.uk/news/articles/"
elsew = [
 S("Uganda", "Uganda’s army chief, the president’s son, arrests generals", [
  "At least a dozen generals and senior officers have been arrested in 15 months under Gen Muhoozi Kainerugaba. He is the army chief and the son of President Yoweri Museveni, who has ruled for four decades.",
  "This week he threatened Vice-President Jessica Alupo with dismissal. The ruling party says reports that it rejected backing him are “completely false.”"],
  "No one knows who will lead Uganda next, and the army is part of the story.", "BBC", "Nov 14", B+"cmlydy0xw45wo",
  views="Not everyone agrees. Some see a purge of rivals. Others see an anti-corruption drive."),
 S("India", "India’s young protesters find it hard to gather again", [
  "In July, protests led by Gen Z forced the education minister to resign. In October, thousands who joined a voting-rights protest by the Cockroach Janta Party were detained.",
  "The BJP says the right to protest must stay within the law and not harm public safety."],
  "A protest win can be followed by a tougher response.", "BBC", "Nov 13", B+"cq99e0z4vg1eo"),
 S("Hungary", "Nearly $20 million in cash found in a probe of an Orbán-era minister", [
  "Investigators found the money in safes, buried in forests and hidden in farm buildings. Miklós Seszták, a former development minister, is accused of taking bribes in a state transport company scheme. He denies it.",
  "Prime Minister Péter Magyar won in April on a promise to fight corruption."],
  "It is a test of Hungary’s new anti-corruption drive.", "BBC", "Nov 14", B+"ckjwj03w4w0qo"),
 S("Germany", "Germany’s parliament gives its spy agencies new powers", [
  "The Bundestag voted 309 to 190, with 71 abstentions. Foreign spies of the BND may run covert operations abroad, including sabotage, such as disabling hackers’ servers.",
  "The Left Party warned of a “secret police.” The interior minister called it a “reform of the century.”"],
  "Germany is moving from watching threats to acting on them.", "BBC", "Nov 13", B+"c6jre3z03w4go",
  views="Not everyone agrees. The interior minister says foreign threats require it. The Left Party says it risks abuse.")]
sci = [
 S("Climate", "Oceans and plants take in about half of our carbon, but may slow down", [
  "A study in the journal Science finds the oceans have absorbed 35% of fossil-fuel carbon dioxide since 1990, and forests and other plants 13%.",
  "The ocean sink has grown, but may start to slow. The land sink has not grown, which surprised the team. The authors say measuring both is hard and costly."],
  "These natural sinks decide how much carbon we can still release.", "The Conversation", "Nov 13", "https://theconversation.com/oceans-and-forests-have-absorbed-roughly-half-our-carbon-emissions-for-decades-slowing-climate-change-but-can-they-keep-it-up-296498"),
 S("Fossils", "A turkey-sized “hell chicken” dinosaur may have eaten fruit", [
  "Researchers rebuilt the skull and jaw of Infernogallus, a beaked dinosaur found in Montana. Its jaw moved forward and back, as in fruit-eating parrots.",
  "They say it is the first sign that non-bird dinosaurs adapted to eat fruit, as flowering plants spread."],
  "It adds to evidence that dinosaurs were more varied than thought.", "Science News", "Nov 13", "https://www.sciencenews.org/article/hell-chicken-dinosaur-terror-fruit-eat")]
regs = [b for b in world["blocks"] if b["type"] == "region"]
for blk, st, bl in zip(regs, [indo, can, usa, elsew, sci], [
  "A wage subsidy still waiting, community forests, and a wider export-money rule.",
  "Alberta’s party rift, steel jobs and a tent camp.",
  "A nationwide flight stop, an asylum case and a slow housing market.",
  "Uganda’s army, India’s protests, cash in Hungary and German spies.",
  "How much carbon nature absorbs, and a fruit-eating dinosaur."]):
    blk["stories"] = st; blk["blurb"] = bl
nb = {"type": "numbers", "title": "Indonesia’s wage subsidy, in numbers", "items": [{"n": "Rp900,000", "label": "per worker, paid once"}, {"n": "13.3 million", "label": "workers targeted"}, {"n": "Rp12 trillion", "label": "planned cost"}], "source": "ANTARA, Nov 14"}
nb2 = {"type": "numbers", "title": "Where the carbon goes", "items": [{"n": "35%", "label": "absorbed by oceans since 1990"}, {"n": "13%", "label": "absorbed by plants on land"}, {"n": "3.75 million", "label": "US home sales (yearly pace), Oct"}], "source": "The Conversation (Science study); PBS NewsHour"}
i0 = world["blocks"].index(regs[0]); world["blocks"].insert(i0+1, nb)
for b in world["blocks"]:
    if b["type"] == "box": b["paras"] = ["Of 11 newsletters since yesterday, 3 were mainly about AI. No news story today is. One non-AI read worth your time is the Palladium piece on Brazil’s new party, in your email."]

world_drop = {"A ministry uses family data to target child stunting in Boyolali","Germany’s parliament gives its spy agencies new powers"}
for b in world["blocks"]:
    if b["type"] == "region": b["stories"] = [x for x in b["stories"] if x["headline"] not in world_drop]
world["blocks"] = [b for b in world["blocks"] if b["type"] != "numbers"]
# merge Science into the last region to save a page
regs2 = [b for b in world["blocks"] if b["type"] == "region"]
regs2[3]["stories"] += [x for x in regs2[4]["stories"] if x["tag"] == "Climate"]
regs2[3]["title"] = "Around the World, and Science"
regs2[3]["blurb"] = "Uganda’s army, India’s protests, cash in Hungary, and how much carbon nature absorbs."
world["blocks"].remove(regs2[4])
# ---------------- essays
def clean(t): return re.sub(r"[  ]+", " ", t).strip()
dec = [clean(x) for x in open("/tmp/claude-0/ess/agent-orange-is-a-lie.txt").read().split("\n\n") if x.strip()]
body = dec[0:3] + dec[4:11]
body.append(" ".join(dec[11:21]).replace("; ", "; "))
heads = {"Soft Tissue Sarcoma:","Non-Hodgkin’s Lymphoma:","Hodgkin’s Disease:","B-Cell Leukemias:","Multiple Myeloma:","Respiratory Cancers:","Prostate Cancer:","Bladder Cancer:","Type II Diabetes:","Neuropathy:","Ischemic Heart Disease:","Hypertension:","AL Amyloidosis:","Hypothyroidism:","Spina Bifida:"}
for x in dec[21:53]:
    if x in heads: body.append("## " + x.rstrip(":"))
    elif x == "Parkinson’s Disease:": continue
    else: body.append(x)
body.append(dec[53])
ben = [clean(x) for x in open("/tmp/claude-0/ess/why-are-you-so-confident.txt").read().split("\n\n") if x.strip()]
ess = [s for s in d["sections"] if s["id"] == "essays"][0]
e1, e2 = ess["blocks"][0], ess["blocks"][1]
e1.update({"essay_id": "decker-agent-orange", "priority": 9, "kicker": "Homo Economicus · Nov 13 · Opinion", "title": "Agent Orange did not cause your father’s sickness",
  "author": "Nicholas Decker", "publication": "Homo Economicus", "dek": "An economist argues that the US list of illnesses blamed on Agent Orange rests on weak studies, and that billions are spent on that basis.",
  "paras": body, "source_note": "nicholasdecker.substack.com/p/agent-orange-is-a-lie",
  "counter_label": "In plain words, and the other side",
  "counterpoint": ["The short version: Agent Orange was a chemical the US sprayed in Vietnam. The government treats 19 illnesses as caused by it, so veterans get benefits without proving it. Decker says the studies behind most are weak, and only two skin conditions are clearly linked.",
   "The other side. This is one economist’s reading of the studies, not a new study, and he is not a doctor. He says himself that review panels called much of the evidence “limited or suggestive.” That is weaker than proof, but not nothing. A sick veteran who served where the spray was used may fairly get the benefit of the doubt. A question to carry: when evidence is unclear, who should bear the risk of being wrong?"],
  "new_page": False})
e1.pop("optional", None)
e2.update({"essay_id": "benthams-confident", "priority": 7, "kicker": "Bentham’s Newsletter · Nov 13 · Essay", "title": "Why are you so confident?",
  "author": "Bentham’s Bulldog", "publication": "Bentham’s Newsletter", "dek": "A philosopher says people are too sure of many views, from machine consciousness to shrimp pain, without strong arguments.",
  "paras": ben, "source_note": "benthams.substack.com/p/why-are-you-so-confident · printed in full",
  "counter_label": "In plain words, and the other side",
  "counterpoint": ["The short version: Bentham says you need a strong reason to be very sure of something. On hard questions, such as what can feel pain or what advanced AI might do, he thinks experts should stay unsure.",
   "The other side. These are his own guesses, and he has a clear stake: he writes for readers who share his worries about AI and animals. Critics could say that treating every unsettled question as a coin flip makes small risks seem too large. A question to carry: what am I very sure of, and what is my reason?"],
  "new_page": False})
e2["optional"] = False; e2["priority"] = 7
ess["blocks"] = [e1, e2] + [b for b in ess["blocks"][2:] if b.get("style") == "poem"]
for b in ess["blocks"]:
    if b.get("style") == "poem":
        b["label"] = "A short poem"
        b["paras"] = ["I think I could turn and live with animals, they are so placid and self-contained,", "I stand and look at them long and long.", "Walt Whitman, “Song of Myself,” section 32, 1855. The first two lines."]

bub = [b for b in world["blocks"] if b.get("label") == "Bubble check"]
world["blocks"] = [b for b in world["blocks"] if b.get("label") != "Bubble check"]
ess["blocks"] = ess["blocks"][:2] + bub + ess["blocks"][2:]
ess["blocks"] = [b for b in ess["blocks"] if b.get("style") != "poem"]
# ---------------- newsstand
stand = [s for s in d["sections"] if s["id"] == "stand"][0]
ns = stand["blocks"][0]
ns["items"] = [
 {"essay_id": "decker-agent-orange", "pub": "Homo Economicus", "title": "Agent Orange did not cause your father’s sickness", "mode": "in full", "paras": [], "summary": "", "hide_if_full": True,
  "fallback": ["Opinion. An economist says the evidence for most illnesses on the US Agent Orange list is weak, and that billions are spent on it. Keep in mind: he reviews other people’s studies and is not a doctor."]},
 {"essay_id": "benthams-confident", "pub": "Bentham’s Newsletter", "title": "Why are you so confident?", "mode": "in full", "paras": [], "summary": "", "hide_if_full": True,
  "fallback": ["Opinion. A philosopher says people are too sure of many views without strong arguments, and says this is why he now puts the risk of AI disaster at about 12%. Keep in mind: these are his own estimates."]},
 {"essay_id": "palladium-movement", "pub": "Palladium Magazine", "author": "Oscar Campora", "title": "A Movement Is Not Enough", "mode": "summary", "long": True,
  "paras": ["Opinion. A political consultant in São Paulo says Brazil’s big parties lock out newcomers, so a group called the Free Brazil Movement built its own party, Missão. It collected five times as many valid signatures as Bolsonaro’s party did. Its leader came fourth in the 2026 presidential election. Keep in mind: it reads as an admiring portrait."]}]

d["sections"] = [x for x in d["sections"] if x["id"] != "stand"]
ess["blocks"] = [b for b in ess["blocks"] if b.get("label") != "Bubble check"] + bub + [{"type": "box", "style": "poem", "optional": True, "priority": -2, "label": "A short poem",
  "paras": ["I think I could turn and live with animals, they are so placid and self-contained,", "I stand and look at them long and long.", "Walt Whitman, “Song of Myself,” section 32, 1855. The first two lines."]}]
# ---------------- back
d["back"] = {"src": "assets/art/processed/back-05-hodogaya.png", "kicker": "The Road · Stop 5 of 55", "title": "Hodogaya · Hiroshige",
 "caption": "Hodogaya was the fifth town on the road from Edo. The picture shows travellers crossing the Shinkame Bridge, with tall pines and hills behind. Hiroshige made 55 prints of the road, and this paper shows one each issue. Turn the page sideways to see it the right way up.",
 "credit": "Public domain. Cleveland Museum of Art open-access copy, via Wikimedia Commons."}
d["credits"] = ["Front page band: Katsushika Hokusai, Famous Places on the Tōkaidō in One View (c. 1818). UBC Library, no known copyright restrictions.",
 "Back page: Utagawa Hiroshige, Hodogaya (Shinkame Bridge), from the Fifty-three Stations of the Tōkaidō, c. 1834. Public-domain print via Wikimedia Commons (file CH 18608907-2).",
 "Maps: Natural Earth data via world-atlas. Weather: MET Norway (Open-Meteo was over its daily limit)."]
d["email_notes"] = [
 "Issue No. 5, Saturday Nov 14. I ran this on a Saturday because the schedule fired today. Gmail, Calendar, Slack, Todoist and the web all worked. The Quercus calendar feed is not set up; school dates come from Todoist, Quercus mail and QUERCUS_CONTEXT.md.",
 "Weather: Open-Meteo said its daily limit was exceeded, so the forecast is from MET Norway (api.met.no). Rain chances are my estimates from zero rain in the forecast, not published percentages.",
 "Opportunities: it is not Monday, so the list is carried over. I re-checked CLR (apply by Mon Nov 16, 23:59 GMT), Apart (entries due Sun Nov 15, 11:59 pm AoE) and AI Safety Camp (team applications opened Nov 13, close Nov 29) on their own pages. I did not re-open the BlueDot course page, so its Nov 15 date comes from yesterday’s check. Nothing new reached the inbox or Slack.",
 "School: Todoist no longer lists the MGEA01 Chapter 11 quiz, GGRA30 Practical 7 or the COPB50 interview, so I dropped them. Still late: PHLB18 reading response 6 and Scaffolding 2. New: MGEA01 Chapter 12 quiz due Nov 19, 7 pm; ENGA10 film studies mix and mingle Nov 18, 3:30 pm. Robarts room 2H is booked for Nov 28, 11:30 am to 2:30 pm. Three Todoist items due Nov 13 (Writing Desk proposal, hackathon decision, TAISI ideas for Joseph) are now late.",
 "Slack: read #taisi-team, #colloquium, #phl-panel (others had nothing new). Nobody named you. The Slack digest email about Joseph’s message in #organizing-discussion was not opened.",
 "Essays: Nicholas Decker (Agent Orange) and Bentham’s Bulldog (confidence) are printed in full. Decker’s page had a heading, “Parkinson’s Disease,” with no text under it, so I left that heading out. The Palladium piece “A Movement Is Not Enough” (about 4,200 words) was too long to print. Short version, opinion: a São Paulo political consultant says Brazil’s big parties lock out newcomers, so the Free Brazil Movement built its own party, Missão, which gathered five times as many valid signatures as Bolsonaro’s party; its leader Renan Santos came fourth in the 2026 presidential election. It reads as an admiring portrait. Link: palladium.substack.com/p/a-movement-is-not-enough. Left out: Noahpinion (paid), Persuasion (paywalled), Zvi, ControlAI, Cosmos Institute, the ACX vote reminder, Visual Capitalist, and Substack login codes.",
 "News: CBC and Nature pages were not used. Canada comes from Global News. The Science News “hell chicken” article says the study was reported Oct 10 in Nature Communications although Science News listed it Nov 13, so I did not print a date for the study. I did not print the Microsoft outage or the Nvidia stories because they were mostly about AI. I read but cut: ANTARA on Germany ties, Starship, the New Orleans cruise-boat collision, Alaska’s governor race and the Schumer challenge.",
 "Space: with two long essays in full, I printed 12 news stories and merged Science into Around the World (one science story, the ocean-carbon study). Cut for space: ANTARA on a stunting-data program (Boyolali), BBC on Germany’s new spy powers, and Science News on the “hell chicken” dinosaur (which I read and could print another day). The Newsstand and the TAISI grants line were cut too; Apart’s Dec 4 and Dec 11 hackathons, the Vector Institute internship and the UTSC summer award are still on the carried-over list: Apart Threat Intelligence (Dec 4–6, entries due Dec 6), Apart Agent Attribution (Dec 11–13), Vector (summer 2027, not open), UTSC UTEA (likely Feb).",
 "Art: Hiroshige’s Hodogaya, from Wikimedia (the original link was refused, so I used the Special:FilePath copy at 3,840 px)."]
json.dump(d, open(R + "issues/2026-11-14/issue.json", "w"), ensure_ascii=False, indent=1)
print("ok")
