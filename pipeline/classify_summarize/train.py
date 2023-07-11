import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk.stem import WordNetLemmatizer
from sklearn.linear_model import SGDClassifier
import pickle

# reads the csvdf = pd.read_csv("DATA/merged_dataset.csv")
# function that performs text cleaning
def clean_text(text):    
    text = text.lower()
    text = re.sub(r"what's", "what is ", text)    
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)    
    text = re.sub(r"can't", "can not ", text)
    text = re.sub(r"n't", " not ", text)    
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)    
    text = re.sub(r"\'scuse", " excuse ", text)
    text = re.sub('\W', ' ', text)    
    text = re.sub('\s+', ' ', text)
    text = text.strip(' ')    
    text=re.sub('[^a-zA-Z]',' ',text)
    text=text.lower()    
    text=text.split()
    lemmatizer = WordNetLemmatizer()    
    text=[lemmatizer.lemmatize(word) for word in text if not word in set(stopwords.words('english'))]
    text=' '.join(text)
    return text

# method to the text in the data frame in order to get the relevant informationdf['article']=df['article'].map(lambda article:clean_text(article))
# Create and fit the vectorizer
vectorizer_filename = 'vectorizer.pkl'# we create a matrix based on the frequency of words
vectorizer = TfidfVectorizer(max_df=0.9, min_df=1, stop_words='english')
vectors = vectorizer.fit_transform(df['article'])
# Save the vectorizer to a file
with open(vectorizer_filename, 'wb') as file:    
    pickle.dump(vectorizer, file)
# Train the SGDClassifier on the whole dataset
sgd_classifier = SGDClassifier()
sgd_classifier.fit(vectors, df['category'])
# Save the trained model to a file
with open('sgd_classifier_model.pkl', 'wb') as file:    
    pickle.dump(sgd_classifier, file)
