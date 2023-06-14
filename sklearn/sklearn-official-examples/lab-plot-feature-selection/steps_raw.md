# Univariate Feature Selection

## Introduction

This lab demonstrates how to use univariate feature selection to improve classification accuracy on a noisy dataset. Support vector machine (SVM) is used to classify the dataset both before and after applying univariate feature selection. For each feature, we plot the p-values for the univariate feature selection and the corresponding weights of SVMs. With this, we will compare model accuracy and examine the impact of univariate feature selection on model weights.

## Steps

### Step 1: Generate Sample Data

First, we will generate some sample data for the demonstration. We will use the iris dataset and add some noisy data to it that is not correlated.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# The iris dataset
X, y = load_iris(return_X_y=True)

# Some noisy data not correlated
E = np.random.RandomState(42).uniform(0, 0.1, size=(X.shape[0], 20))

# Add the noisy data to the informative features
X = np.hstack((X, E))

# Split dataset to select feature and evaluate the classifier
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
```

### Step 2: Univariate Feature Selection

Next, we will perform univariate feature selection with F-test for feature scoring. We will use the default selection function to select the four most significant features.

```python
from sklearn.feature_selection import SelectKBest, f_classif

selector = SelectKBest(f_classif, k=4)
selector.fit(X_train, y_train)
scores = -np.log10(selector.pvalues_)
scores /= scores.max()
```

### Step 3: Plot Feature Univariate Score

We can plot the univariate scores for each feature to see which features are significant.

```python
import matplotlib.pyplot as plt

X_indices = np.arange(X.shape[-1])
plt.figure(1)
plt.clf()
plt.bar(X_indices - 0.05, scores, width=0.2)
plt.title("Feature univariate score")
plt.xlabel("Feature number")
plt.ylabel(r"Univariate score ($-Log(p_{value})$)")
plt.show()
```

### Step 4: Compare with SVMs

We will now compare the SVM classification accuracy with and without univariate feature selection.

#### Without Univariate Feature Selection

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import LinearSVC

clf = make_pipeline(MinMaxScaler(), LinearSVC(dual="auto"))
clf.fit(X_train, y_train)
print(
    "Classification accuracy without selecting features: {:.3f}".format(
        clf.score(X_test, y_test)
    )
)

svm_weights = np.abs(clf[-1].coef_).sum(axis=0)
svm_weights /= svm_weights.sum()
```

#### After Univariate Feature Selection

```python
clf_selected = make_pipeline(
    SelectKBest(f_classif, k=4), MinMaxScaler(), LinearSVC(dual="auto")
)
clf_selected.fit(X_train, y_train)
print(
    "Classification accuracy after univariate feature selection: {:.3f}".format(
        clf_selected.score(X_test, y_test)
    )
)

svm_weights_selected = np.abs(clf_selected[-1].coef_).sum(axis=0)
svm_weights_selected /= svm_weights_selected.sum()
```

### Step 5: Plot Comparing Feature Selection

We can plot the feature scores and weights for each feature to see the impact of univariate feature selection.

```python
plt.bar(
    X_indices - 0.45, scores, width=0.2, label=r"Univariate score ($-Log(p_{value})$)"
)

plt.bar(X_indices - 0.25, svm_weights, width=0.2, label="SVM weight")

plt.bar(
    X_indices[selector.get_support()] - 0.05,
    svm_weights_selected,
    width=0.2,
    label="SVM weights after selection",
)

plt.title("Comparing feature selection")
plt.xlabel("Feature number")
plt.yticks(())
plt.axis("tight")
plt.legend(loc="upper right")
plt.show()
```

## Summary

This lab demonstrated how to use univariate feature selection to improve classification accuracy on a noisy dataset. We generated sample data, performed univariate feature selection, and compared SVM classification accuracy with and without univariate feature selection. We also plotted the feature scores and weights for each feature to see the impact of univariate feature selection.
