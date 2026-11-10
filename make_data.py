import ast,json
from pathlib import Path
s=ast.parse(Path('../build_exam.py').read_text()); lists=[]; passages=[]
for node in ast.walk(s):
 if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='passages' for t in node.targets):passages=ast.literal_eval(node.value)
 if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id=='enumerate' and isinstance(node.args[0],ast.List):
  try: lists.append((ast.literal_eval(node.args[1]),ast.literal_eval(node.args[0])))
  except:pass
answers=list('BADECCAEBDDAC EBBCEAD'.replace(' ',''))+list('BACAB CABCC'.replace(' ',''))
opts=[['好，我下班以后就去买。','坐公共汽车，大概二十分钟。','当然可以，你想看哪一本？','因为昨天晚上睡得太晚了。','我觉得蓝色的更好看。'],['没关系，下次小心一点儿。','在前面，过了那个路口就到了。','已经好多了，谢谢你的关心。','还没想好，可能去北京。','好啊，我们几点出发？'],['习惯','终于','附近','认真','一共'],['影响','记得','如果','参加','新鲜']]
key=['B','A','D','E','C','C','A','E','B','D','D','A','C','E','B','B','C','E','A','D','B','A','C','A','B','C','A','B','C','C']
written=['我已经写完了作业','这家商店的东西比那家便宜','请把这本书放在桌子上','她一边听音乐一边做饭','他是昨天坐火车来的','气','习','马','信','带']
qs=[]
for start,items in lists:
 if start not in [1,6,11,16,31,36] or len(items)!=5: continue
 for i,t in enumerate(items,start):
  qs.append(dict(id=i,text=t,options=opts[(i-1)//5] if i<=20 else [],answer=key[i-1] if i<=20 else written[i-31],kind='match' if i<=10 else 'fill' if i<=20 else 'order' if i<=35 else 'character'))
for i,(t,q,o) in enumerate(passages,21):
 import re
 qs.append(dict(id=i,text=q,passage=t,options=re.split(r'[ABC]\. ',o)[1:],answer=key[i-1],kind='read'))
qs.sort(key=lambda q:q['id'])
assert len(qs)==40
Path('questions.json').write_text(json.dumps(qs,ensure_ascii=False))
