# Natural Language Processing with Disaster Tweets

<img src="https://user-images.githubusercontent.com/70445052/206781487-e448ae6f-1f1e-40fb-8859-7b42dd7ebdae.png" width="700">

Creator: RomoloTavani Credit: Getty Images/iStockphoto


Twitter has become an important communication channel in times of emergency and the ubiquitousness of smartphones enables people to announce an emergency they’re observing in real-time. Therefore, news agencies and disaster relief organizations might be interested in monitoring Twitter to gain a better understanding of the natural disaster situation and to offer assistance to people and regions affected. An application that can automatically categorize tweets as disaster related or not will help with this process.


## 1. Purpose

* The purpose of this project is to build a simple web application that can predict if the imputted tweet is about disaster or not
* The Focus of the project is to find the model that has the highest accuracy when comes to predict whether a tweet announces disaster or not
* Future Work: 
It could be inserted into the system and once there are a number of disaster related tweets about a specific region at a specific time were posted, the system will be able to send notifications to interested parties and users. 

## 2. Implementation

### Word Cleaning
* Tokenization
    Using word_tokenize from nltk.tokenize
* Lowercase; Remove Punctuation; Remove Stopwords
    Using string.punctuation from string package and importing stopwords from nltk.corpus package
* Stemming
    Importing PorterStemmer from nltk.stem
* Combining tokenized and cleaned words into a sentence and then apply word embedding techniques

### Word Embedding
* Word2Vec
* DF-IDF

### Training
* Fitting in machine learning models and compare their accuracies

<img width="784" alt="Screen Shot 2022-12-09 at 11 58 13 AM" src="https://user-images.githubusercontent.com/70445052/206786432-7a9a6b7b-9dc2-4d76-b146-ac99650545b8.png" width="200" height="250"/>


Since CatBoost performed the best among the four models, a model.pkl file was generated with catboost model trained inside. 

### Flask
* Built a user interface with html and css 
<img src="https://user-images.githubusercontent.com/70445052/205758080-191a7cd7-4a38-4419-99d6-00b9470edaa6.png" width="700">

* import new data to model.pkl and generate a prediction in main.py file
* By inputting a tweet, the webpage will run the model and inform you whether the tweet is related to a disaster or not.
<img src="https://user-images.githubusercontent.com/70445052/206791008-1826f5ec-2d01-4c2e-981c-45eab9b675fa.png" width="700">



## 3. Launch
* Please download all the files and put them into the correct folders just as following:
<img alt="Screen Shot 2022-12-05 at 2 41 53 PM" src="https://user-images.githubusercontent.com/70445052/205758566-5b6c1629-e671-49b3-89de-c83b39766dcd.png" width="300" height="300" />

* Static and Templates folders are required to put index.html and css file in.
Open terminal and CD to the correct directory and run: python main.py to start the application.
