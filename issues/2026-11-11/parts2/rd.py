import sys,re,subprocess,html
u=sys.argv[1]
b=subprocess.run(['curl','-sSL','-m','30','-A','Mozilla/5.0',u],capture_output=True,text=True).stdout
b=re.sub(r'(?s)<(script|style|nav|header|footer|aside)[^>]*>.*?</\1>','',b)
ps=re.findall(r'(?s)<(?:p|h2)[^>]*>(.*?)</(?:p|h2)>',b)
ps=[html.unescape(re.sub(r'<[^>]+>','',p)).strip() for p in ps]
ps=[p for p in ps if len(p.split())>6]
print('###',u);print('\n'.join(ps[:int(sys.argv[2]) if len(sys.argv)>2 else 14]))
