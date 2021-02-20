import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error

# Reading the data1.csv file
dataFrame = pd.read_csv('data1.csv')

# Checking the skew and plotting the histogram
print("Skew is:", dataFrame.revenue.skew())
plt.hist(dataFrame.revenue, color='blue')  # Plotting histogram
plt.title("Revenue Right Skewness")
plt.show()

# Revenue has Positive skew so applying log on the revenue and plotting the histogram
dataFrame.revenue = np.log(dataFrame.revenue)
plt.hist(dataFrame.revenue, color='blue')  # Plotting histogram
plt.title("Revenue No Skewness")
plt.show()

# Converting the categorical data into the numerical data.
labelEncoder = LabelEncoder()
dataFrame["City Group"] = labelEncoder.fit_transform(dataFrame["City Group"])
dataFrame["Type"] = labelEncoder.fit_transform(dataFrame["Type"])

dataFrame_Y = dataFrame.revenue  # Creating the target dataFrame
dataFrame_X = dataFrame.drop(["revenue"], axis=1)  # Dropping the target column in the Training dataframe

# Splitting the dataset into the Training and Testing
X_train, X_test, y_train, y_test = train_test_split(dataFrame_X, dataFrame_Y, random_state=2, test_size=.20)

linearModel = LinearRegression()  # Creating the Linear Regression Model
linearModel.fit(X_train, y_train)  # Training the model
y_hat = linearModel.predict(X_test)  # Testing the model on the unseen data( i.e Test dataset)
# R2 score is negative which indicates that the regression model bad.
print("R2 Score is: ", linearModel.score(X_test, y_test))
print("RMSE is: ", mean_squared_error(y_test, y_hat))  # The error is also very high

# Plotting the scatter plot between the actual and predicted values
plt.scatter(y_hat, y_test, alpha=.75, color='b')
plt.xlabel('Predicted Price')
plt.ylabel('Actual Price')
plt.title('Linear Regression Model Prediction')
plt.show()