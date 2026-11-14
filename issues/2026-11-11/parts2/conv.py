import json,sys,re,html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s): super().__init__(); s.out=[]; s.cur=None; s.skip=0
    def handle_starttag(s,t,a):
        a=dict(a)
        if t in('p','h1','h2','h3','h4','blockquote','li'): s.cur=[t,'']
        if t in('figure','button','style','script','svg') or 'subscription-widget' in a.get('class','') or 'footnote' in a.get('class','') : s.skip+=1
        if t=='br' and s.cur: s.cur[1]+=' '
    def handle_endtag(s,t):
        if t in('figure','button','style','script','svg') and s.skip: s.skip-=1
        if t in('p','h1','h2','h3','h4','blockquote','li') and s.cur and s.cur[0]==t:
            x=re.sub(r'\s+',' ',s.cur[1]).strip()
            if x: s.out.append((t,x))
            s.cur=None
    def handle_data(s,d):
        if s.cur is not None and not s.skip: s.cur[1]+=d
d=json.load(open(sys.argv[1])); p=P(); p.feed(d['body_html'])
paras=[]
for t,x in p.out:
    if t in('h1','h2','h3','h4'): paras.append('## '+x)
    elif t=='blockquote': paras.append('> '+x)
    elif t=='li': paras.append('• '+x)
    else: paras.append(x)
json.dump({'title':d['title'],'url':d['canonical_url'],'dek':d.get('subtitle'),'paras':paras},open(sys.argv[2],'w'),ensure_ascii=False,indent=1)
print(len(paras),sum(len(x.split()) for x in paras)); 
for x in paras[:3]+paras[-6:]: print('>>',x[:200])
