import pandas as pd
import numpy as np
import os
from collections import Counter
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm

def train_model():
   data=pd.read_csv(('training_data.tsv.txt'),header=0,delimiter="\t",quoting=3)


   #removing the not number values

   data.dropna(inplace=True)


   #to reset indices
   data.reset_index(drop=True,inplace=True)

   data.loc[data['label'] != 'Not Found', 'label']='Found'

   #making the training and test data

   X=data['sent']
   y=data['label']
   X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.02,random_state=0)

   #time to clean data by parsing through it
   clean_training_data=[]
   for i in (X_train):
      clean_training_data.append(i)
  ######################################################

   vectorizer=CountVectorizer(ngram_range=(1,2))

   training_features=vectorizer.fit_transform(clean_training_data)

   np.asarray(training_features)
   #now to create the tfidf thing

   tfidf_vec=TfidfTransformer()
   X_train_tfidfvec=tfidf_vec.fit_transform(training_features)

   #time to classify

   #print(X_train_tfidfvec)


   classifier=svm.LinearSVC().fit(X_train_tfidfvec,y_train)


   #time to save classifer and vectorizer

   import pickle

   f=open('da_classifier.pickle','wb')
   pickle.dump(classifier,f)
   f.close()

   g=open('da_vectorizer.pickle','wb')
   pickle.dump(vectorizer,g)
   g.close()
