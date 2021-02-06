import numpy as np  # importing the numpy package

randomData = np.random.uniform(1, 20, 20)  # Creating the random 20 floating variables from 1 to 20
reshapedData = randomData.reshape((4, 5))  # Reshaping the data into the 4x5 Matrix
print("The random data in 4x5 matrix:\n", reshapedData)
maxValInRow = np.max(reshapedData, axis=1).reshape(-1, 1)  # Finding the max value in each row and reshaping to 4x1
finalResult = np.where(reshapedData == maxValInRow, 0, reshapedData)  # If the value is equal the replacing with 0
# else replacing with the same value
print()
print("The resultant matrix is:\n", finalResult)
