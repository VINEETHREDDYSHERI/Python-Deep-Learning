# importing the pandas package and plt, seaborn for visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train_dataFrame = pd.read_csv("train.csv")  # Loading the train.csv file data using pandas
# Finding the correlation between the Sex Feature and Survived target variable.
corr = train_dataFrame[["Survived", "Sex"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False)
print(corr)  # Printing the Correlation
# The survival rate of Female is very higher when compared to Male.
# So these feature plays a very important role. Hence we will keep the feature.
# Plotting the plot using the FacetGrid of seaborn library between Sex and Survived
g = sns.FacetGrid(train_dataFrame, col="Sex", row="Survived", margin_titles=True)
g.map(plt.hist, "Age", color="purple")  # Plotting Against the age.
plt.show()  # Showing the plot
# From the plot it is very clear that most of the men will not survive.
