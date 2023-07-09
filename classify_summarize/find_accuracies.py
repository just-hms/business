import reimport pandas as pd
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifierfrom sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizerfrom sklearn.metrics import accuracy_score
from nltk.corpus import stopwordsstop_words = set(stopwords.words('english'))
from nltk.stem import WordNetLemmatizerfrom sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegressionfrom sklearn.svm import SVC
from sklearn.linear_model import SGDClassifierfrom sklearn.naive_bayes import MultinomialNB

# reads the csvdf = pd.read_csv("merged_dataset.csv")
# function that performs text cleaning
def clean_text(text):    
    text = text.lower()
    text = re.sub(r"what's", "what is ", text)    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)    text = re.sub(r"can't", "can not ", text)
    text = re.sub(r"n't", " not ", text)    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)    text = re.sub(r"\'scuse", " excuse ", text)
    text = re.sub('\W', ' ', text)    text = re.sub('\s+', ' ', text)
    text = text.strip(' ')    text=re.sub('[^a-zA-Z]',' ',text)
    text=text.lower()    text=text.split()
    lemmatizer = WordNetLemmatizer()    text=[lemmatizer.lemmatize(word) for word in text if not word in set(stopwords.words('english'))]
    text=' '.join(text)
    return text

# method to the text in the data frame in order to get the relevant informationdf['article']=df['article'].map(lambda article:clean_text(article))
df.to_csv('clean_data.csv', index=False)
# train test split
train, test = train_test_split(df, random_state=42, test_size=0.2)x_train = train.article
x_test = test.articley_train=train.category
y_test=test.category
# we create a matrix based on the frequency of wordsvectorizer=TfidfVectorizer(max_df=0.9,min_df=1,stop_words='english')
train_vectors=vectorizer.fit_transform(x_train)test_vectors=vectorizer.transform(x_test)
total_vectors=vectorizer.transform(df['article'])
# MLPClassifier
mlp = MLPClassifier()mlp.fit(train_vectors, y_train)
mlp_prediction = mlp.predict(test_vectors)mlp_accuracy = accuracy_score(y_test, mlp_prediction)
print("MLP Accuracy:", mlp_accuracy)
# RandomForestClassifierrandom_forest = RandomForestClassifier()
random_forest.fit(train_vectors, y_train)rf_prediction = random_forest.predict(test_vectors)
rf_accuracy = accuracy_score(y_test, rf_prediction)print("Random Forest Accuracy:", rf_accuracy)
# LogisticRegression
logistic_regression = LogisticRegression()logistic_regression.fit(train_vectors, y_train)
lr_prediction = logistic_regression.predict(test_vectors)lr_accuracy = accuracy_score(y_test, lr_prediction)
print("Logistic Regression Accuracy:", lr_accuracy)
# SVC (Support Vector Classifier)svc = SVC()
svc.fit(train_vectors, y_train)svc_prediction = svc.predict(test_vectors)
svc_accuracy = accuracy_score(y_test, svc_prediction)
print("SVC Accuracy:", svc_accuracy)
# SGDClassifiersgd_classifier = SGDClassifier()
sgd_classifier.fit(train_vectors, y_train)sgd_prediction = sgd_classifier.predict(test_vectors)
sgd_accuracy = accuracy_score(y_test, sgd_prediction)print("SGD Classifier Accuracy:", sgd_accuracy)
# Naive Bayes Classifier (MultinomialNB)
naive_bayes = MultinomialNB()naive_bayes.fit(train_vectors, y_train)
nb_prediction = naive_bayes.predict(test_vectors)nb_accuracy = accuracy_score(y_test, nb_prediction)
print("Naive Bayes Accuracy:", nb_accuracy)
# Gradient Boosting Classifiergradient_boosting = GradientBoostingClassifier()
gradient_boosting.fit(train_vectors, y_train)gb_prediction = gradient_boosting.predict(test_vectors)
gb_accuracy = accuracy_score(y_test, gb_prediction)print("Gradient Boosting Accuracy:", gb_accuracy)
