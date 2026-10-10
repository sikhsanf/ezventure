#!/usr/bin/env python3
"""Wrap the game fragment (default /home/claude/ezventure.html) into index.html and stamp a new build id."""
import re,sys,time,json
src=sys.argv[1] if len(sys.argv)>1 else '/home/claude/ezventure.html'
old=open('index.html',encoding='utf-8').read()
i=old.index('<title>');j=old.index("<script>if('serviceWorker'")
head,foot=old[:i],old[j:]
build=time.strftime('%Y%m%d-%H%M%S')
head=re.sub(r'(<meta name="ezv-build" content=")[^"]*(")',r'\g<1>'+build+r'\2',head)
frag=open(src,encoding='utf-8').read().rstrip('\n')
open('index.html','w',encoding='utf-8').write(head+frag+'\n\n'+foot)
json.dump({'build':build},open('version.json','w'))
print('build',build)
