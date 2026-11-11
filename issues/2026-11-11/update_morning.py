"""Morning update of Issue No. 2 (Wed Nov 11): fresh news, new essays, fresh weather. Starts from the evening issue.json."""
import json, subprocess
from pathlib import Path
HERE = Path(__file__).parent
D = json.load(open(HERE / "issue.evening.json"))
A = json.load(open(HERE / "parts2" / "acx.json")); N = json.load(open(HERE / "parts2" / "noah.json"))
src = open(HERE / "make_issue.py").read().split("\n")
exec("\n".join(src[7:19]))
d = D
d["weather"] = {"daily": daily}
d["edition"] = "Morning update"
d["weather_word"] = "Cloudy, then rain"
f = d["front"]
f["lede"] = ["Your GIS Assignment 3 is due at 10:59 this morning, and the Practical 7 quiz closes at 7 tonight. An AI Safety Week session at 11:15 overlaps your GGRA30 lecture, so pick one. Expect a cloudy day at about 10°, and real rain on Thursday. Two PHLB18 items are still late."]
f["todos"][0]["items"].insert(1, {"text": "GGRA30 midterm grades were posted in Quercus last night.", "src": "Quercus mail"})
f["brief"] = [{"where": "Essays", "text": "How to take criticism; why India is doing well."},
              {"where": "World", "text": "Indonesia’s vice president; Spain’s strike; Ebola in Congo."}]
S = {s["id"]: s for s in d["sections"]}
W = S["world"]["blocks"]
# ---- Indonesia
ind = W[0]; ind.pop("chart", None)
ind["blurb"] = "A House move against the vice president, a China trade plan, and a forest plan."
forests = ind["stories"][1]
ind["stories"] = [
 {"tag": "Politics", "headline": "Every party in Indonesia’s House backs a move to impeach the vice president", "lead": True,
  "paras": ["All party groups in the House of Representatives have handed in a formal motion to start impeachment of Vice President Gibran Rakabuming Raka. It is about his high school papers. The motion is called the Right to Express an Opinion. It is the first step toward asking whether he can stay in office.",
            "Parties that signed include PDI-P, Golkar, NasDem, PKS, the Democratic Party, PKB and Prabowo’s own party, Gerindra. A lawmaker from PAN said earlier court rulings show Gibran’s school certificate has no legal force. The House leaders say the motion goes to a full meeting of the House on Thursday."],
  "views": "Gibran has said he wants a chance to prove the certificate is real through a court process. Parties in the House say the question is about whether he meets the rules to hold the job.",
  "why": "On Tuesday the palace said Gibran wanted to resign. Now the House is moving to decide the matter itself.",
  "outlet": "ANTARA", "date": "Nov 11", "url": "https://en.antaranews.com/news/441795/all-house-factions-submit-proposal-to-impeach-vp-gibran"},
 {"tag": "Trade", "headline": "Prabowo and Xi plan to talk about a China–Indonesia trade deal",
  "paras": ["President Prabowo Subianto and China’s president, Xi Jinping, will meet at the APEC summit in Shenzhen. APEC is a group of countries around the Pacific Ocean that talk about trade. A foreign ministry official said one point will be an agreement to start talks on a trade deal called a CEPA, short for Comprehensive Economic Partnership Agreement.",
            "Prabowo speaks to the APEC CEO Summit on Nov 18. The leaders’ meeting is on Nov 19. The official said the schedule is packed, so Indonesia may hold only short, informal chats with other partners."],
  "why": "A trade deal with China, Indonesia’s biggest trading partner, would shape prices and jobs.", "outlet": "ANTARA", "date": "Nov 11",
  "url": "https://en.antaranews.com/news/441811/prabowo-xi-to-discuss-china-indonesia-cepa-at-apec-summit"},
 forests]
# ---- United States
usa = W[2]
usa["blurb"] = "A House vote on the defense secretary, prices still rising, and the Justice Department dropping cases."
usa["stories"][2] = {"tag": "Justice", "headline": "The Justice Department asks to wipe out Steve Bannon’s contempt conviction",
  "paras": ["Steve Bannon, an adviser to President Trump, was found guilty of contempt of Congress after he ignored a subpoena from the House committee that studied the Jan. 6 attack on the Capitol. A jury took less than three hours, and an appeals court kept the verdict.",
            "Now the Justice Department has asked a court to drop the case “in the interests of justice.” Bannon’s lawyers do not oppose it. Legal experts told NPR it follows a pattern. In April the department asked to cancel the convictions of about a dozen leaders of the Oath Keepers and Proud Boys groups."],
  "views": "Bruce Searby, a defense lawyer and former prosecutor, says the courts hear no opposing side. The Justice Department did not answer NPR’s request for comment.",
  "why": "Courts normally hear two sides. Here, no one is arguing against the request.", "outlet": "NPR", "date": "Nov 11",
  "url": "https://www.npr.org/2026/11/11/g-s1-152713/doj-abandons-convictions-trump-allies-no-defense"}
# ---- Around the World
wd = W[3]
wd["blurb"] = "Peace talks in Abu Dhabi, a general strike in Spain, Ebola in Congo, and floods feared in Kenya."
st = wd["stories"]
ukraine, kenya = st[0], st[1]
wd["stories"] = [ukraine,
 {"tag": "Strike", "headline": "Spain holds its first general strike in 14 years over high rents",
  "paras": ["Millions of workers in Spain stopped work on Wednesday to demand action on housing. The two main unions, UGT and CCOO, called the strike. Buses and trains ran late or stopped in Barcelona and Madrid, and many schools closed or ran at low levels.",
            "The unions said 90% of workers in the car and port sectors joined, and 75% in energy. Rents in Spain have almost doubled in ten years. The strike comes less than three weeks before a national election."],
  "why": "It shows how much housing costs now shape politics in Europe.", "outlet": "NPR (Associated Press)", "date": "Nov 11",
  "url": "https://www.npr.org/2026/11/11/nx-s1-6037314/spain-general-strike"},
 {"tag": "Health", "headline": "Congo’s Ebola outbreak passes 11,000 cases",
  "paras": ["Congo’s government says 11,042 people have caught Ebola since May, and 5,387 have died. It is the country’s deadliest outbreak. The virus, called Bundibugyo, has no known vaccine or treatment. It has reached 8 of Congo’s 26 provinces.",
            "Fighting in Ituri and North Kivu provinces makes it hard to reach the sick. Some health workers have been attacked by people who distrust the virus warnings. The disease has also spread to Uganda, Kenya and Nigeria."],
  "why": "The worst Ebola outbreak so far, in West Africa from 2014 to 2016, had about 28,000 cases.", "outlet": "NPR (Associated Press)", "date": "Nov 11",
  "url": "https://www.npr.org/2026/11/11/nx-s1-6037304/ebola-congo-outbreak"},
 kenya]
NUM = {"type": "numbers", "title": "Congo’s Ebola outbreak", "items": [{"n": "11,042", "label": "people infected since May"}, {"n": "5,387", "label": "people who have died"}, {"n": "8 of 26", "label": "provinces reached"}], "source": "Congo’s health ministry, via NPR (AP), Nov 11"}
W.insert(4, NUM)
W[6]["paras"] = ["The three newsletters that arrived since last night are about the midterms, India’s economy and how to take criticism. None is about AI. None of today’s news stories is either. For something different, read the Spain story: the price of a flat can move a whole country to strike."]
# ---- Essays
E = S["essays"]["blocks"]
def clean(ps): return [p for p in ps if p not in ("I.", "II.", "III.")]
acx = dict(E[0]); acx.update({"essay_id": "1a1c974b97364390", "optional": False, "priority": 9, "kicker": "Astral Codex Ten · Nov 11 · Opinion", "title": A["title"], "author": "Scott Alexander",
  "publication": "Astral Codex Ten", "dek": "A psychiatrist-blogger explains a trick used to call anyone closed-minded, and how to answer it.",
  "paras": A["paras"], "source_note": "astralcodexten.com/p/escaping-the-outside-criticism-trap · Scott Alexander is a psychiatrist who writes about science and rationality; a list of book reviews at the end is left out",
  "counterpoint": ["The short version: you can attack anyone as closed-minded. If they show they read critics, you say those critics were too close to them. Eric Raymond called this a “Kafkatrap”, because every answer counts as proof you are guilty. Alexander says you should not get lost in it. His rule is to spend most of your attention on views near your own, and a bit less on each step further away, maybe half as much each step. That way you do read outsiders without feeling you must give every view equal time.",
                  "The other side. This is one writer’s view, and he is a target of this kind of criticism, so he has a stake. Critics say “most time on views near mine” can be a polite way to ignore people who disagree the most, and that those are often the ones who spot your blind spots. He answers that you can’t read everything, and that famous or powerful critics aren’t always the right ones. The essay gives no test for who is worth reading."]})
if acx["paras"][-1].startswith("SSC/ACX book reviews"): acx["paras"] = acx["paras"][:-1]
acx["paras"] = clean(acx["paras"])
noah = dict(E[1]); noah.update({"essay_id": "1a1c9d31b03d704b", "optional": True, "priority": 6, "new_page": False, "kicker": "Noahpinion · Nov 11 · Opinion", "title": N["title"], "author": "Noah Smith",
  "publication": "Noahpinion", "dek": "An economics writer argues that India’s economy is doing very well, even if few people notice.",
  "paras": clean(N["paras"]), "source_note": "noahpinion.blog/p/india-is-quietly-doing-great · the charts in the original are left out",
  "counterpoint": ["The short version: Noah Smith says India is where China was around 2008, but doing better in one way: it has cut extreme poverty while keeping inequality down. It grows about 6.5% a year, faster than China now. Government spending on roads and trains is rising fast. Factories are making more cars and electronics. He says it is the brightest big economy in the world right now.",
                  "The other side. This is an opinion piece by an economics blogger, and he says himself that he doubts one popular explanation, the reforms. He also names open problems: weak private investment, poor rural schools and few women in jobs. Others point out that India’s growth figures are sometimes questioned, and that growing fast from a low income is easier than growing fast later. A writer arguing a bullish case may stress the good news."]})
S["essays"]["blocks"] = [acx, noah] + E[2:]
# ---- Newsstand
items = S["stand"]["blocks"][0]["items"]
items[0] = {"essay_id": "1a1c9d31b03d704b", "pub": "Noahpinion", "author": "Noah Smith", "title": N["title"], "mode": "in full", "summary": "Printed in full in the Essays.", "hide_if_full": True,
  "fallback": ["Opinion, from Wednesday. The writer says India is doing very well. Extreme poverty has mostly ended, the economy grows about 6.5% a year, and the government is building roads and trains fast. He says it may become the brightest big economy. He names open problems: weak private investment, poor rural schools and few women in work."]}
# ---- notes
d["email_notes"] = [
 "This is the morning update of Issue No. 2, Wednesday Nov 11. The evening copy was emailed late last night. Things that changed: the two essays (Yglesias on Sanders and Bentham’s animals piece were printed last night, so today’s are Scott Alexander on criticism and Noah Smith on India), the Indonesia, US and Around the World stories, the Bubble check and the weather. Canada, Science, opportunities and the Desk are unchanged except where noted.",
 "Todoist, Gmail, Calendar and Slack worked. No Slack messages since last night. New in Gmail: GGRA30 midterm grades posted (Nov 10, 8:09 pm). The calendar is the same as last night. Opportunities were carried over (it is not Monday). BlueDot closes Nov 15 and CLR closes Nov 16, as checked last night.",
 "Indonesia: the vice president story is from ANTARA, Nov 11. The CEPA story is from ANTARA. I did not use the Aceh recovery or National Heroes stories for space. Canada was not refreshed: CBC is blocked and Global News had only two new items, so last night’s three Canadian stories remain.",
 "Left out and why: Matthew Yglesias’s “Twenty-three points on the midterms” is paywalled (only the free part is public). ControlAI, Hyperdimensional and the Palladium video were left out as before; podcasts and live video follow your rule. The Noah Smith essay had charts and a few lines that point to them. I left the charts out, so a couple of sentences end with a colon.",
 "Around the World and Science are not about AI. The Spain and Ebola stories come from NPR’s copy of Associated Press reports.",
 "UTSC Health and Wellness sent a secure message through Medeo on Nov 10. I did not open it. The paper only tells you to read it.",
]
(HERE / "issue.json").write_text(json.dumps(d, indent=1, ensure_ascii=False)); print("ok")
