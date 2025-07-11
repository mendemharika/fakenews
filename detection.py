import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
path = "./Desktop/ProjectGurukul/Fake News Detection/"
true_df = pd.read_csv(path + 'True.csv')
fake_df = pd.read_csv(path + 'Fake.csv')
true_df['label'] = 0
fake_df['label'] = 1
true_df.head()
fake_df.head()
true_df = true_df[['text','label']]
fake_df = fake_df[['text','label']]
dataset = pd.concat([true_df , fake_df])
dataset.shape
dataset.isnull().sum() # no null values
dataset['label'].value_counts()
true_df.shape # true news
fake_df.shape # fake news
dataset = dataset.sample(frac = 1)

dataset.head(20)
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
stopwords = stopwords.words('english')
nltk.download('wordnet')
def clean_data(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z]' , ' ' , text)
    token = row.split()
    token = [lemmatizer.lemmatize(word) for word in token if not word in stopwords]
    clean_news = ' '.join(news)

    return clean_news
dataset['text'] = dataset['text'].apply(lambda x : clean_data(x))
dataset.isnull().sum()
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features = 50000 , lowercase=False , ngram_range=(1,2))
X = dataset.iloc[:35000,0]
y = dataset.iloc[:35000,1]
X.head()
y.head()
from sklearn.model_selection import train_test_split
train_X , test_X , train_y , test_y = train_test_split(X , y , test_size = 0.2 ,random_state = 0)
vec_train = vectorizer.fit_transform(train_data)
vec_train = vec_train.toarray()
vec_test = vectorizer.transform(test_X).toarray()
train_data = pd.DataFrame(vec_train , columns=vectorizer.get_feature_names())
test_data = pd.DataFrame(vec_test , columns= vectorizer.get_feature_names())
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,classification_report
clf = MultinomialNB()
clf.fit(train_data, train_y)
predictions  = clf.predict(test_data)
print(classification_report(test_y , predictions))
predictions_train = clf.predict(train_data)
print(classification_report(train_y , predictions_train))
accuracy_score(train_y , predictions_train)
accuracy_score(test_y , predictions)
