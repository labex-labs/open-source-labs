# Ordinary Least Squares and Ridge Regression Variance

## Introduction

In this lab, we will use Python scikit-learn library to explore the difference between Ordinary Least Squares (OLS) and Ridge Regression. We will examine how these two methods of linear regression cope with noise in the data, and how they differ in their predictions.

## Steps

### Step 1: Import Libraries

In this step, we will import the necessary Python libraries.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
```

### Step 2: Create Data

In this step, we will create the data that we will use for our analysis.

```python
X_train = np.c_[0.5, 1].T
y_train = [0.5, 1]
X_test = np.c_[0, 2].T
```

### Step 3: Define Classifiers

In this step, we will define the OLS and Ridge Regression classifiers.

```python
classifiers = dict(
    ols=linear_model.LinearRegression(), ridge=linear_model.Ridge(alpha=0.1)
)
```

### Step 4: Visualize the Results

In this step, we will visualize the results of our analysis.

```python
for name, clf in classifiers.items():
    fig, ax = plt.subplots(figsize=(4, 3))

    for _ in range(6):
        this_X = 0.1 * np.random.normal(size=(2, 1)) + X_train
        clf.fit(this_X, y_train)

        ax.plot(X_test, clf.predict(X_test), color="gray")
        ax.scatter(this_X, y_train, s=3, c="gray", marker="o", zorder=10)

    clf.fit(X_train, y_train)
    ax.plot(X_test, clf.predict(X_test), linewidth=2, color="blue")
    ax.scatter(X_train, y_train, s=30, c="red", marker="+", zorder=10)

    ax.set_title(name)
    ax.set_xlim(0, 2)
    ax.set_ylim((0, 1.6))
    ax.set_xlabel("X")
    ax.set_ylabel("y")

    fig.tight_layout()

plt.show()
```

## Summary

In this lab, we learned how to use Python scikit-learn library to explore the difference between Ordinary Least Squares (OLS) and Ridge Regression. We saw how these two methods of linear regression cope with noise in the data, and how they differ in their predictions. We also visualized the results of our analysis.
