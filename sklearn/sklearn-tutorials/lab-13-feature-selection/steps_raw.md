# Feature Selection

## Introduction

Feature selection is an important step in machine learning. It involves selecting the most relevant features from a dataset to improve the accuracy and performance of the model. In scikit-learn, the `sklearn.feature_selection` module provides various methods for feature selection and dimensionality reduction.

This lab will guide you through the process of feature selection using scikit-learn. We will cover techniques such as removing features with low variance, univariate feature selection, recursive feature elimination, and feature selection using SelectFromModel.

## Steps

### Step 1: Removing features with low variance

The `VarianceThreshold` class in scikit-learn can be used to remove features with low variance. Features with low variance typically do not provide much information for the model. We will demonstrate how to use `VarianceThreshold` to remove zero-variance features.

```python
from sklearn.feature_selection import VarianceThreshold

X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]

# Initialize VarianceThreshold with a threshold of 80% variability
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))

# Select features with high variability
X_selected = sel.fit_transform(X)

print("Original X shape:", X.shape)
print("X with selected features shape:", X_selected.shape)
print("Selected features:", sel.get_support(indices=True))
```

This code snippet demonstrates how to use `VarianceThreshold` to remove zero-variance features from a dataset. The output will show the original shape of the dataset and the shape after selecting features with high variability.

### Step 2: Univariate feature selection

Univariate feature selection works by selecting the best features based on univariate statistical tests. In scikit-learn, there are several classes that implement univariate feature selection:

- `SelectKBest`: selects the top k highest scoring features
- `SelectPercentile`: selects a user-specified percentage of highest scoring features
- `SelectFpr`: selects features based on the false positive rate
- `SelectFdr`: selects features based on the false discovery rate
- `SelectFwe`: selects features based on family wise error
- `GenericUnivariateSelect`: allows selection with a configurable strategy

Here is an example of using `SelectKBest` to select the two best features from the Iris dataset:

```python
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

# Load the Iris dataset
X, y = load_iris(return_X_y=True)

# Initialize SelectKBest with the f_classif scoring function and k=2
selector = SelectKBest(f_classif, k=2)

# Select the best features
X_selected = selector.fit_transform(X, y)

print("Original X shape:", X.shape)
print("X with selected features shape:", X_selected.shape)
print("Selected features:", selector.get_support(indices=True))
```

In this example, we use the `f_classif` scoring function and select the two best features from the Iris dataset. The output will show the original shape of the dataset and the shape after selecting the best features.

### Step 3: Recursive feature elimination

Recursive feature elimination (RFE) is a feature selection method that recursively considers smaller and smaller sets of features to select the most important ones. It works by training an external estimator with weights assigned to features and pruning the least important features.

```python
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.feature_selection import RFE

# Load the Iris dataset
X, y = load_iris(return_X_y=True)

# Initialize SVC as the external estimator
estimator = SVC(kernel="linear")

# Initialize RFE with the external estimator and select 2 features
selector = RFE(estimator, n_features_to_select=2)

# Select the best features
X_selected = selector.fit_transform(X, y)

print("Original X shape:", X.shape)
print("X with selected features shape:", X_selected.shape)
print("Selected features:", selector.get_support(indices=True))
```

In this example, we use a Support Vector Classifier (SVC) as the external estimator and select the two best features from the Iris dataset. The output will show the original shape of the dataset and the shape after selecting the best features.

### Step 4: Feature selection using SelectFromModel

The `SelectFromModel` class is a meta-transformer that can be used with any estimator that assigns importance to each feature. It selects features based on their importance and removes features below a specified threshold.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel

# Load the Iris dataset
X, y = load_iris(return_X_y=True)

# Initialize RandomForestClassifier as the estimator
estimator = RandomForestClassifier()

# Initialize SelectFromModel with the estimator and threshold of "mean"
selector = SelectFromModel(estimator, threshold="mean")

# Select the best features
X_selected = selector.fit_transform(X, y)

print("Original X shape:", X.shape)
print("X with selected features shape:", X_selected.shape)
print("Selected features:", selector.get_support(indices=True))
```

In this example, we use a Random Forest Classifier as the estimator and select features with an importance greater than the mean importance. The output will show the original shape of the dataset and the shape after selecting the best features.

## Summary

Feature selection is an essential step in machine learning to improve the accuracy and performance of models. In this lab, we covered various techniques such as removing features with low variance, univariate feature selection, recursive feature elimination, and feature selection using SelectFromModel. These techniques help in selecting the most relevant features and reducing the dimensionality of the dataset, resulting in improved model performance.
