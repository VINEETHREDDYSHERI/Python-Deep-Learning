from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.svm import LinearSVC

# Loading the training and test data and also shuffling it.
twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)

# (a)
# Creating the instance of which will convert the text data into feature vector.
# The default n-gram used is unigram.
tfidf_Vect = TfidfVectorizer()
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)  # Fitting the data and also transforming

clf = LinearSVC()  # Creating the Linear SVM model
clf.fit(X_train_tfidf, twenty_train.target)  # Training the model

X_test_tfidf = tfidf_Vect.transform(twenty_test.data)  # Transforming the test data to feature vector
predicted = clf.predict(X_test_tfidf)  # Testing the svm model on unseen data
print("The accuracy with Linear SVM model is: ", metrics.accuracy_score(twenty_test.target, predicted))
# The accuracy is 0.853 which is 0.8 more than that of Naive bayes algorithm.

# (b)
# Creating the instance of TfidfVectorizer which includes both unigram and bigrams.
tfidf_Vect = TfidfVectorizer(ngram_range=(1, 2))
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)  # Fitting the data and also transforming

clf = LinearSVC()  # Creating the Linear SVM model
clf.fit(X_train_tfidf, twenty_train.target)  # Training the model

X_test_tfidf = tfidf_Vect.transform(twenty_test.data)  # Transforming the test data to feature vector
predicted = clf.predict(X_test_tfidf)  # Testing the svm model on unseen data
print("The accuracy with Linear SVM model which includes both unigram and bigrams is: ", metrics.accuracy_score(twenty_test.target, predicted))
# The accuracy is 0.857 which is slightly better than the previous model (a).

# (c)
# Creating the instance of TfidfVectorizer that removes stop words according to english dictionary
# And also includes both unigram and bigrams.
tfidf_Vect = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)  # Fitting the data and also transforming

clf = LinearSVC()  # Creating the Linear SVM model
clf.fit(X_train_tfidf, twenty_train.target)  # Training the model

X_test_tfidf = tfidf_Vect.transform(twenty_test.data)  # Transforming the test data to feature vector
predicted = clf.predict(X_test_tfidf)  # Testing the svm model on unseen data
print("The accuracy with Linear SVM model after removing stopwords and n-grams used is both unigram and bigrams is: ", metrics.accuracy_score(twenty_test.target, predicted))
# The accuracy is 0.856. This model is performing better than the first model (a) but not as good as second model (b).
