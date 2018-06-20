import os
import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
path_training_data=os.getcwd()+'/training_data.tsv.txt'

path_test_data=os.getcwd()+'/eval_data.txt'

import regex
print('Going Through Training Data of 8000 sentences')
bucket_lists=regex.regex_find(path_training_data)
#print(bucket_lists)

import regex_matcher_imade
print('The following may take time, Be patient dude!')
extracted_stuff_from_eval= regex_matcher_imade.evalregex(bucket_lists[0],bucket_lists[1],path_test_data)
#print(extracted_stuff_from_eval[:20])
print('--------------------------------------------------------------------------------------------------------------------------')
print('_'*50)
import training_classifier_imade

training_classifier_imade.train_model()
print('Importing the trained classifier ')
f = open('da_classifier.pickle', 'rb')
clss = pickle.load(f)
f.close()
###### get vectorizer ######
f = open('da_vectorizer.pickle', 'rb')
vectorizer = pickle.load(f)
f.close()

#load the data

data=[]

eval_data=open(path_test_data,'r')

for sent_msg in eval_data:
   data.append(' '.join(sent_msg.split())) #copied from sample code in github
df= pd.DataFrame(data)

df=df[0]
#print(df)
#cleaning the data and parsing

clean_data=[]

for i in df:
   clean_data.append(i)

count_vectorized_data=vectorizer.transform(clean_data)

np.asarray(count_vectorized_data)

tfidf_trans=TfidfTransformer()

X_data_tfidfed=tfidf_trans.fit_transform(count_vectorized_data)


predictions=clss.predict(X_data_tfidfed)

final=pd.DataFrame(data={'sent':df,'label':predictions})

print('making predictions')
pred_result=list(predictions)

print('Creating files : Bag of words and the final submission')
final.to_csv(('New_bag_of_words.csv'), index=False, quoting=3, escapechar='\\')

#NOW TO FINALLY MAKE MY SUBMISSION........... PHEW!

fully_final_answer=[]
for i,p in enumerate(pred_result):
   if p=='Not Found':
      fully_final_answer.append('Not Found')
   else:
      fully_final_answer.append(extracted_stuff_from_eval[i][1][0])
      #print(type(extracted_stuff_from_eval[i][1][0]))

da_sub=pd.DataFrame(data={'sent': df,'label':fully_final_answer})

da_sub.to_csv(('final_submission'), index=False, quoting=3, escapechar='\\')


print('DONE!!!!!!!!!!!!!!!')

print('Check folder containing the files for submission')
      


