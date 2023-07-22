# Linear Regression Example

## Introduction

This lab demonstrates how to use linear regression to draw a straight line that best fits a dataset and how to calculate the coefficients, residual sum of squares, and coefficient of determination. We will be using the scikit-learn library to perform linear regression on the diabetes dataset.

## Steps

### Step 1: Load the Diabetes Dataset

We start by loading the diabetes dataset from scikit-learn and only selecting one feature from the dataset.

```python
import numpy as np
from sklearn import datasets

# Load the diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Use only one feature
diabetes_X = diabetes_X[:, np.newaxis, 2]
```

### Step 2: Split the Dataset

Next, we split the dataset into training and testing sets. We will use 80% of the data for training and 20% for testing.

```python
# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```

### Step 3: Train the Model

Now, we create a linear regression object and train the model using the training sets.

```python
from sklearn import linear_model

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)
```

### Step 4: Make Predictions

We can now use the trained model to make predictions on the testing set.

```python
# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)
```

### Step 5: Calculate Metrics

We can calculate the coefficients, mean squared error, and coefficient of determination.

```python
from sklearn.metrics import mean_squared_error, r2_score

# The coefficients
print("Coefficients: \n", regr.coef_)

# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))

# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f"
      % r2_score(diabetes_y_test, diabetes_y_pred))
```

### Step 6: Visualize the Results

Finally, we can plot the predicted values against the actual values to visualize how well the model fits the data.

```python
import matplotlib.pyplot as plt

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
```

## Summary

In this lab, we learned how to use linear regression to fit a straight line to a dataset and how to calculate the coefficients, residual sum of squares, and coefficient of determination. We also learned how to visualize the predicted values against the actual values using a scatter plot.
