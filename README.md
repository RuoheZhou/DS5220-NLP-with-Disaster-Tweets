# DS5220-NLP-with-Disaster-Tweets

Predict if the posted tweet is about disaster or not using NLP and Machine Learning

1. Problem Definition

* Predict whether a given tweet is about a real disaster or not 
* Find the model that has the highest accuracy when comes to predict whether a tweet announces disaster or not
* Who might be interested in?
Companies like Twitter might want to collaborate with the federal emergency management agency of the federal government to help them better monitor the natural disaster situation and offer assistance to people and regions affected. This new feature will also increase the number of users on twitter for them to receive notifications on time. 
* Why this project makes sense?
This project is about classifying the posted tweets as disaster related or not. It could be inserted into the system and once there are a number of disaster related tweets about a specific region at a specific time were posted, the system will be able to send notifications to interested parties and users. 

2. NLP
* Tokenization
    Using word_tokenize from nltk.tokenize
* Lowercase; Remove Punctuation; Remove Stopwords
    Using string.punctuation from string package and importing stopwords from nltk.corpus package
* Stemming
    Importing PorterStemmer from nltk.stem
* Combining tokenized and cleaned words into a sentence and use TfidfVectorizer to transform sentences to a matrix of word counts 
    <img width="532" alt="Screen Shot 2022-12-05 at 2 27 59 PM" src="https://user-images.githubusercontent.com/70445052/205756500-84f30a22-2d14-4e7b-8524-53253f4fb611.png">

3. Fitting in Machine Learning Models
* Naive Bayes
Training Accuracy: 0.9485832238693939
Testing Accuracy: 0.5971978984238179
* Random Forest Classifier
Training Accuracy: 0.8498780258960406
Testing Accuracy: 0.7211033274956217
* XGBoost
Training Accuracy: 0.8472508913492213
Testing Accuracy: 0.7092819614711033
* CatBoost
Training Accuracy: 0.8478138487521111
Testing Accuracy: 0.7390542907180385

Since CatBoost performed the best among the four models, a model.pkl file was generated with catboost model trained inside. 

4. Web Application
A web application was built using flask with a user interface as the followering picture:

![Screen Shot 2022-12-05 at 2 38 57 PM](https://user-images.githubusercontent.com/70445052/205758080-191a7cd7-4a38-4419-99d6-00b9470edaa6.png)
By inputting a tweet, the webpage will run the model and inform you whether the tweet is related to a disaster or not.

5. Implementation
Please download all the files and put them into the correct folders just as following:
<img width="493" alt="Screen Shot 2022-12-05 at 2 41 53 PM" src="https://user-images.githubusercontent.com/70445052/205758566-5b6c1629-e671-49b3-89de-c83b39766dcd.png">
<img width="733" alt="Screen Shot 2022-12-05 at 2 42 02 PM" src="https://user-images.githubusercontent.com/70445052/205758592-cde96619-13e9-4cd0-9f9c-07aa49982137.png">

Static and Templates folders are required to put index.html and css file in order for the web application to work. 

Open terminal and CD to the correct directory and run: python main.py to start the application.
