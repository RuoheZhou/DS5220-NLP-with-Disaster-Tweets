from flask import Flask, render_template, request
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
import pandas as pd
import pickle

import string
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps = PorterStemmer()
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
train = pd.read_csv('train.csv')

@app.route("/")
def hello_world():
    return render_template("index.html") #build a directory named 'templates' and put index.html inside, otherwise won't work

def nlp(text_str):
    k = word_tokenize(text_str)
    for i in range(len(k)):
        k[i] = k[i].lower()
    k = [ps.stem(i) for i in k if i not in list(string.punctuation) and i not in stopwords.words('english')]
    k = " ".join(k)
    return k
for i in range(len(train['text'])):
    train['text'][i] = nlp(train['text'][i])

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
tfidf.fit(train['text'])

x_train = count_vect.fit_transform(train['text'])

@app.route("/predict", methods=['POST'])
def predict():
    tweets = request.form['tweets']

    test_sample = nlp(tweets)
    test = tfidf.transform([test_sample])

    prediction = model.predict(test)
    #
    if prediction[0] == 1:
        final_prediction = 'This Tweet is reporting a disaster'
    else:
        final_prediction = 'This Tweet is not about a disaster'
    # prediction

    return render_template("index.html", prediction_text= final_prediction)

if __name__ == "__main__":
    app.run()
