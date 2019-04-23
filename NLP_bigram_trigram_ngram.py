## -*- coding: utf-8 -*-
#"""
#Created on Sun Feb 10 03:27:11 2019
#
#@author: ASUS
#"""
#
#import nltk
#import re
#from nltk.stem import PorterStemmer
#from nltk.stem import WordNetLemmatizer
#from nltk.corpus import stopwords
#import heapq
#import numpy as np
#paragraph = """Thank you all so very much. Thank you to the Academy. 
#               Thank you to all of you in this room. I have to congratulate 
#               the other incredible nominees this year. The Revenant was 
#               the product of the tireless efforts of an unbelievable cast
#               and crew. First off, to my brother in this endeavor, Mr. Tom 
#               Hardy. Tom, your talent on screen can only be surpassed by 
#               your friendship off screen … thank you for creating a t
#               ranscendent cinematic experience. Thank you to everybody at 
#               Fox and New Regency … my entire team. I have to thank 
#               everyone from the very onset of my career … To my parents; 
#               none of this would be possible without you. And to my 
#               friends, I love you dearly; you know who you are. And lastly,
#               I just want to say this: Making The Revenant was about
#               man's relationship to the natural world. A world that we
#               collectively felt in 2015 as the hottest year in recorded
#               history. Our production needed to move to the southern
#               tip of this planet just to be able to find snow. Climate
#               change is real, it is happening right now. It is the most
#               urgent threat facing our entire species, and we need to work
#               collectively together and stop procrastinating. We need to
#               support leaders around the world who do not speak for the 
#               big polluters, but who speak for all of humanity, for the
#               indigenous people of the world, for the billions and 
#               billions of underprivileged people out there who would be
#               most affected by this. For our children’s children, and 
#               for those people out there whose voices have been drowned
#               out by the politics of greed. I thank you all for this 
#               amazing award tonight. Let us not take this planet for 
#               granted. I do not take tonight for granted. Thank you so very much."""
#
#
#sentence=nltk.sent_tokenize(paragraph)
#word_tokenize=nltk.word_tokenize(paragraph)
#
##sentence.split(" ")
##sentence.split(",")
#
##STEMMING
#stemming = PorterStemmer()
#
#sentence=nltk.sent_tokenize(paragraph)
#
#for i in range(len(sentence)):
#    words= nltk.word_tokenize(sentence[i])
#    newwords= [stemming.stem(word) for word in words]
#    sentence[i] = " " .join(newwords)
#
##Lemmatization
#lemmatizer = WordNetLemmatizer()
#sentence=nltk.sent_tokenize(paragraph)
#for i in range(len(sentence)):
#    words= nltk.word_tokenize(sentence[i])
#    newwords= [lemmatizer.lemmatize(word) for word in words]
#    sentence[i] = " " .join(newwords)
#
#
##STOPWORDS
#sentence=nltk.sent_tokenize(paragraph)
#for i in range(len(sentence)):
#    words= nltk.word_tokenize(sentence[i])
#    newwords= [word for word in words if word not in stopwords.words("english")]
#    sentence[i] = " " .join(newwords)    
#
#
##PARTS OF SPEECH
#words = nltk.word_tokenize(paragraph)
#tagged_words = nltk.pos_tag(words)
#
##sentence=nltk.sent_tokenize(paragraph)
#
##tagged_sents = nltk.pos_tag_sents(sentence)
#
#
#word_tagged=[]
#for i in tagged_words:
#    word_tagged.append(i[0]+"_"+i[1])
#    
#tagged_para = " " .join(word_tagged)
#
#
##NAMED ENTITY 
#words = nltk.word_tokenize(paragraph)
#tagged_words = nltk.pos_tag(words)
#
#nameentity=nltk.ne_chunk(tagged_words)
#nameentity.draw()
#
##BAG OF WORDS
#dataset=nltk.sent_tokenize(paragraph)
#for i in range(len(sentence)):
#    sentence[i]= sentence[i].lower()
#    sentence[i]= re.sub(r"\W"," ",sentence[i])
#    sentence[i]= re.sub(r"\s+"," ",sentence[i])
#
##creating histogram
#    
#wordcount = {}
#for i in dataset:
#    words =  nltk.word_tokenize(i) 
#    for word in words:
#        if word not in wordcount.keys():
#            wordcount[word]=1
#        else:
#            wordcount[word] +=1
#
#most_frequent_words=heapq.nlargest(100,wordcount,key=wordcount.get)
#
#X = []
#for data in dataset:
#    vector=[]
#    for word in most_frequent_words:
#        if word in nltk.word_tokenize(data):
#            vector.append(1)
#        else:
#            vector.append(0)
#    X.append(vector)
#
#
#X = np.asarray(X)
#
##TF-IDF
##TF
## IDF Dictionary
#word_idfs = {}
#for word in most_frequent_words:
#    doc_count = 0
#    for data in dataset:
#        if word in nltk.word_tokenize(data):
#            doc_count += 1
#    word_idfs[word] = np.log(len(dataset)/(1+doc_count))
#    
## TF Matrix
#tf_matrix = {}
#for word in most_frequent_words:
#    doc_tf = []
#    for data in dataset:
#        frequency = 0
#        for w in nltk.word_tokenize(data):
#            if word == w:
#                frequency += 1
#        tf_word = frequency/len(nltk.word_tokenize(data))
#        doc_tf.append(tf_word)
#    tf_matrix[word] = doc_tf
#    
## Creating the Tf-Idf Model
#tfidf_matrix = []
#for word in tf_matrix.keys():
#    tfidf = []
#    for value in tf_matrix[word]:
#        score = value * word_idfs[word]
#        tfidf.append(score)
#    tfidf_matrix.append(tfidf)   
#    
## Finishing the Tf-Tdf model
#X = np.asarray(tfidf_matrix)
#
#X = np.transpose(X)


#N-grams\\
import nltk
from nltk.util import bigrams,trigrams,ngrams
text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""
word = nltk.word_tokenize(text)
b_gram = list(nltk.bigrams(word))
for i in b_gram:
    if i== "Global":
        print (i)
t_gram = list(nltk.trigrams(word))
t_gram
n_gram = list(nltk.ngrams(word,5))
n_gram


            