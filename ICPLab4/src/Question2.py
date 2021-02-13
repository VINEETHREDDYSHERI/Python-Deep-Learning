# importing the pandas and packages from sklearn to split the data, Naive Bayes algorithm and metrics
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

dataFrame = pd.read_csv("glass.csv")  # Loading the train.csv file data using pandas
Y_dataFrame = dataFrame['Type']  # Creating the target dataFrame
X_dataFrame = dataFrame.drop('Type', axis=1)  # Dropping the target column in the Training dataframe
# Splitting the dataset into the Training and Testing
X_train, X_test, Y_train, Y_test = train_test_split(X_dataFrame, Y_dataFrame, test_size=0.2, random_state=3)
naive_model = GaussianNB()  # Creating the Naive Bayes Model
naive_model.fit(X_train, Y_train)  # Training the model
y_predict = naive_model.predict(X_test)  # Testing the model on the unseen data( i.e Test dataset)
accuracy = round(naive_model.score(X_test, Y_test) * 100, 2)  # Finding the accuracy of model on Unseen data( Test data)
print("The Accuracy of the model using Naive Bayes Algorithm is", accuracy)  # Printing the accuracy of model
print("The Classification Report using Naive Bayes Algorithm is: ")
print(classification_report(Y_test, y_predict))  # Printing the complete report
