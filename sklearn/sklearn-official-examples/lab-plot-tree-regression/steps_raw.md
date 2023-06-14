# Decision Tree Regression

## Introduction

In this lab, we will learn how to use the decision tree regression algorithm to fit a sine curve with additional noisy observation. The decision trees will be used to learn local linear regressions approximating the sine curve. We will see that if the maximum depth of the tree is set too high, the decision trees learn too fine details of the training data and learn from the noise, i.e. they overfit.

## Steps

### Step 1: Import necessary libraries

We will import the necessary libraries and modules, including numpy, matplotlib, and DecisionTreeRegressor.

```python
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
```

### Step 2: Create a random dataset

We will create a random dataset using NumPy and add some noise to it.

```python
rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))
```

### Step 3: Fit regression model

We will fit regression models with two different maximum depths: 2 and 5.

```python
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_1.fit(X, y)
regr_2.fit(X, y)
```

### Step 4: Predict

We will use the models to make predictions on a range of values from 0 to 5.

```python
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)
```

### Step 5: Plot the results

We will plot the results to visualize how the models fit the data.

```python
plt.figure()
plt.scatter(X, y, s=20, edgecolor="black", c="darkorange", label="data")
plt.plot(X_test, y_1, color="cornflowerblue", label="max_depth=2", linewidth=2)
plt.plot(X_test, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()
```

## Summary

In this lab, we learned how to use the decision tree regression algorithm to fit a sine curve with additional noisy observation. We saw that if the maximum depth of the tree is set too high, the decision trees learn too fine details of the training data and learn from the noise, i.e. they overfit. We also learned how to plot the results to visualize how the models fit the data.
