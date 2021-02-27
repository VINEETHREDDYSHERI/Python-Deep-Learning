import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
pd.options.mode.chained_assignment = None

# Loading the data into pandas dataframe
dataFrame = pd.read_csv('data.csv')
print("Number of rows: ", dataFrame.shape[0])

# Removing the Outliers using InterQuartile range method
sns.boxplot(x=dataFrame.GarageArea)  # Boxplot using the seaborn
plt.title("GarageArea BoxPlot")
plt.show()  # To show the above plot
# All the points above 938.25 are Outliers.
Q1 = dataFrame.GarageArea.quantile(0.25)  # 1st Quartile
Q3 = dataFrame.GarageArea.quantile(0.75)  # 3rd Quartile
IQR = Q3 - Q1  # InterQuartile range
# Excluding the outliers which are not in the range -27.75 and 938.25
dataFrameIQR = dataFrame[dataFrame["GarageArea"] > (Q1 - 1.5 * IQR)]
dataFrameIQR = dataFrame[dataFrame["GarageArea"] < (Q3 + 1.5 * IQR)]
print("Number of rows after removing the outliers using InterQuartile range method: ", dataFrameIQR.shape[0])  # 21 outliers
# Plotting the scatter plot
plt.scatter(dataFrame.GarageArea, dataFrame.SalePrice)
plt.title('GarageArea Vs SalePrice with Outliers')
plt.show()
plt.scatter(dataFrameIQR.GarageArea, dataFrameIQR.SalePrice)
plt.title('GarageArea Vs SalePrice by InterQuartile Range method')
plt.show()

# Removing the Outliers using Z-Score method
dataFrame["zscore"] = stats.zscore(dataFrame.GarageArea)  # Calculating the Zscore
# Excluding the outliers which are not in the range -3 and 3.
dataFrameZScore = dataFrame[dataFrame["zscore"].abs() < 3]
dataFrameZScore.drop("zscore", axis=1, inplace=True)
print("Number of rows after removing the outliers using Zscore method: ", dataFrameZScore.shape[0])  # 7 outliers
# Plotting the scatter plot
plt.scatter(dataFrameZScore.GarageArea, dataFrameZScore.SalePrice)
plt.title('GarageArea Vs SalePrice by Z-Score method')
plt.show()
