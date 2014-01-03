# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:24:53 2013

@author: Iulia

Translate Romanian and Spanish manifestos to English. 
Uses goslate - a free Python module for Google Translate API. 
"""

import glob, os
import goslate

#Test:
gs = goslate.Goslate()
print gs.translate('hello world', 'ro').encode('utf-8')


thepath=glob.glob('D:/Manifestos/Spanish manifestos split/*.txt')

for i in thepath:
    base=os.path.basename(i)
    file_name=os.path.splitext(base)[0]
    text=([open(i).read().decode('iso-8859-1')])
    with open('D:/Manifestos/Spanish manifestos split/Translated/en_%s.txt' %file_name, 'wb') as f:
        for line in text:
             transl=gs.translate(line, 'en').encode('utf-8')
             f.write(transl+'\n')
    pass

