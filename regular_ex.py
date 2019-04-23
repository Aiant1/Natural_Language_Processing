# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 01:59:17 2019

@author: antika
"""

import re
sentence = "I was born in 1995"
# .* sequence of any characters including 0 number of characters
re.match(r".*",sentence)
sentence1 = " "
re.match(r".*",sentence1)
# .+ sequence of any characters from  1 number of characters to any

sentence2 = "hey how are you "
re.match(r".+",sentence2)
sentence3 = ""
re.match(r".+",sentence3)

#maching word characters
sentence = "I was born in 1995"
re.match(r"[a-zA-Z]",sentence) #match function returns only the first word/character

sentence4 = "1996 I was born"
re.match(r"[a-zA-Z]+",sentence4) 
re.search(r"[a-zA-Z]+",sentence4) 
# starts with
if re.match(r"^1996",sentence4):
    print ("match")
else:
    print ("no match")
#Ends with
if re.search(r"1995$",sentence):
    print ("match")
else:
    print ("no match")
    
#Subsub
s = " I love avenger 5"
re.sub(r"avenger","justice",s)
re.sub(r"\d", "g",s)
re.sub(r"[a-z]", "0",s)
re.sub(r"[a-z]", "0",s,flags=re.I)

#shorthand
sentence11= " hey how are you 66"

sentence22 = " dfg#@!%*9 >& love's ok"

sentence33 = "I       Love You"

sentence11_modified=re.sub(r"\d","",sentence11)
sentence22_modified=re.sub(r"[@#$%^&*()>!\.]","",sentence22) #\. means escaping
sentence22_modified1=  re.sub(r"\w","",sentence22)                            
sentence22_modified2=  re.sub(r"\W"," ",sentence22)  
sentence22_modified3 = re.sub(r"\s+"," ",sentence33)     

sentence22_modified22=  re.sub(r"\s+[a-zA-Z]\s+"," ",sentence22_modified2)  
                     


    


