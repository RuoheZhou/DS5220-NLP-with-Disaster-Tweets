from nltk.tokenize import word_tokenize
import nltk
import numpy as np
nltk.download('punkt')
import pandas as pd
import pickle

train = pd.read_csv('train.csv')

import string
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps = PorterStemmer()

def nlp(text_str):
    k = word_tokenize(text_str)
    for i in range(len(k)):
        k[i] = k[i].lower()
    k = [ps.stem(i) for i in k if i not in list(string.punctuation) and i not in stopwords.words('english')]
    k = " ".join(k)
    return k


for i in range(len(train['text'])):
    train['text'][i] = nlp(train['text'][i])

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
tfidf.fit(train['text'])
x_train = tfidf.transform(train['text'])

y_train = train['target']

from catboost import CatBoostClassifier
cat_boost = CatBoostClassifier(verbose=0, random_state = 123)
cat_boost.fit(x_train, y_train)

pickle.dump(cat_boost, open('model.pkl', 'wb'))
