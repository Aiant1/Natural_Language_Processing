


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


            