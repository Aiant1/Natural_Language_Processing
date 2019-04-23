# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 22:23:13 2019

@author: antika
"""

import re
s = "i was born in 1996"
s1=""
re.match(r".*",s)
re.match(r".*",s1)
re.match(r".+",s1)

re.match(r".+",s)


re.match(r"[a-zA-Z]+",s)
s = "1996 was the year I was born"

re.search(r"[a-zA-Z]+",s)

#^ - starts with

if re.match(r"^1996",s):
    print ("atch")
    
#^ - ends with
if re.search(r"born$",s):
    print ("atch")
    
    
import re    
s2= "I love Avengers"
s3 = "I love love avengers"
re.sub(r"love","hate",s2)
re.sub(r"love","hate",s3)
re.sub(r"[a-z]","0",s2)
re.sub(r"[a-z]","0",s2,flags=re.I)
re.sub(r"[a-z]","0",s2,1,flags=re.I)



import re
s = "i was born in 1996"
s2= "I love $*...*& Avengers"
s3 = "I love        love avengers"

s_modified=re.sub(r"\d","",s)
# \ escaping the actual meaning"
s_modified2=re.sub(r"[$#@!^&*()^%\.]","",s2)
s_modified=re.sub(r"\w","",s2)
s_modified=re.sub(r"\W","",s2)
s_modified=re.sub(r"\s+","",s3)

import re
x = [" this id wolf  f #mehbbn", " I   love ... you", " 123 the number you kn"]
for i in range (len(x)):
    x[i]= re.sub(r"\W\."," ",x[i])
    x[i]= re.sub(r"\d"," ",x[i])
    x[i]= re.sub(r"\s+[a-z]\s+"," ",x[i], flags=re.I)
    x[i]= re.sub(r"^\s","",x[i])
    x[i]= re.sub(r"\s$","",x[i])



    

    
                      



















