# -*- coding: utf-8 -*-
"""
Divide Romanian manifestos into sentences.

October 2013 - fixed extra blank lines.

@author: Iulia
"""

import glob, nltk, re

# Read all the files together:

thepath=glob.glob('C:/Data/Romanian_manifestos/For Python/*.txt')
texts=[]
for i in thepath:
    texts.append([open(i).read()])

# Divide into sentences, based on normal delimiters:
sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
sentlevel=[]
for i in texts:
    temp=sent_tokenizer.tokenize(i[0])
    sentlevel.append([temp])

# Pick one manifesto from the list (3rd here - change first number to 0 for 2st manifesto, 1 for 2nd). 
first=sentlevel[2][0]

print first[0] 
first1=[]
f=[]
fi=[]

# Also divide into sentences based on * and ;. 
for i in range(len(first)):
    first[i]=re.split('\*|\#|;',first[i])


   # Rewrite the lists.     
for i in range(len(first)):
    f.extend(first[i])

for i in range(len(f)):
    fi.append([f[i]])

#Get rid of end-of-line indicators(\n). 
for i in fi:
    for j in i:
        temp1=j.replace('\n', ' ')
        first1.append(temp1)
 

# Write the text document (the 3rd manifesto here). 
# removing blank lines

mani1=open('C:/Data/Romanian_manifestos/Python Output/RO_USL_2012.txt','wb')

for line in first1:
    line1=' '.join(line.split())
    cleanedLine = line1.strip()
    if cleanedLine:
            mani1.write(cleanedLine+'\n')
mani1.close()

