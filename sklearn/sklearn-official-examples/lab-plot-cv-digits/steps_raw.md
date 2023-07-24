# Cross-validation on Digits Dataset

## Introduction

This lab uses cross-validation with a support vector machine (SVM) on the digits dataset. This is a classification problem, where the task is to identify digits from images of handwritten digits.

## Steps

### Step 1: Load the dataset

First, we need to load the digits dataset from scikit-learn and split it into features and labels.

```python
import numpy as np
from sklearn import datasets

X, y = datasets.load_digits(return_X_y=True)
```

### Step 2: Create a Support Vector Machine (SVM) model

Next, we create an SVM model with a linear kernel.

```python
from sklearn import svm

svc = svm.SVC(kernel="linear")
```

### Step 3: Define the hyperparameter values to test

We will test different values of the regularization parameter C, which controls the trade-off between maximizing the margin and minimizing the classification error. We will test 10 logarithmically-spaced values between 10^-10 and 1.

```python
C_s = np.logspace(-10, 0, 10)
```

### Step 4: Perform cross-validation and record results

For each value of C, we perform 10-fold cross-validation and record the mean and standard deviation of the scores.

```python
from sklearn.model_selection import cross_val_score

scores = list()
scores_std = list()
for C in C_s:
    svc.C = C
    this_scores = cross_val_score(svc, X, y, n_jobs=1)
    scores.append(np.mean(this_scores))
    scores_std.append(np.std(this_scores))
```

### Step 5: Plot the results

Finally, we plot the mean scores as a function of C, and also include error bars to visualize the standard deviation.

```python
import matplotlib.pyplot as plt

plt.figure()
plt.semilogx(C_s, scores)
plt.semilogx(C_s, np.array(scores) + np.array(scores_std), "b--")
plt.semilogx(C_s, np.array(scores) - np.array(scores_std), "b--")
locs, labels = plt.yticks()
plt.yticks(locs, list(map(lambda x: "%g" % x, locs)))
plt.ylabel("CV score")
plt.xlabel("Parameter C")
plt.ylim(0, 1.1)
plt.show()
```

## Summary

In this lab, we performed 10-fold cross-validation with an SVM model on the digits dataset, testing different values of the regularization parameter C. We plotted the results to visualize the relationship between C and the mean cross-validation score. This is a useful technique for tuning hyperparameters and assessing model performance.
