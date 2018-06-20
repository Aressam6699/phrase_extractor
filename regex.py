#installing dependencies
import re
import numpy as np
import pandas as pd
import os
import matplotlib
from collections import Counter
def regex_find(path):
    #opening file
    #path=r'C:/Users/Shrawan/Desktop/nlpclassifier/trial/training_data.tsv.txt'
    data=pd.read_csv(path,header=0,delimiter='\t',quoting=3)
    #splitting into label and sent
    sent=list(data['sent'])
    label=list(data['label'])
    #print(label)
    useable=[]
    for idi,label1 in enumerate(label):
        if label1!='Not Found':
            useable.append([sent[idi],label1])
    #print(useable)
        #identifying both side patterns
    bothside=[]
    for i in useable:
        phrase=i[1]
        #remove special charachters
        phrase=re.sub('[^A-Za-z0-9]+',' ', phrase)
        tofind='(\w*)\W*('+phrase+')\W*(\w*)'
        findin=i[0]
        for linefound in re.findall(tofind,findin,re.I):
            bothside.append ([" ".join([x for x in linefound if x != ""]),phrase])
    #print(bothside)
    bucketbothside=[]
    for i in bothside:
       bucketbothside.append(i[0].replace(i[1],' '))

    bucketed=((Counter(bucketbothside)).most_common())
    final_bucket1=[j[0] for j in bucketed]
    #print(final_bucket1)
    print('#################################################################################')

    leftside=[]
    for i in useable:
        phrase=i[1]
        #remove special charachters
        phrase=re.sub('[^A-Za-z0-9]+',' ', phrase)
        tofind='(\w*)\W*(\w*)\W*('+phrase+')'
        findin=i[0]
        for linefound in re.findall(tofind,findin,re.I):
            leftside.append ([" ".join([x for x in linefound if x != ""]),phrase])
    #print(bothside)
    bucketleftside=[]
    for i in leftside:
       bucketleftside.append(i[0].replace(i[1],' '))

    bucketed2=((Counter(bucketleftside)).most_common())
    final_bucket2=[j[0] for j in bucketed2]
    #print(final_bucket2)
    return(final_bucket1,final_bucket2)
#regex()
        

