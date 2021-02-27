import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

dataFrame = pd.read_csv("CC.csv")  # Loading the data into pandas dataframe
print("No of the Null values:")
print(dataFrame.isnull().sum())  # Printing No.of null values in each column
# Replacing the null values with the mean value.
dataFrame["MINIMUM_PAYMENTS"] = dataFrame["MINIMUM_PAYMENTS"].fillna(dataFrame["MINIMUM_PAYMENTS"].mean())
dataFrame["CREDIT_LIMIT"] = dataFrame["CREDIT_LIMIT"].fillna(dataFrame["CREDIT_LIMIT"].mean())
# Printing No.of null values in each column after replacing null with mean value
print("No of the Null values after replacing null with mean value:")
print(dataFrame.isnull().sum())

SSWC = []
# CUST_ID indicates customer Id and the feature will not have any impact during clustering, so excluding it.
# Using the KMeans algorithm to cluster the given data with n_clusters ranging from 1 to 10.
for i in range(1, 10):
    KMeansModel = KMeans(n_clusters=i, random_state=0)  # Creating the KMeans Model with i no.of clusters
    KMeansModel.fit(dataFrame.iloc[:, 1:])  # Fitting the data to the model
    SSWC.append(KMeansModel.inertia_)  # appending the Sum of squares with in cluster for i

# Plotting the graph between the no.of clusters and Sum of Squares within the cluster
# This plot is called elbow plot.
# The best No.of cluster is a point at which the steep or huge decrease in Sum of Squares within the cluster stops.
plt.plot(range(1, 10), SSWC)
plt.title("Elbow Method")
plt.xlabel("No of Clusters")
plt.ylabel("Sum of Squares within the cluster")
plt.show()
# From the plot we can conclude that the best No.of cluster is 3.

KMeansModel = KMeans(n_clusters=3, random_state=0)  # Creating the KMeans Model no.of clusters as 3
KMeansModel.fit(dataFrame.iloc[:, 1:])  # Fitting the data to the model
clusters = KMeansModel.predict(dataFrame.iloc[:, 1:])  # Predicting the cluster for each sample.
# silhouette_score indicates how dense the data is with in the cluster range from -1 to 1.
print("The Silhouette score is: ", silhouette_score(dataFrame.iloc[:, 1:], clusters))
# The score is 0.466 which indicates the model is performing good.
