# Diabetes Prediction using Voting Regressor

## Introduction

In this lab, we will use a Voting Regressor to predict the progression of diabetes in patients. We will use three different regressors to predict the data: Gradient Boosting Regressor, Random Forest Regressor, and Linear Regression. Then the above 3 regressors will be used for the Voting Regressor. Finally, we will plot the predictions made by all models for comparison.

We will work with the diabetes dataset which consists of 10 features collected from a cohort of diabetes patients. The target is a quantitative measure of disease progression one year after baseline.

## Steps

### Step 1: Import Libraries

Let's import the necessary libraries to perform the diabetes prediction using the Voting Regressor.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import VotingRegressor
```

### Step 2: Load the Diabetes Dataset

Next, we will load the diabetes dataset into our program using the `load_diabetes()` function provided by scikit-learn. This function returns the dataset as a tuple of two arrays - one containing the feature data and the other containing the target data. We will assign these arrays to `X` and `y`, respectively.

```python
# Load the diabetes dataset
X, y = load_diabetes(return_X_y=True)
```

### Step 3: Train the Regressors

Now, let's initiate a Gradient Boosting Regressor, a Random Forest Regressor, and a Linear Regression. Next, we will use the 3 regressors to build the Voting Regressor.

```python
# Train classifiers
reg1 = GradientBoostingRegressor(random_state=1)
reg2 = RandomForestRegressor(random_state=1)
reg3 = LinearRegression()

reg1.fit(X, y)
reg2.fit(X, y)
reg3.fit(X, y)

ereg = VotingRegressor([("gb", reg1), ("rf", reg2), ("lr", reg3)])
ereg.fit(X, y)
```

### Step 4: Making Predictions

Now we will use each of the regressors to make the 20 first predictions.

```python
# Make predictions
xt = X[:20]

pred1 = reg1.predict(xt)
pred2 = reg2.predict(xt)
pred3 = reg3.predict(xt)
pred4 = ereg.predict(xt)
```

### Step 5: Plot the Results

Finally, we will visualize the 20 predictions. The red stars show the average prediction made by Voting Regressor.

```python
# Plot the results
plt.figure()
plt.plot(pred1, "gd", label="GradientBoostingRegressor")
plt.plot(pred2, "b^", label="RandomForestRegressor")
plt.plot(pred3, "ys", label="LinearRegression")
plt.plot(pred4, "r*", ms=10, label="VotingRegressor")

plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)
plt.ylabel("predicted")
plt.xlabel("training samples")
plt.legend(loc="best")
plt.title("Regressor predictions and their average")

plt.show()
```

## Summary

In this lab, we have used the Voting Regressor to predict the progression of diabetes in patients. We have used three different regressors to predict the data: Gradient Boosting Regressor, Random Forest Regressor, and Linear Regression. We have also visualized the predictions made by all models for comparison.
