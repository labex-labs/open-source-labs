# Recursive Feature Elimination

## Introduction

In this lab, we will learn how to use Recursive Feature Elimination (RFE) for feature selection. We will be using the Scikit-Learn library in Python to perform this task. Feature selection is an important step in machine learning to improve model performance by removing irrelevant or redundant features.

## Steps

### Step 1: Load the Dataset and Split the Data

First, we will load the digits dataset using the Scikit-Learn library. This dataset consists of 8x8 images of digits from 0 to 9. Each image is represented as an array of 64 features. We will split the data into features and target variables.

```python
from sklearn.datasets import load_digits
digits = load_digits()
X = digits.images.reshape((len(digits.images), -1))
y = digits.target
```

### Step 2: Create the RFE Object and Fit the Data

Next, we will create an object of the RFE class and fit the data to it. We will use a Support Vector Classifier (SVC) with a linear kernel as the estimator. We will select one feature at a time and take one step at a time.

```python
from sklearn.svm import SVC
from sklearn.feature_selection import RFE

svc = SVC(kernel="linear", C=1)
rfe = RFE(estimator=svc, n_features_to_select=1, step=1)
rfe.fit(X, y)
```

### Step 3: Rank the Features

After fitting the data to the RFE object, we can rank the features based on their importance. We will use the `ranking_` attribute of the RFE object to get the feature rankings. We will also reshape the rankings to match the shape of the original images.

```python
ranking = rfe.ranking_.reshape(digits.images[0].shape)
```

### Step 4: Visualize the Feature Rankings

Finally, we will plot the feature rankings using the Matplotlib library. We will use the `matshow()` function to display the rankings as an image. We will also add a color bar and a title to the plot.

```python
import matplotlib.pyplot as plt

plt.matshow(ranking, cmap=plt.cm.Blues)
plt.colorbar()
plt.title("Ranking of pixels with RFE")
plt.show()
```

## Summary

In this lab, we learned how to use Recursive Feature Elimination (RFE) for feature selection. We used the Scikit-Learn library in Python to load the digits dataset, create an RFE object, fit the data, rank the features, and visualize the feature rankings.
