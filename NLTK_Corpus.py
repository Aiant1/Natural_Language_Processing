# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 19:37:36 2019

@author: ASUS
"""

import nltk
nltk.corpus.gutenberg.fileids()
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma)
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
emma.concordance("surprize")


from nltk.corpus import gutenberg
gutenberg.fileids()

for fileid in gutenberg.fileids():
     num_chars = len(gutenberg.raw(fileid)) 
     num_words = len(gutenberg.words(fileid))
     num_sents = len(gutenberg.sents(fileid))
     
     
from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid))
    
from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
chatroom
chatroom1 = nps_chat.raw('10-19-20s_706posts.xml')
chatroom1

from nltk.corpus import brown

brown.categories()

brown.raw(categories="belles_lettres")
brown.words(categories="belles_lettres")

brown.fileids()
brown.raw(fileids=['cg22'])
brown.words(fileids=['cg22'])

import nltk
from nltk.corpus import brown
news_text = brown.words(categories='news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
fdist

cfd = nltk.ConditionalFreqDist((genre,words) for genre in brown.categories() for words in brown.words(categories =genre))
genre = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genre, samples=modals)























