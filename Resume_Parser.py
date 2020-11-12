# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 17:26:18 2019

@author: ANTIKA DAS
"""
import pandas as pd
import re
import docx
from nltk.tokenize import sent_tokenize 

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from io import StringIO
import en_core_web_sm
nlp = en_core_web_sm.load()
import sys
import nltk
mobile1=[]
name1=[]
email1=[]
github1=[]
linkedin1=[]
name=[]
skill1=[]
rawtext=[]
filepath=[]
extension=[]
gender=[]
import glob
doc_files = glob.glob("C:\\Users\\ASUS\\Desktop\\DATA_SCIENCE_FOLDER\\*.doc")
docx_files = glob.glob("C:\\Users\\ASUS\\Desktop\\DATA_SCIENCE_FOLDER\\*.docx")
pdf_files = glob.glob("C:\\Users\\ASUS\\Desktop\\DATA_SCIENCE_FOLDER\\\*.pdf")
#rtf_files = glob.glob("C:\\Users\\Naveen\\Desktop\\Test\\*.rtf")
#text_files = glob.glob("C:\\Users\\Naveen\\Desktop\\Test\\*.txt")
files = set(doc_files + docx_files + pdf_files)
#print (len(files))
from nltk.tag import StanfordNERTagger

from nltk.tokenize import word_tokenize

import os
java_path = "C:\Program Files (x86)\Common Files\Oracle\Java\javapath/java.exe"
os.environ['JAVAHOME'] = java_path

stanford_classifier = 'C:\\Users\\ASUS\\Desktop\\PARSER\\stanford-ner-2018-10-16\\classifiers\\english.all.3class.distsim.crf.ser.gz'

stanford_ner_path = 'C:\\Users\\ASUS\\Desktop\\PARSER\\stanford-ner-2018-10-16\stanford-ner.jar'

# Creating Tagger Object

st = StanfordNERTagger(stanford_classifier, stanford_ner_path, encoding='utf-8')


def convertdocx_doc(path):
    doc=docx.Document(path)
    L=[]
    for para in doc.paragraphs:
        L.append(para.text)
    return '\n'.join(L)




def convert_pdf_to_txt(input_pdf_path):
  
    # Setup pdf reader
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    # Iterate through pages
    path_open = open(input_pdf_path, 'rb')
    for page in PDFPage.get_pages(path_open, pagenos, maxpages=maxpages, password=password,
                                  caching=caching, check_extractable=True):
        interpreter.process_page(page)
    path_open.close()
    device.close()

    # Get full string from PDF
    full_string = retstr.getvalue()
    retstr.close()

    # Normalize a bit, removing line breaks
    full_string = full_string.replace("\r", "\n")
    full_string = full_string.replace("\n", " ")

    # Remove awkward LaTeX bullet characters
    full_string = re.sub(r"\(cid:\d{0,2}\)", " ", full_string)
    return full_string.encode('ascii', errors='ignore')

def extract_phone_numbers(string):
    r = re.compile(r'[0-9\.\-\s+\/()]+')
#    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    
    return [re.sub(r'\D', '', number) for number in phone_numbers]
'''mob = extract_phone_numbers(string)
'''
def extract_skills(string):
    
    nlp_text = nlp(string)
    #print (nlp_text)
    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]
    #print (tokens)
    
    # reading the csv file
    data = pd.read_csv('C:\\Users\\ASUS\Desktop\\DATA_SCIENCE_FOLDER\\Data_Set.csv\\skills.csv')
    
    
    
    # extract values
    skills = list(data.columns.values)
#    print (skills)
    skillset = []
    
    # check for one-grams (example: python)
    for token in tokens:
    #    print (tokens)
        
        if token.lower() in skills:
            skillset.append(token)
    
    #print (set(skillset))
    
    # check for bi-grams and tri-grams (example: machine learning)
    #for token in nlp_text.noun_chunks:
    #    print (token)
    #
    #    token1 = string.strip()
    word = nltk.word_tokenize(string)
    n_gram = list(nltk.ngrams(word,2))
    #print (n_gram)
    
    l3= []
    for i in n_gram:
        c= i[0].lower() + " " + i[1].lower()
        
        l3.append(c)
    a=[x for x in l3 if x in skills]
    for i in a:
        skillset.append(i)
    
    return set(skillset)
    
def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

def extract_linkedin(myString):
    l=re.findall("(?P<url>https?://[^\s]+)", myString)
    return l

def extra_gender(string):
    word_tokenize=nltk.word_tokenize(string.lower())
    if "female"  in word_tokenize:
        
        gender.append("Female")

    elif "male" in word_tokenize:
        gender.append("Male")
    else:
        gender.append("not_mentioned")
    return gender
    



def extract_names(srt):
    email=extract_email_addresses(srt)
    email1=" ".join(email)


    
    head, sep, tail = email1.partition('@')
    s=head
    
    string=re.sub('\d', ' ', s)
    string=string.title()
    string=string.replace("."," ")
    
    
    return string

def extract_github(myString):
    l=re.findall("(?P<url>https?://[^\s]+)", myString)
    return l

def get_continuous_chunks(tagged_sent):
    
    continuous_chunk = []
    current_chunk = []
    
    for token, tag in tagged_sent:
        if tag != "O":
            current_chunk.append((token, tag))
        else:
            if current_chunk: # if the current chunk is not empty
                continuous_chunk.append(current_chunk)
                current_chunk = []
    # Flush the final current_chunk into the continuous_chunk, if any.
    if current_chunk:
        continuous_chunk.append(current_chunk)
    return continuous_chunk

#PDF_CONVERSION
b=[]
for file in files:
    if file.endswith('.pdf'):
        dcx=file
        print (dcx)
        
        text=convert_pdf_to_txt(dcx)
        text=str(text)
        rawtext.append(text)
        filepath.append(file)
        n=extract_names(text)


#NAME
        text1=re.sub("b","",text)
        text1=re.sub("'"," ",text1)
        text2=text1.split()
        for i in text2:
            if i.isupper():
                a=i.title()
                b.append(a)
                b.append(" ")
            else:
                b.append(i)
                b.append(" , ")
        text1=" ".join(b)
        b=[]
        text_list=text1.split()
        text_list=text_list[0:25]                
        text1=" ".join(text_list)
        text1=re.sub('[^A-Za-z0-9]+', ' ', text1)
        tokenized_text = word_tokenize(text1)        
        classified_text = st.tag(tokenized_text)
        ne_tagged_sent = classified_text
        named_entities = get_continuous_chunks(ne_tagged_sent)
        named_entities = get_continuous_chunks(ne_tagged_sent)
        named_entities_str = [" ".join([token for token, tag in ne]) for ne in named_entities]
        named_entities_str_tag = [(" ".join([token for token, tag in ne]), ne[0][1]) for ne in named_entities]
        for i in named_entities_str_tag:
            if "PERSON" in i:
                length=str(i[0]).split()
                if len(length)==3 or len(length)==2:
                    
                    name.append(i[0])
                elif len(length)>3:                                            
                        length=length[0:3]
                        length=" ".join(length)
                        name.append(length)
                break
        else:
            name.append(n) 
            
#GENDER           
        gender=extra_gender(text)
        
#EMAIL        
        email=extract_email_addresses(text)
        
        email1.append(email)
        
#GITHUB
        github11=extract_github(text)
        
            
        for i in github11:
            
            if "github" in i:
        #                print (i)
                github1.append(i)
                break
        
        else:
           github1.append("not_mentoned")
           
#LINKEDIN               
        linkedinnn=extract_linkedin(text)
        for i in linkedinnn:
        #    print(i)
        
            if "linkedin" in i:
                linkedin1.append(i)
                break
        else:
            linkedin1.append("not mentioned")
                
#SKILL        
        skll=extract_skills(text)
        skill1.append(skll)
        mobile_text=text
        mobile_text=re.sub("  ",",",mobile_text)
        mobile_text=mobile_text=re.sub("   ",",",mobile_text)

        mobile=extract_phone_numbers(mobile_text)
    #    print (mobile)
        l3=[]
        for i in mobile:
            
            if  i.isdigit():
            
                l3.append(i)
        
        for i in l3:
            if len(i)>=10 and len(i)<=14:
                a=int(i)
                
    #            print (type(i))
                mobile1.append(a)
                break
        else:
            mobile1.append("not_mentoned")
#                
            
#                
mobile1=['None' if v is None else v for v in  mobile1]        
skill1=['None' if v is None else v for v in  skill1]     
github1=['None' if v is None else v for v in  github1]  
linkedin1=['None' if v is None else v for v in  linkedin1]     
email1=['None' if v is None else v for v in  email1]   
rawtext=['None' if v is None else v for v in  rawtext]
    
for file in files:
    if file.endswith('.docx'):
        text=convertdocx_doc(file)
        rawtext.append(text)
        filepath.append(file)
#        extension.append(file[-1])

        
        
        
        text=str(text)
        print (text)
        n=extract_names(text)
        
        
        gender=extra_gender(text)
        
        
        
        
        email=extract_email_addresses(text)
        
        email1.append(email)
        
        
            
            
        
        
        github11=extract_github(text)
        
            
        for i in github11:
            
            if "github" in i:
        #                print (i)
                github1.append(i)
                break
        
        else:
           github1.append("not_mentoned")
           
        #                
                
        linkedinnn=extract_linkedin(text)
        for i in linkedinnn:
        #    print(i)
        
            if "linkedin" in i:
                linkedin1.append(i)
                break
        else:
            linkedin1.append("not mentioned")
                
        
        skll=extract_skills(text)
        skill1.append(skll)
        
        mobile=extract_phone_numbers(text)
        #    print (mobile)
        l3=[]
        for i in mobile:
            
            if  i.isdigit():
            
        #        print (i)
                l3.append(i)
        #    print (l3)
        
        for i in l3:
            if len(i)>=10 and len(i)<=14:
                a=int(i)
                
        #            print (type(i))
                mobile1.append(a)
                break
        else:
            mobile1.append("not_mentoned")
        
        
#                
mobile1=['None' if v is None else v for v in  mobile1]        
skill1=['None' if v is None else v for v in  skill1]     
github1=['None' if v is None else v for v in  github1]  
linkedin1=['None' if v is None else v for v in  linkedin1]     
email1=['None' if v is None else v for v in  email1]  
#        

print (len(github1))    
print (len(linkedin1))
print (len(email1))
print(len(mobile1))
print(len(skill1))  
print(len(filepath))  
print (len(gender))
print (len(name))


#        
data1=pd.DataFrame({"Name":name,"gender":gender,"filepath":filepath,"rawtext":rawtext,"skills":skill1,"Email":email1,"linkedin":linkedin1,"github":github1,"mobile":mobile1})       

data1=data1.to_csv("C:\\Users\\ASUS\\Desktop\\DATA_SCIENCE_FOLDER\\final_resume_parser1.csv") 
