from keras import Sequential
from keras.datasets import mnist
import numpy as np
from keras.layers import Dense
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.shape[1:])  # Shape of the image
# Converting image of shape 28*28 to 784 dimensional
dimData = np.prod(train_images.shape[1:])
print(dimData)
train_data = train_images.reshape(train_images.shape[0], dimData)
test_data = test_images.reshape(test_images.shape[0], dimData)

# Converting the data to float datatype
train_data = train_data.astype('float')
test_data = test_data.astype('float')
# Scaling the data
train_data /= 255.0
test_data /= 255.0
# Converting the labels from integer to one-hot encoding. to_categorical is doing the same thing as LabelEncoder()
train_labels_one_hot = to_categorical(train_labels)
test_labels_one_hot = to_categorical(test_labels)

# Defining the Neural network Model
model = Sequential()  # Creating the model
# Input Layer with 748 nodes and 1st Hidden layer with 512 nodes
model.add(Dense(512, activation='relu', input_shape=(dimData,)))
model.add(Dense(512, activation='relu'))  # 2nd Hidden layer with 512 nodes
model.add(Dense(10, activation='softmax'))  # Output layer with 10 nodes and a softmax activation function
# Loss function used is categorical_crossentropy, Optimizer is rmsprop and model metric is Accuracy
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
# Training the model for 10 epochs with 256 images at each iteration within a epoch
history = model.fit(train_data, train_labels_one_hot, batch_size=256, epochs=10, verbose=1,
                    validation_data=(test_data, test_labels_one_hot))
# The model accuracy after tenth epoch on validation data is 98.29% and loss is 0.0898

# Plotting the first image in the test dataset
plt.imshow(test_images[0])
plt.title("First image from test data")
plt.show()

# Predicting the first image
pred = model.predict(test_data[0].reshape(1, 784))
print("Model prediction for the Test image :", pred.argmax())
# The model prediction is 7 which correctly classified the image. The model is performing good.

