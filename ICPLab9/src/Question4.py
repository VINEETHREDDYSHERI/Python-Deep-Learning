from keras import Sequential
from keras.datasets import mnist
import numpy as np
from keras.layers import Dense
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

# Loading the training and test dataset.
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
# The model accuracy after tenth epoch on validation data is 96% and loss is 0.4321
# The model is performing somewhat poor than the same model with scaled data
# Plotting the graph of training and validation phase accuracy with No.of epochs
plt.plot(history.history['accuracy'])  # Accuracy of training phase
plt.plot(history.history['val_accuracy'])  # Accuracy of Validation phase
plt.title('Model accuracy at each epoch')  # Plot tile
plt.ylabel('Accuracy')  # Y-axis label
plt.xlabel('No.of epochs')  # X-axis label
plt.legend(['train', 'val'], loc='upper left')
plt.show()  # Showing the plot

# Plotting the graph of training and validation phase Loss value with No.of epochs
plt.plot(history.history['loss'])  # Loss value of training phase
plt.plot(history.history['val_loss'])  # Loss value of Validation phase
plt.title('Model loss Value at each epoch')  # Plot tile
plt.ylabel('Loss')  # Y-axis label
plt.xlabel('No.of epochs')  # X-axis label
plt.legend(['train', 'val'], loc='upper left')
plt.show()  # Showing the plot
# The Model accuracy and loss function is different at each epoch when compared to previous model
