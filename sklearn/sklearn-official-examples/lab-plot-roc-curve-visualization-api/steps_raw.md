# Scikit-Learn Visualization API Tutorial

## Introduction

Scikit-learn is a popular Python library that provides a simple and efficient API for machine learning tasks. One of the key features of scikit-learn is its built-in visualization API, which makes it easy to generate visualizations for machine learning models. In this lab, we will explore how to use the scikit-learn visualization API to compare ROC curves for two different classifiers.

## Steps

### Step 1: Load Data and Train a SVC

We will start by loading the wine dataset and converting it to a binary classification problem. Then, we will train a support vector classifier on the training dataset.

```python
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import RocCurveDisplay
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

X, y = load_wine(return_X_y=True)
y = y == 2

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
svc = SVC(random_state=42)
svc.fit(X_train, y_train)
```

### Step 2: Plot the ROC Curve

Next, we will plot the ROC curve using the `RocCurveDisplay.from_estimator` function. This function takes the trained classifier, the test dataset, and the true labels as inputs, and returns an object that can be used to plot the ROC curve. We will then call the `show()` method to display the plot.

```python
svc_disp = RocCurveDisplay.from_estimator(svc, X_test, y_test)
svc_disp.show()
```

### Step 3: Train a Random Forest and Plot the ROC Curve

In this step, we will train a random forest classifier and plot its ROC curve alongside the SVC ROC curve. To do this, we will create a new `RandomForestClassifier` object, fit it to the training data, and then create a new `RocCurveDisplay` object using this classifier. We will also pass the `ax` parameter to this function to plot the curves on the same axis. Finally, we will call the `plot()` method of the `svc_disp` object to plot the SVC ROC curve.

```python
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=10, random_state=42)
rfc.fit(X_train, y_train)

ax = plt.gca()
rfc_disp = RocCurveDisplay.from_estimator(rfc, X_test, y_test, ax=ax, alpha=0.8)
svc_disp.plot(ax=ax, alpha=0.8)
plt.show()
```

## Summary

In this lab, we explored how to use the scikit-learn visualization API to plot ROC curves for two different classifiers. We started by loading the wine dataset and training a support vector classifier on the training data. We then plotted the ROC curve for this classifier using the `RocCurveDisplay` function. Finally, we trained a random forest classifier and plotted its ROC curve alongside the SVC ROC curve. The scikit-learn visualization API makes it easy to compare different classifiers and visualize their performance.
