# -*- coding: utf-8 -*-
import re
corpus = []
corpus2 = []
l_id = []

nnum = 0
for line in open('segmentation', 'r').readlines():
    #print type(line)
    #print line
    corpus.append(line.strip())
    line = line.replace('　','')
    a = re.split(r'\s+',line)
    if a != []:
        l_id.append(a[0])
    #print a[0]
    '''
    for i in a:
        i=i.decode('utf-8')
        print [i]
        print type(i),i,len(i)
    '''
    corpus2.append(a[1:-1])
    nnum+=1
print nnum

f = open('corpusxz.txt','w')
f.write(str(nnum)+'\n')
num = 0
for line in corpus2:
    
    for token in corpus[1:]:
        f.write(str(token)+'')
    f.write('\n')
    num=num+1
print num
