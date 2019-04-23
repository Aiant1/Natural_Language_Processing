# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 21:09:30 2019

@author: antika
"""

from nltk.corpus import wordnet
synonyms = []
antonyms = []

for word in wordnet.synsets("good"):
    for syn in word.lemmas():
        synonyms.append(syn.name())
        for s in syn.antonyms():
            antonyms.append(s.name())
            
print (set(synonyms))
print (set(antonyms))

# Word Negation Tracking - Strategy 1

import nltk

sentence = "I was not happy with the team's performance"

words = nltk.word_tokenize(sentence)

new_words = []

temp_word = ''
for word in words:
    if word == 'not':
        temp_word = 'not_'
    elif temp_word == 'not_':
        word = temp_word + word
        temp_word = ''
    if word != 'not':
        new_words.append(word)

sentence = ' '.join(new_words)

import nltk
from nltk.corpus import wordnet

sentence = "I was not happy with the team's performance"

words = nltk.word_tokenize(sentence)

new_words = []

temp_word = ''
for word in words:
    antonyms = []
    if word == 'not':
        temp_word = 'not_'
    elif temp_word == 'not_':
        for syn in wordnet.synsets(word):
            for s in syn.lemmas():
                for a in s.antonyms():
                    antonyms.append(a.name())
        if len(antonyms) >= 1:
            word = antonyms[0]
        else:
            word = temp_word + word
        temp_word = ''
    if word != 'not':
        new_words.append(word)

sentence = ' '.join(new_words)











