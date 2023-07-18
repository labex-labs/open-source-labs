# Comparison of F-test and Mutual Information

## Introduction

In this lab, we will learn about the differences between univariate F-test statistics and mutual information. We will use scikit-learn library to perform F-test and mutual information regression on a dataset and compare the results.

## Steps

### Step 1: Import libraries

We will start by importing the necessary libraries for this lab. We will use numpy, matplotlib and scikit-learn for this lab.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_selection import f_regression, mutual_info_regression
```

### Step 2: Create dataset

We will create a dataset with 3 features, where the first feature has a linear relationship with the target, the second feature has a non-linear relationship with the target, and the third feature is completely irrelevant. We will create 1000 samples for this dataset.

```python
np.random.seed(0)
X = np.random.rand(1000, 3)
y = X[:, 0] + np.sin(6 * np.pi * X[:, 1]) + 0.1 * np.random.randn(1000)
```

### Step 3: Calculate F-test

We will now calculate the F-test score for each feature. F-test captures only linear dependency between variables. We will normalize the F-test scores by dividing them by the maximum F-test score.

```python
f_test, _ = f_regression(X, y)
f_test /= np.max(f_test)
```

### Step 4: Calculate mutual information

We will now calculate the mutual information score for each feature. Mutual information can capture any kind of dependency between variables. We will normalize the mutual information scores by dividing them by the maximum mutual information score.

```python
mi = mutual_info_regression(X, y)
mi /= np.max(mi)
```

### Step 5: Plot the results

We will now plot the dependency of the target against each feature and the F-test and mutual information scores for each feature.

```python
plt.figure(figsize=(15, 5))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.scatter(X[:, i], y, edgecolor="black", s=20)
    plt.xlabel("$x_{}$".format(i + 1), fontsize=14)
    if i == 0:
        plt.ylabel("$y$", fontsize=14)
    plt.title("F-test={:.2f}, MI={:.2f}".format(f_test[i], mi[i]), fontsize=16)
plt.show()
```

## Summary

In this lab, we learned about the differences between univariate F-test statistics and mutual information. We performed F-test and mutual information regression on a dataset and compared the results. We found that F-test captures only linear dependency between variables while mutual information can capture any kind of dependency between variables.
