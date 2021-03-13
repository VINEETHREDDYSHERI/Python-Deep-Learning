import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.model_selection import train_test_split

# Loading the data
dataset = pd.read_csv("diabetes.csv", header=None).values

# Splitting the dataset into the Training and Testing
X_train, X_test, Y_train, Y_test = train_test_split(dataset[:, 0:8], dataset[:, 8], test_size=0.25, random_state=87)

np.random.seed(155)
model = Sequential()  # Creating the model
model.add(Dense(20, input_dim=8, activation='relu'))  # Input Layer with 8 nodes and 1st Hidden layer with 20 nodes
model.add(Dense(40, activation='relu'))  # 2nd Hidden layer with 40 nodes
model.add(Dense(20, activation='relu'))  # 3rd Hidden layer with 20 nodes
model.add(Dense(1, activation='sigmoid'))  # Output layer
# Loss function used is binary_crossentropy, Optimizer is Adam and model metric is Accuracy
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
fit = model.fit(X_train, Y_train, epochs=100)  # Training the model for 100 epochs

print(model.summary())  # Model summary includes No.of layers and No.of weights in each layer etc
print(model.evaluate(X_test, Y_test))  # Loss and Accuracy on test dataset
# The accuracy of Model is 71% which is 2% more than UseCase model
