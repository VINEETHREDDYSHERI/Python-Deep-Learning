import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# Breast Cancer Model
# Loading the data
dataFrame = pd.read_csv("Breas Cancer.csv", header=0)
print(dataFrame.isnull().sum())  # Count of Null values in each feature
# "Unnamed: 32" contains only Null values. So dropping the column.
dataFrame = dataFrame.iloc[:, :32]

# Converting the categorical data into the numerical data.
labelEncoder = LabelEncoder()
target = labelEncoder.fit_transform(dataFrame["diagnosis"])  # Target dataFrame after converting to numerical format
# Dropping the target column and "id" feature in the Training dataframe
dataFrame = dataFrame.drop(["diagnosis", "id"], axis=1)

Scaler = StandardScaler()  # Creating the StandardScaler model
Scaler.fit(dataFrame)  # Fitting the data to the model
dataFrame_scaled_array = Scaler.transform(dataFrame)  # Transforming the data.

# Splitting the dataset into the Training and Testing
X_train, X_test, Y_train, Y_test = train_test_split(dataFrame_scaled_array, target, test_size=0.25, random_state=87)

np.random.seed(155)
model = Sequential()  # Creating the model
model.add(Dense(20, input_dim=30, activation='relu'))  # Input Layer with 8 nodes and 1st Hidden layer with 20 nodes
model.add(Dense(32, activation='relu'))  # 2nd Hidden layer with 32 nodes
model.add(Dense(1, activation='sigmoid'))  # Output layer
# Loss function used is binary_crossentropy, Optimizer is Adam and model metric is Accuracy
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
fit = model.fit(X_train, Y_train, epochs=100)  # Training the model for 100 epochs

print(model.summary())  # Model summary includes No.of layers and No.of weights in each layer etc
print(model.evaluate(X_test, Y_test))  # Loss and Accuracy on test dataset
# The accuracy is 96% which is 14% greater than previous model
