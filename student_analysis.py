import pandas as pd

df = pd.read_csv("PB_data.csv")

print(df.head(),df.shape,df.info())

print(df.isnull().sum())

print(df.describe())

import matplotlib.pyplot as plt
df.hist()
plt.show()

print(df.corr())

import seaborn as sns

sns.heatmap(df.corr(), annot=True)
plt.show()

sns.boxplot(x=df["Marks"])
plt.title("Outliers in Marks")
plt.show()

Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["Marks"] < lower) | (df["Marks"] > upper)]

print(outliers["Marks"])

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower)
print("Upper Bound:", upper)

from sklearn.model_selection import train_test_split
X = df[["Hours", "Attendance", "PreviousMarks"]]
y = df["Marks"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
# Create model
model = LinearRegression()

# Train model on training data
model.fit(X_train, y_train)

# Predict marks for test data
y_pred = model.predict(X_test)
print("Model Score:", r2_score(y_test, y_pred))

# Show predictions
print("Predicted Values:")
print(y_pred)

from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np


mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)


print("MAE:", mae)
print("MAE:", mae)
print("RMSE:", rmse)

# -------------------------------
# STEP 8 — Cross Validation
# -------------------------------
from sklearn.model_selection import cross_val_score

# Perform 5-fold cross validation
scores = cross_val_score(model, X, y, cv=5)

# Show individual scores
print("Cross Validation Scores:", scores)

# Show average score
print("Average Cross Validation Score:", scores.mean())

new_prediction = model.predict([[7, 85, 75]])
print("Predicted Marks:", new_prediction[0])
