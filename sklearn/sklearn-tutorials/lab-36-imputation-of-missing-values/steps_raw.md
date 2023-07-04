# Imputation of Missing Values

## Introduction

Many real-world datasets contain missing values, which can cause issues when using machine learning algorithms that assume complete and numerical data. In such cases, it is important to handle missing values appropriately to make the most of the available data. One common strategy is imputation, which involves filling in the missing values based on the known part of the data.

In this tutorial, we will explore different strategies for imputing missing values using scikit-learn, a popular machine learning library in Python.

## Steps

### Step 1: Import the necessary modules

First, we need to import the required modules from the scikit-learn library. We will use the `SimpleImputer` class for univariate feature imputation and the `IterativeImputer` class for multivariate feature imputation.

```python
import numpy as np
from sklearn.impute import SimpleImputer, IterativeImputer
```

### Step 2: Univariate feature imputation using SimpleImputer

The `SimpleImputer` class provides basic strategies for imputing missing values in a univariate manner. We can choose from different strategies, such as replacing missing values with a constant value or using the mean, median, or most frequent value of each column to impute the missing values.

Let's start by considering the mean strategy. We will create an instance of `SimpleImputer` and fit it on our data to learn the imputation strategy. Then, we can use the `transform` method to impute the missing values based on the learned strategy.

```python
imp = SimpleImputer(strategy='mean')
X = [[1, 2], [np.nan, 3], [7, 6]]
imp.fit(X)
X_test = [[np.nan, 2], [6, np.nan], [7, 6]]
imputed_X_test = imp.transform(X_test)
```

### Step 3: Multivariate feature imputation using IterativeImputer

The `IterativeImputer` class is a more advanced approach to imputing missing values. It models each feature with missing values as a function of other features and uses that estimate for imputation. It iteratively learns the relationships between features and imputes the missing values based on these relationships.

```python
imp = IterativeImputer()
X = [[1, 2], [3, 6], [4, 8], [np.nan, 3], [7, np.nan]]
imp.fit(X)
X_test = [[np.nan, 2], [6, np.nan], [np.nan, 6]]
imputed_X_test = imp.transform(X_test)
```

### Step 4: Nearest neighbors imputation using KNNImputer

The `KNNImputer` class provides imputation for filling in missing values using the k-Nearest Neighbors approach. It finds the nearest neighbors for each sample with missing values and imputes the missing feature values based on the values of the neighbors.

```python
from sklearn.impute import KNNImputer
nan = np.nan
X = [[1, 2, nan], [3, 4, 3], [nan, 6, 5], [8, 8, 7]]
imputer = KNNImputer(n_neighbors=2)
imputed_X = imputer.fit_transform(X)
```

### Step 5: Keeping the number of features constant

By default, scikit-learn imputers drop columns containing only missing values. However, in some cases, it is necessary to keep the empty features to maintain the shape of the data. We can achieve this by setting the `keep_empty_features` parameter to True.

```python
imputer = SimpleImputer(keep_empty_features=True)
X = np.array([[np.nan, 1], [np.nan, 2], [np.nan, 3]])
imputed_X = imputer.fit_transform(X)
```

### Step 6: Marking imputed values using MissingIndicator

The `MissingIndicator` transformer is useful for indicating the presence of missing values in a dataset. It can be used in conjunction with imputation to preserve information about which values were imputed. This transformer returns a binary matrix indicating the presence of missing values in the dataset.

```python
from sklearn.impute import MissingIndicator
X = np.array([[-1, -1, 1, 3], [4, -1, 0, -1], [8, -1, 1, 0]])
indicator = MissingIndicator()
mask_missing_values_only = indicator.fit_transform(X)
```

## Summary

In this tutorial, we learned different strategies for imputing missing values using scikit-learn. We explored univariate feature imputation with `SimpleImputer`, multivariate feature imputation with `IterativeImputer`, nearest neighbors imputation with `KNNImputer`, keeping the number of features constant, and marking imputed values with `MissingIndicator`. These techniques can be valuable tools for handling missing data and ensuring that machine learning algorithms can be applied to incomplete datasets.
