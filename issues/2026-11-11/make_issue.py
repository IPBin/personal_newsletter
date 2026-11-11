"""Issue No. 2 — Wednesday, November 11, 2026. Builds issue.json from yesterday's skeleton."""
import json, subprocess
from pathlib import Path
HERE = Path(__file__).parent
prev = json.load(open(HERE.parent / "2026-11-10" / "issue.json"))
P = lambda n: json.load(open(HERE / "parts" / n))

# ---------- weather
w = json.loads(subprocess.run(["curl", "-sS", "--retry", "4", "--retry-all-errors", "--retry-delay", "2", "-m", "20", "https://api.open-meteo.com/v1/forecast?latitude=43.65&longitude=-79.38&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,rain_sum,snowfall_sum&timezone=America%2FToronto&start_date=2026-11-11&end_date=2026-11-15"], capture_output=True, text=True).stdout)["daily"]
days = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
daily = []
for i, d in enumerate(w["time"]):
    rain, snow, pc = w["rain_sum"][i], w["snowfall_sum"][i], w["precipitation_probability_max"][i]
    typ = "rain" if rain >= 2 else ("snow" if snow >= 0.5 else "")
    summ = "rain" if rain >= 2 else ("light rain" if rain > 0.3 else ("flurries" if snow > 0 else "mostly cloudy"))
    daily.append({"date": d, "day_of_week": days[i], "high": round(w["temperature_2m_max"][i]), "low": round(w["temperature_2m_min"][i]),
                  "precipitation_chance": pc, "precipitation_type": typ, "summary": summ})
print(daily)

# ---------- front
front = {
    "image": {"src": "assets/art/processed/front-overworld-band.png",
              "caption": "The old road from Edo to Kyoto, drawn by Katsushika Hokusai around 1818. Today’s back page is the second stop on that road, Shinagawa."},
    "lede": ["Your GIS Assignment 3 is due at 10:59 this morning, and the Practical 7 quiz closes at 7 tonight. An AI Safety Week session at 11:15 overlaps your GGRA30 lecture, so pick one. Expect drizzle and about 11°, with real rain on Thursday. Two PHLB18 items are still late."],
    "today": [
        {"time": "10:59", "what": "GGRA30 Assignment 3 due (PostgreSQL in QGIS)", "where": "Quercus upload · 5%"},
        {"time": "11:00", "what": "GGRA30 lecture", "where": "HL B101 · until 1:00 · clashes with next", "dim": False},
        {"time": "11:15", "what": "AI Safety Week, Day 3: Power Concentration Risk", "where": "Design Exchange, 234 Bay St · until 12:15", "dim": True},
        {"time": "1:00", "what": "ENGA10 lecture (Mrs Dalloway)", "where": "AC 223 · until 3:00"},
        {"time": "4:00", "what": "GGRA30 practical", "where": "BV 469 · until 5:00"},
        {"time": "6:00", "what": "Hinton Lectures, night 3", "where": "Livestream · until 7:30", "dim": True},
    ],
    "todos": [
        {"topic": "Academics", "items": [
            {"text": "GGRA30 Assignment 3 is due 10:59 this morning. Practical 7 quiz closes 7 tonight.", "src": "Todoist", "urgent": True},
            {"text": "PHLB18 reading response 6 is late. It earns half marks until Nov 16, then nothing.", "src": "Todoist", "urgent": True},
            {"text": "PHLB18 Scaffolding 2 is late. It loses 20% for every 3 days. It stays open to Dec 8.", "src": "Todoist"},
            {"text": "MGEA01 Achieve quiz, Chapter 11: Thursday 7 pm.", "src": "Todoist"},
        ]},
        {"topic": "TAISI", "items": [
            {"text": "Upload your receipts to HCB, if you haven’t.", "src": "#taisi-team"},
            {"text": "Shivam’s cohort, Mon Nov 16: order the kosher meal too.", "src": "Todoist"},
        ]},
        {"topic": "Misc", "items": [
            {"text": "Pay off the credit card by Thursday.", "src": "Todoist", "urgent": True},
            {"text": "Read the UTSC Health and Wellness message waiting in Medeo.", "src": "UofT mail"},
        ]},
    ],
    "brief": [
        {"where": "Essays", "text": "Yglesias on Democratic populism; animals and the far future."},
        {"where": "World", "text": "Indonesia’s vice president; Ukraine talks; a lost WWII ship."},
    ],
}

# ---------- desk
desk_blocks = [
    {"type": "attention", "title": "Needs you", "items": [
        {"what": "School deadlines today.", "detail": "GGRA30 Assignment 3 is due at 10:59 this morning, before your lecture ends. The Practical 7 quiz opens at 1:00 and closes at 7:00 tonight. Both are in Todoist.", "src": "Todoist · QUERCUS_CONTEXT"},
        {"what": "Two PHLB18 items are late.", "detail": "Reading response 6 gets half marks until Nov 16, then is not accepted. Scaffolding 2 loses 20% for every 3 days it is late, so handing it in soon costs less. It closes Dec 8.", "src": "Todoist · QUERCUS_CONTEXT"},
        {"what": "Two course windows close this weekend.", "detail": "BlueDot’s governance course closes Sunday, Nov 15. CLR’s course closes Monday, Nov 16. Both are below.", "src": "bluedot.org · longtermrisk.org"},
    ]},
    {"type": "agenda", "title": "This week and beyond", "items": [
        {"time": "Wed", "what": "AI Safety Week, Day 3: Forecasting AI-Enabled Power Concentration Risk", "where": "11:15–12:15 · Design Exchange · overlaps GGRA30 lecture"},
        {"time": "Wed", "what": "Hinton Lectures, night 3, then the Q&A", "where": "6:00–7:30 pm · livestream"},
        {"time": "Thu", "what": "MGEA01 lecture, Perfect Competition; Achieve quiz Ch. 11 due 7 pm", "where": "7:00–10:00 pm · IC 130"},
        {"time": "Thu", "what": "Credit card payment", "where": "your Todoist date"},
        {"time": "Fri", "what": "Apart epistemics sprint starts; AI Safety Camp project list goes up", "where": "online · see Opportunities"},
        {"time": "Sat", "what": "Marches for an AI treaty", "where": "cities in the US, Canada and France · noted in Astral Codex Ten", "dim": True},
        {"time": "Sun", "what": "COPB50 Informational Interview due; BlueDot closes", "where": "Nov 15"},
        {"time": "Nov 16", "what": "PHLB18 lecture 10–12 (IA 2150) and tutorial 1–2 (HW 402); reading response 7 due; CLR closes; Shivam’s cohort food", "where": "Monday"},
    ]},
    {"type": "events", "title": "Your events (from Luma)", "items": [
        {"when": "Nov 11", "time": "Wed", "name": "AI Safety Week, Day 3.", "detail": "Power Concentration Risk, 11:15 to 12:15.", "status": "approved"},
        {"when": "Nov 9–11", "time": "6 pm", "name": "The Hinton Lectures 2026.", "detail": "Paul Christiano, three evenings. Monday’s and Tuesday’s recordings are online.", "status": "registered"},
    ]},
    {"type": "channels", "title": "TAISI Slack · since Monday", "channels": [
        {"name": "#taisi-team · money and food", "points": [
            "Isabel reminded everyone to upload receipts to HCB. A locked card hurts people who use the Uber Business account. Joseph said he is working on it.",
            "You ordered shawarma from Ali Baba for Shivam’s cohort, and kosher food from Dr. Laffa for Daniel. Isabel thanked you.",
        ]},
        {"name": "#taisi-team · a study-group offer", "points": [
            "Someone outside TAISI wants to run a linear algebra study group. Joseph thinks it is slightly good, but he would not run it and would not call it a TAISI program. He is happy to refer people and may call the organizer first.",
            "Boyan said it should not overlap with his reading group. He asked who the group is for, since it says it is for people outside a university program.",
        ]},
        {"name": "Other channels", "points": ["No new messages in #writing-desk, #si-main or #hackathons. #general had only a note about spare Hinton tickets for Tuesday."]},
    ]},
]
desk = {"id": "desk", "title": "Your Desk", "tab": "For you", "aside": "What needs you, and what TAISI talked about", "blocks": desk_blocks}

# ---------- opportunities (carried from Issue 1; dates re-checked for BlueDot and CLR)
opp = next(b for s in prev["sections"] if s["id"] == "opps" for b in s["blocks"])
opp = json.loads(json.dumps(opp))
opp["note"] = "Programs that don’t fit you yet are listed in this morning’s email. Always check dates on the program’s own site."
opp["intro"] = "Picked for a second-year CS and Public Policy student on TAISI’s operations team. ★ = strong fit. Each item says why. Dates were last checked on each program’s own page on Nov 9. BlueDot and CLR were checked again today."
for g in opp["groups"]:
    for it in g["items"]:
        it["tags"] = [t for t in it["tags"] if t != "new"]
        if it["name"].startswith("Apart: AI"):
            it["deadline_note"] = "starts Fri"
        if it["name"].startswith("Frontier AI Governance"):
            it["deadline_note"] = "Sun; closes in 4 days"
opps = {"id": "opps", "title": "Opportunities", "new_page": False, "tab": "Don’t miss", "aside": "Sorted by deadline", "blocks": [opp]}

# ---------- news
def S(tag, headline, paras, why, outlet, date, url, lead=False, views=None):
    d = {"tag": tag, "headline": headline, "paras": paras, "why": why, "outlet": outlet, "date": date, "url": url}
    if lead: d["lead"] = True
    if views: d["views"] = views
    return d

indonesia = {"type": "region", "kicker": "Region one", "title": "Indonesia", "region": "indonesia", "map_points": [],
  "blurb": "The vice president’s diploma, a forest plan, and jobs abroad.",
  "chart": {"type": "chart", "title": "Indonesians placed in jobs abroad", "sub": "Workers sent abroad in 2025, and the government’s guess for 2026.", "kind": "bars", "unit": "", "max": 400000,
            "rows": [{"label": "2025 (actual)", "value": 296948, "style": "grey"}, {"label": "2026 (projected)", "value": 350000, "style": "solid"}],
            "source": "Ministry of Migrant Worker Protection (KP2MI), via ANTARA, Nov 10"},
  "stories": [
    S("Politics", "Vice President Gibran says he wants to resign over his school diploma",
      ["On Tuesday the palace said Vice President Gibran Rakabuming Raka told President Prabowo Subianto he wants to step down. They met for two and a half hours. The palace said Prabowo did not oppose the idea.",
       "The issue is Gibran’s high school paper. In October the Supreme Court declared his senior high school equivalency certificate invalid. A different court case on his qualifications was dismissed earlier, because the people who filed it had no standing. Gibran asked for another chance to prove the diploma is real, through an administrative court."],
      "Several parties in the House want a formal inquiry. The palace says it respects the House’s right to hold one. Reports say Gibran still does his duties.",
      "ANTARA", "Nov 10", "https://en.antaranews.com/news/441583/palace-confirms-gibrans-intention-to-resign-from-vice-presidency", lead=True,
      views="The palace says a House inquiry is a normal political process. Two parties, PKB and PDI-P, call it the right tool. Gibran wants to answer the question in court instead."),
    S("Forests", "Indonesia says it will protect forests, earn from them, and share them with villages",
      ["At the UN climate meeting (COP31) in Turkey, a forestry ministry adviser gave three priorities for ending forest loss by 2030. They are protecting and restoring forests and peatland, building a forest economy beyond timber, and helping local communities.",
       "Villages now have legal access to more than 8.3 million hectares of forest. That helps about 1.4 million households."],
      "Forests hold carbon, and Indonesia has some of the largest in the world.", "ANTARA", "Nov 10", "https://en.antaranews.com/news/441635/indonesia-outlines-three-priorities-to-halt-deforestation-at-cop31"),
    S("Jobs", "The government wants to send 500,000 trained workers abroad by 2029",
      ["The Ministry of Migrant Worker Protection runs a program called SMK Go Global. It trains vocational school graduates in language and job skills for work in 85 countries. Japan, South Korea, Germany and Austria are among them. It plans 32,000 placements in 2026.",
       "In 2025 about 296,948 Indonesians were placed abroad, and their remittances (money sent home) were Rp288 trillion. The ministry expects up to 350,000 placements this year."],
      "Money sent home by workers abroad is a big source of foreign currency for Indonesia.", "ANTARA", "Nov 10", "https://en.antaranews.com/news/441579/indonesia-targets-500000-migrant-workers-abroad-by-2029"),
  ]}

canada = {"type": "region", "kicker": "Region two", "title": "Canada", "region": "canada", "map_points": [],
  "blurb": "A meeting with China’s leader, a rate rise, and a lost ship found.",
  "stories": [
    S("China", "Carney will raise foreign interference when he meets Xi",
      ["Prime Minister Mark Carney said on Tuesday that he will bring up foreign interference when he meets China’s president, Xi Jinping, next week. The two are expected to meet at the APEC summit in Shenzhen.",
       "Carney also said the two countries’ partnership is growing but has “clear guardrails”. A public inquiry found in January 2025 that China was the top source of foreign interference in Canadian democracy. Carney said a new ambassador to China will be named soon. The post has been empty since spring."],
      "Canada is rebuilding trade ties with China while worrying about its meddling.", "Global News (Canadian Press)", "Nov 10", "https://globalnews.ca/news/12145021/carney-xi-china-foreign-interference/", lead=True),
    S("Rates", "The Bank of Canada says it may raise interest rates again, but slowly",
      ["The bank’s summary of its last meeting says members will decide “one meeting at a time”. Last month it raised its key rate by a quarter point to 2.5%. That was its first rise since 2023.",
       "It fears high oil prices, because of the war in the Middle East, could spread to other prices. It expects inflation to reach 3.5% by the end of this year. The next decision is Dec 9."],
      "Interest rates set what Canadians pay on mortgages and loans.", "Global News (Canadian Press)", "Nov 10", "https://globalnews.ca/news/12144994/bank-of-canada-rate-hike-summary/"),
    S("History", "Divers find a Canadian ship sunk by a German U-boat in 1944",
      ["The S.S. Cornwallis was sailing from Barbados to New Brunswick in December 1944 when a German submarine sank it. Only five of its 48 crew survived. For more than 80 years nobody knew where it lay.",
       "A team of volunteer American divers found it in July, about 16 km from a small island off Maine and 122 metres deep. They checked it was the Cornwallis by its size, 400 feet long. Relatives of the crew say the news brings some closure."],
      "More than 1,600 merchant sailors died carrying supplies in the Second World War.", "Global News", "Nov 10", "https://globalnews.ca/news/12144434/ss-cornwallis-wreckage-found/"),
  ]}

usa = {"type": "region", "kicker": "Region three", "title": "United States", "region": "usa", "map_points": [],
  "blurb": "A House vote on the defense secretary, prices still rising, and California’s billionaire tax.",
  "stories": [
    S("Congress", "The House sends the effort to impeach Defense Secretary Hegseth back to committee",
      ["On Tuesday the House voted to send the impeachment articles back to a committee. That effectively ends the effort for now. Representative Thomas Massie of Kentucky wrote them. He lost his primary. The articles accuse Pete Hegseth of illegal wars and unlawful strikes.",
       "Hegseth said the charges are policy disagreements, and he would carry out the same operations again. President Trump praised him. The same day, House Republicans chose Jim Jordan as their leader, and Senate Republicans kept John Thune."],
      "It shows how much Republicans will back the administration after losing the House.",
      "PBS NewsHour", "Nov 10", "https://www.pbs.org/newshour/show/house-rejects-hegseth-impeachment-as-gop-selects-jordan-and-thune-as-leaders", lead=True,
      views="Massie says Hegseth is a “threat to the Constitution”. Hegseth calls it a “political spectacle”. Don Bacon, a Republican, has doubts about Hegseth but opposed the impeachment as written."),
    S("Prices", "US prices rose 0.4% in October, and about 4% a year is expected",
      ["The latest Consumer Price Index showed prices up four-tenths of a percent in a month, more than expected. Food and energy led the rise. Housing rose 0.3%.",
       "Economists expect about 4% inflation this year, faster than pay is rising. Austan Goolsbee, who runs the Federal Reserve Bank of Chicago, called the report “distressing”. He said price rises in services, such as health care, are not mainly from oil or tariffs."],
      "Prices are rising faster than pay, so most households can buy less.", "PBS NewsHour", "Nov 10", "https://www.pbs.org/newshour/show/u-s-inflation-report-highlights-strain-of-rising-food-energy-and-housing-costs"),
    S("Taxes", "California voters reject a one-time tax on billionaires",
      ["Proposition 40 would have taxed people worth more than $1 billion 5% of their wealth, one time. Most of the money would have replaced federal health-care cuts. The Associated Press said on Monday that “no” had won.",
       "The “no” side raised about 10 times as much money. Sergey Brin of Google gave more than $100 million. Supporters say they may bring the idea back in 2028."],
      "It was the biggest US test yet of taxing the wealth of the very rich.", "Associated Press via PBS", "Nov 10", "https://www.pbs.org/newshour/politics/california-voters-reject-tax-on-net-worth-of-billionaires",
      views="Critics said the rich would leave the state. Supporters said it was needed to protect health care."),
  ]}

world = {"type": "region", "kicker": "Region four", "title": "Around the World", "map_points": [],
  "blurb": "Peace talks in Abu Dhabi, floods feared in Kenya, a court ruling in the Caribbean, and a Malaysian ex-leader at home.",
  "stories": [
    S("Ukraine", "Ukraine, Russia and the US hold a first day of peace talks in Abu Dhabi",
      ["Senior officials met for about four hours on Tuesday and will meet again today. They said little. President Zelensky, who was not there, called the talks “constructive and quite substantive”. US Secretary of State Marco Rubio said they were “very productive”.",
       "Few expect a breakthrough soon. US officials say both sides are showing “a little bit of flexibility” on who will control eastern Ukraine after the war. Prisoner swaps were also discussed. European leaders have mostly been left out, but the US now says they are part of the answer."],
      "These are the main talks on ending a war that began in 2022.", "BBC News", "Nov 10", "https://www.bbc.co.uk/news/articles/cqpvgvrpjvv8o", lead=True),
    S("Kenya", "Kenyans in Nairobi’s river slums fear floods from El Niño",
      ["El Niño is a warming of the Pacific Ocean that changes weather around the world. Forecasters say this one could be among the strongest on record. In March floods killed more than 60 people in Kenya.",
       "Crews are clearing rubbish from Nairobi’s rivers and drains. The city’s drains were built 30 years ago for 2.5 million people, and about 7 million are there by day. A full upgrade would cost up to $192 million, which the city lacks. Officials say up to 100,000 people could be at risk in the worst case."],
      "Poor neighbourhoods by rivers take the worst of the flooding.", "BBC News", "Nov 11", "https://www.bbc.co.uk/news/articles/c8wy9y37z30vo"),
    S("Caribbean", "A UK court strikes down Trinidad and Tobago’s ban on same-sex intimacy",
      ["The Privy Council in London is the island’s final court of appeal. It ruled that the laws break the right to private and family life. The case was brought by Jason Jones, 62, and took 11 years.",
       "It is the first time the court has struck down such a law. Until now Trinidad and Tobago was one of about 34 Commonwealth countries that keep these laws, which date from British rule."],
      "Campaigners hope other countries will see similar court cases.", "BBC News", "Nov 10", "https://www.bbc.co.uk/news/articles/cm0e0evlpp87o"),
    S("Malaysia", "Ex-prime minister Najib Razak leaves prison for house arrest",
      ["Najib, 73, went home late on Tuesday. He was jailed in 2022 for taking money from the 1MDB state fund. Investigators say about $4.5 billion was taken from the fund. In September the king pardoned him on condition that he serve the rest of his sentence, about two years, at home.",
       "The high court ruled the house arrest begins now. Critics say it weakens the fight against corruption, and that Malaysian law has no house arrest."],
      "How a country treats a corrupt former leader signals how serious it is about corruption.", "BBC News", "Nov 10", "https://www.bbc.co.uk/news/articles/cxnv0v4yln7do",
      views="Najib says he was misled by advisers. Critics question the legal basis for house arrest."),
  ]}

science = {"type": "region", "kicker": "Region five", "title": "Science", "map_points": [],
  "blurb": "Emissions dip for a reason that may not last, fungi that hold up grasslands, and a new eye warning.",
  "chart": {"type": "chart", "title": "How big is this year’s dip in CO2?", "sub": "Change in carbon dioxide from fossil fuels, in billion tonnes.", "kind": "bars", "unit": " Gt", "max": 2,
            "rows": [{"label": "2026 (projected)", "value": 0.16, "style": "solid"}, {"label": "2009 financial crisis", "value": 0.5, "style": "grey"}, {"label": "2020 COVID", "value": 1.9, "style": "outline"}],
            "source": "Science News, Nov 10, on a Nature Climate Change study"},
  "stories": [
    S("Climate", "Carbon dioxide from fossil fuels is set to fall slightly in 2026",
      ["Scientists project emissions will fall 0.4% this year. From 2019 to 2025 they grew 0.8% a year on average. The study was published Nov 9 in Nature Climate Change.",
       "The likely cause is high oil prices from the Iran war, not a faster switch to clean energy. Electric cars, wind and solar are helping, though. If they keep growing, they could cancel about 63% of the growth in emissions from 2025 to 2028."],
      "A dip caused by a price shock may not last.", "Science News", "Nov 10", "https://www.sciencenews.org/article/fossil-fuel-emissions-down-2026-gas", lead=True),
    S("Ecology", "Hidden fungi may help save Mongolia’s dry grasslands",
      ["More than 70% of Mongolia’s land is damaged by heat, drought and overgrazing. The country is warming three times faster than the world average. Researchers want to map the underground fungi that trade nutrients with plant roots and help plants live in poor soil.",
       "The idea is early. The team is still looking for the places where these fungi are most common, so those spots can be protected first."],
      "Protecting the soil’s hidden life might be cheaper than replanting land that has died.", "Nature", "Nov 10", "https://www.nature.com/articles/d41586-026-03589-9"),
    S("Health", "Weight-loss drugs must now carry a warning about a rare eye condition",
      ["The US Food and Drug Administration told the makers of Ozempic, Wegovy, Mounjaro and Zepbound to add a warning about NAION. It happens when blood stops reaching the optic nerve. It can cause sudden, painless vision loss in one eye.",
       "The agency found a higher risk of this rare condition in people taking the drugs. Eye doctors say any added risk looks small and that cause is not proven. They tell patients not to stop the drugs without asking a doctor."],
      "Millions take these drugs, so even a rare risk affects many people.", "BBC News", "Nov 10", "https://www.bbc.co.uk/news/articles/crwydyde0lp3o"),
  ]}

bubble = {"type": "box", "style": "tint", "label": "Bubble check", "paras": [
    "Seven of the 12 newsletters that reached your inbox in the last day were about AI. None of today’s 17 news stories is. For something different, read up on Kenya’s drains: a city built for 2.5 million people now holds about 7 million by day."]}
worldsec = {"id": "world", "title": "The World", "tab": "News", "aside": "The facts first. The opinions get labels.", "new_page": True,
            "blocks": [indonesia, canada, usa, world, science, bubble]}

# ---------- essays
yg = P("essay_yglesias.json"); bb = P("essay_bentham.json")
yg_paras = [p for p in yg["paras"] if "Subscribe" not in p]
bb_paras = [p for i, p in enumerate(bb["paras"]) if i not in (15, 16, 19)]
essay_yg = {"type": "essay", "essay_id": "slowboring-sanders-populist", "optional": False, "priority": 9,
  "kicker": "Slow Boring · Nov 10 · Opinion", "title": "Bernie Sanders Did Not Invent Populist Rhetoric", "author": "Matthew Yglesias", "publication": "Slow Boring",
  "dek": "A centre-left writer argues that Democrats have always talked about a “rigged” economy, so last week’s winners are not copying Sanders.",
  "paras": yg_paras, "source_note": "slowboring.com/p/bernie-sanders-did-not-invent-populist · Matthew Yglesias is a Democratic-leaning commentator who is more moderate than Sanders",
  "counter_label": "In plain words, and the other side",
  "counterpoint": [
    "The short version: after the Democrats’ good night last week, some on the left said the winners sound like Bernie Sanders. Yglesias says that is wrong. Talking about a rigged economy and fighting for the “little guy” is how Democrats have talked since Thomas Jefferson. He says what is truly Sanders’s own is his policies, such as Medicare for All (government health insurance for everyone) and a wealth tax. Most Democratic nominees have not adopted those. He adds that voters should judge politicians by what they do, not by their slogans.",
    "The other side. This is opinion, and Yglesias says himself that he is “not that left-wing”. He disagrees with Sanders on policy, so he has a stake in the argument. Sanders’s communications director, Jeremy Slevin, says earlier presidential candidates did not use this kind of broad populist talk. Yglesias answers with history, but a reader can weigh how much old speeches match today’s mood. Another point is open: whether big, specific promises win more votes than slogans. The essay does not test that."]}
essay_bb = {"type": "essay", "essay_id": "benthams-longtermism-animals", "optional": True, "priority": 6, "new_page": False,
  "kicker": "Bentham’s Newsletter · Nov 10 · Opinion", "title": "Longtermism For Animals", "author": "Bentham’s Bulldog", "publication": "Bentham’s Newsletter",
  "dek": "A philosopher-blogger argues that the animal movement should focus on how animals fare in the far future.",
  "paras": bb_paras, "source_note": "benthams.substack.com/p/longtermism-for-animals · two upsetting passages about parasites and a link list are left out",
  "counter_label": "In plain words, and the other side",
  "counterpoint": [
    "The short version: “Longtermism” is the idea that the future could hold so many lives that helping them matters most. The writer says this also applies to animals. If humans spread factory farming, or wild animal suffering, to other planets, the harm could be enormous. He says animal groups should work to stop that, to make future AI care about animals, and to make people kinder to animals.",
    "The other side. This is one writer’s view, and the numbers in it are guesses about a very far future, as he admits. Critics say effort spent on distant futures can take attention from animals suffering now, in farms today, where we know what helps. Others doubt that anyone can predict what will matter for animals in thousands of years. The writer is a committed longtermist, so this is the case from inside that view."]}
poem = {"type": "box", "style": "poem", "optional": True, "priority": -2, "label": "A poem for a wet week",
  "paras": ["I wandered lonely as a cloud / That floats on high o’er vales and hills,", "When all at once I saw a crowd, / A host, of golden daffodils;", "William Wordsworth, “I Wandered Lonely as a Cloud”, 1807. The first four lines. A host is a large crowd."]}
essays = {"id": "essays", "title": "The Essays", "tab": "Read slowly", "aside": "Printed whole, in the writers’ own words", "blocks": [essay_yg, essay_bb, poem]}

# ---------- newsstand
stand = {"type": "newsstand", "items": [
  {"essay_id": "benthams-longtermism-animals", "pub": "Bentham’s Newsletter", "author": "Bentham’s Bulldog", "title": "Longtermism For Animals", "mode": "in full",
   "summary": "Printed in full in the Essays.", "hide_if_full": True,
   "fallback": ["Opinion, from Tuesday. The writer says the animal movement should care most about the far future. If factory farming or wild animal suffering spread to other planets, the harm could be huge. He wants groups to stop that, to make future AI care about animals, and to build kindness toward animals."]},
  {"essay_id": "decker-meritocratic-consensus", "pub": "Homo Economicus", "author": "Nicholas Decker", "title": "On “The Meritocratic Consensus” in Higher Education", "mode": "summary", "url": "https://nicholasdecker.substack.com/p/on-the-meritocratic-consensus-in", "paras": [
    "Opinion. Decker, an economics blogger, disagrees with a new paper on how colleges spend money. The paper notes that top schools have richer students and spend far more on each one. It asks whether that is a good use of money. Decker says the paper’s three theories for why spending more on top students could pay off are never really tested.",
    "Keep in mind: Decker says the paper is “wrong, bad, and annoying”. That is his opinion, and this summary rests on his reading of it, not the paper itself."]},
  {"essay_id": "aisn-85", "pub": "AI Safety Newsletter", "author": "Center for AI Safety", "title": "AISN #85: US midterms favor candidates backing AI regulation", "mode": "summary", "long": True, "url": "https://newsletter.safe.ai/p/aisn-85-us-midterms-favor-candidates", "paras": [
    "Last week’s US elections went well for people who want to regulate AI, the newsletter says. A group that backs data center rules won all six races it spent in. In 44 of 45 local votes on data centers, voters added limits or turned projects down. A poll found 56% of voters said AI and data centers mattered a lot to their vote. But more people named other things, like corruption, living costs and the Iran war.",
    "The authors argue that limits on data centers may not be enough to stop the biggest AI risks. Companies could build elsewhere, or improve AI without more chips. They say rules on how AI is developed may be needed.",
    "Keep in mind: the newsletter comes from an AI safety group. Some in the industry say the vote was about President Trump, not AI."]},
  {"essay_id": "aifutures-q35", "pub": "AI Futures Project", "title": "Q3.5 Timelines Update", "mode": "summary", "long": True, "url": "https://blog.aifutures.org/p/q35-timelines-update-looks-like-the", "paras": [
    "A forecast, and it is long. The authors now think AI that can do the work of the best human AI researchers will probably arrive in 2027. Their main reason is a report from METR, a research group. It estimates that AI is already speeding up progress at one AI company by about two times.",
    "Because of this, the authors say AI development should be slowed or paused, ideally with an international agreement.",
    "Keep in mind: this is a forecast, not a fact, and the authors say there may be mistakes in their model. The group has long argued for caution. I read only the opening of the post."]},
  {"essay_id": "asterisk-german-romantics", "pub": "Asterisk", "title": "What Bay Area culture owes the German Romantics", "mode": "summary", "url": "https://asteriskmag.substack.com/p/what-bay-area-culture-owes-the-german", "paras": [
    "A long essay of about 5,400 words. It asks where humans fit in a universe not made for us, a question that started with the philosopher Spinoza in 1677. It says two modern answers, looking inward and building technology, both come from German Romantic thinkers around 1800. It uses these roots to ask whether those answers can face worries about AI today. I read only the opening, so this is the setup, not the argument."]},
  {"essay_id": "hyperdimensional-iron", "pub": "Hyperdimensional", "author": "Dean W. Ball", "title": "Iron Makes Iron", "mode": "summary", "long": True, "url": "https://www.hyperdimensional.co/p/iron-makes-iron", "paras": [
    "Opinion, and a reply to the AI Futures post above. Last week a research group called METR said one AI company is improving its AI about twice as fast as before, with AI helping. Ball says some AI safety people were frightened by this. He thinks the talk about “recursive self-improvement”, AI that builds better AI, has become too loose and extreme.",
    "He splits it in two. In “weak recursion”, a tool helps make better versions of itself, as iron tools helped make better iron tools. That is normal in technology. “Strong recursion” is AI running its own development with no real human control. Ball agrees that is a bad idea and wants laws against it. But he fears fear of the first kind could lead to bans that slow useful work, such as medicine.",
    "Keep in mind: Ball says his views are his own, but he works at OpenAI, an AI company, and that is worth knowing. I read the first part of the post."]},
  {"essay_id": "vc-fossil-fuels", "pub": "Visual Capitalist", "title": "Ranked: countries that use the most of each fossil fuel", "mode": "blurb", "url": "https://www.visualcapitalist.com/", "summary": "A chart. China burns more coal than the rest of the world combined. The US uses the most oil and natural gas."},
]}
plate = {"type": "figure", "src": "assets/art/processed/overworld-crop-kyoto.png", "caption": "Katsushika Hokusai, Famous Places on the Tōkaidō in One View (c. 1818). UBC Library, no known copyright restrictions."}
standsec = {"id": "stand", "title": "The Newsstand", "new_page": False, "tab": "Your inbox", "aside": "The last 24 hours, summed up", "blocks": [stand, plate]}

issue = {
  "date": "2026-11-11", "date_long": "Wednesday, November 11, 2026", "weekday": "Wednesday", "number": "2", "edition": "Morning edition",
  "weather_word": "Drizzly & cool", "weather": {"daily": daily},
  "front": front, "sections": [desk, opps, worldsec, essays, standsec],
  "email_notes": [], "credits": [], "back": {}
}
issue["email_notes"] = [
  "Todoist worked. Slack, Gmail and Calendar worked. Opportunities were carried over from Issue 1 (it is not Monday). I re-read BlueDot’s and CLR’s own pages: BlueDot closes Nov 15, CLR closes Nov 16, 23:59 GMT. Nothing new reached the inbox or Slack. Left-out items are the same as in Issue 1.",
  "Clash today: GGRA30 lecture (11:00–1:00) overlaps AI Safety Week Day 3 (11:15–12:15). GGRA30 Assignment 3 is due 10:59 am and the Practical 7 quiz closes 7 pm. All dates are from Todoist and QUERCUS_CONTEXT.md (Nov 10 snapshot). The calendar says ENGA10 is in AC 223; the snapshot said ARC. I used the calendar.",
  "Thin reads. Asterisk, AI Futures (Q3.5 timelines) and Hyperdimensional were long, so I read only their first parts and said so in print. Decker’s post is summarised from his own text. The Visual Capitalist item is from the email text only, because its page blocks our reader. Zvi’s Nvidia post, the ControlAI doctrine and the two podcast or video items were left out (Zvi and ControlAI: not read; podcast and live video: your rule).",
  "Bentham’s “Longtermism For Animals” did not fit in full, so the Newsstand carries a short summary. I cut two upsetting passages about parasites from the full text, so if it prints in full later it will carry that edit.",
  "Indonesia: the vice president’s diploma story uses two ANTARA pieces. One ANTARA caption dates a photo Nov. 11; the article text and URL say Nov 10, so I used Nov 10. The National Heroes story (19 people named) was cut for space.",
  "Around the World and Science are not about AI. The Science News emissions article says the researchers used an AI model to help with data and code. The printed story is about the emissions result only.",
  "UTSC Health and Wellness sent a secure message through Medeo on Nov 10. I did not open it. The paper only tells you to read it.",
  "Sources for essays: slowboring.com/p/bernie-sanders-did-not-invent-populist and benthams.substack.com/p/longtermism-for-animals (full text from the Substack posts). The two Substack “live video” notices and Mounk’s podcast were skipped.",
]
issue["back"] = {"src": "assets/art/processed/back-02-shinagawa.png", "kicker": "The Road · Stop 2 of 55", "title": "Shinagawa: Sunrise in the Fifth Month · Hiroshige, c. 1833–34",
  "caption": "Shinagawa was the first town travellers reached after leaving Edo. It sat on the shore of Edo Bay, and its inns, teahouses and boats are all in this view. Hiroshige made 55 prints of the road, and this paper shows one each issue. Turn the page sideways to see it the right way up.",
  "credit": "Public domain (CC0). Cleveland Museum of Art, via Wikimedia Commons."}
issue["credits"] = prev["credits"]
(HERE / "issue.json").write_text(json.dumps(issue, indent=1, ensure_ascii=False))
print("ok")
