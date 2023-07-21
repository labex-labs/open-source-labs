# Cross Decomposition

## Introduction

The `cross_decomposition` module in scikit-learn contains supervised estimators for dimensionality reduction and regression, specifically for Partial Least Squares (PLS) algorithms. These algorithms find the fundamental relationship between two matrices by projecting them into a lower-dimensional subspace such that the covariance between the transformed matrices is maximal.

In this lab, we will explore the different cross decomposition algorithms provided by scikit-learn and learn how to use them for dimensionality reduction and regression tasks.

## Steps

### Step 1: Import the necessary libraries

Let's start by importing the necessary libraries for this lab.

```python
import numpy as np
from sklearn.cross_decomposition import PLSRegression, PLSCanonical, CCA, PLSSVD
```

### Step 2: Load the dataset

Next, we'll load a sample dataset to demonstrate the cross decomposition algorithms. For simplicity, we'll create two matrices `X` and `Y` with random values.

```python
np.random.seed(0)
X = np.random.random((100, 5))
Y = np.random.random((100, 3))
```

### Step 3: PLSRegression

#### Fit the PLSRegression model

We'll start with the `PLSRegression` algorithm, which is a form of regularized linear regression. We'll fit the model to our data.

```python
pls = PLSRegression(n_components=2)
pls.fit(X, Y)
```

#### Transform the data

We can transform the original data using the fitted model. The transformed data will have reduced dimensions.

```python
X_transformed = pls.transform(X)
Y_transformed = pls.transform(Y)
```

### Step 4: PLSCanonical

#### Fit the PLSCanonical model

Next, we'll use the `PLSCanonical` algorithm, which finds the canonical correlation between two matrices. This algorithm is useful when there is multicollinearity among the features.

```python
plsc = PLSCanonical(n_components=2)
plsc.fit(X, Y)
```

#### Transform the data

We can transform the original data using the fitted model. The transformed data will have reduced dimensions.

```python
X_transformed = plsc.transform(X)
Y_transformed = plsc.transform(Y)
```

### Step 5: CCA

#### Fit the CCA model

The `CCA` algorithm is a special case of PLS and stands for Canonical Correlation Analysis. It finds the correlation between two sets of variables.

```python
cca = CCA(n_components=2)
cca.fit(X, Y)
```

#### Transform the data

We can transform the original data using the fitted model. The transformed data will have reduced dimensions.

```python
X_transformed = cca.transform(X)
Y_transformed = cca.transform(Y)
```

### Step 6: PLSSVD

#### Fit the PLSSVD model

The `PLSSVD` algorithm is a simplified version of `PLSCanonical` that computes the Singular Value Decomposition (SVD) of the cross-covariance matrix only once. This algorithm is useful when the number of components is limited to one.

```python
plssvd = PLSSVD(n_components=1)
plssvd.fit(X, Y)
```

#### Transform the data

We can transform the original data using the fitted model. The transformed data will have reduced dimensions.

```python
X_transformed = plssvd.transform(X)
Y_transformed = plssvd.transform(Y)
```

## Summary

In this lab, we explored the cross decomposition algorithms provided by scikit-learn. We learned about PLSRegression, PLSCanonical, CCA, and PLSSVD. We also saw how to fit these models to data and transform the data into lower-dimensional representations. These algorithms are useful for dimensionality reduction and regression tasks, especially when there is multicollinearity among the features or when the number of variables is greater than the number of samples.
