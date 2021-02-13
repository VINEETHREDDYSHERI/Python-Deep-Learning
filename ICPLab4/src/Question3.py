# Importing the pandas and packages from sklearn to split the data, Naive Bayes algorithm
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

dataFrame = pd.read_csv("glass.csv")  # Loading the train.csv file data using pandas
Y_dataFrame = dataFrame["Type"]  # Creating the target dataFrame
X_dataFrame = dataFrame.drop("Type", axis=1)  # Dropping the target column in the Training dataframe
# Splitting the dataset into the Training and Testing
X_train, X_test, y_train, y_test = train_test_split(X_dataFrame, Y_dataFrame, test_size=0.2, random_state=3)
svm_model = SVC(kernel="linear")  # Creating the SVM Model and setting the kernel as linear
svm_model.fit(X_train, y_train)  # Training the model
y_predict = svm_model.predict(X_test)  # Testing the model on the unseen data( i.e Test dataset)
accuracy = round(svm_model.score(X_test, y_test) * 100, 2)  # Finding the accuracy of model on Unseen data( Test data)
print("The Accuracy of the model using SVM Linear Algorithm is", accuracy)  # Printing the accuracy of model
# The SVM linear algorithm is better than Naive bayes algorithm.
# One of the reason is the naive assumption of independence between the features.
# Other reason is the because of the small dataset.
# SVM Linear kernel is beating the Naive bayes. Whereas the Naive bayes is beating other SVM kernels(i.e poly,rbf,sigmoid)
