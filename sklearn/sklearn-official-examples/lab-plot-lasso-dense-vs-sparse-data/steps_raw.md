# Scikit-learn Lasso Regression

## Introduction

This lab demonstrates the use of Scikit-learn's Lasso regression algorithm on dense and sparse data. The Lasso algorithm is a linear regression method that adds a penalty to the regression coefficients. This penalty encourages the model to produce sparse coefficients. The Lasso algorithm is useful in situations where the number of features is large compared to the number of samples.

## Steps

### Step 1: Import Libraries

We begin by importing the necessary libraries. We need Scikit-learn, NumPy, and SciPy.

```python
from time import time
from scipy import sparse
from scipy import linalg
from sklearn.datasets import make_regression
from sklearn.linear_model import Lasso
```

### Step 2: Generate Dense Data

Next, we generate some dense data that we will use for the Lasso regression. We use Scikit-learn's `make_regression` function to generate 200 samples with 5000 features.

```python
X, y = make_regression(n_samples=200, n_features=5000, random_state=0)
```

### Step 3: Train Lasso on Dense Data

Now we train two Lasso regression models, one on the dense data and one on the sparse data. We set the alpha parameter to 1 and the maximum number of iterations to 1000.

```python
alpha = 1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
```

### Step 4: Fit Lasso to Dense Data

We fit the Lasso regression models to the dense data using Scikit-learn's `fit` function. We also time the fitting process and print the time for each Lasso model.

```python
t0 = time()
sparse_lasso.fit(X_sp, y)
print(f"Sparse Lasso done in {(time() - t0):.3f}s")

t0 = time()
dense_lasso.fit(X, y)
print(f"Dense Lasso done in {(time() - t0):.3f}s")
```

### Step 5: Compare Coefficients of Dense Lasso and Sparse Lasso

We compare the coefficients of the dense Lasso model and the sparse Lasso model to ensure that they are producing the same results. We compute the Euclidean norm of the difference between the coefficients.

```python
coeff_diff = linalg.norm(sparse_lasso.coef_ - dense_lasso.coef_)
print(f"Distance between coefficients : {coeff_diff:.2e}")
```

### Step 6: Generate Sparse Data

Next, we generate some sparse data that we will use for the Lasso regression. We copy the dense data from the previous step and replace all values less than 2.5 with 0. We also convert the sparse data to Scipy's Compressed Sparse Column format.

```python
Xs = X.copy()
Xs[Xs < 2.5] = 0.0
Xs_sp = sparse.coo_matrix(Xs)
Xs_sp = Xs_sp.tocsc()
```

### Step 7: Train Lasso on Sparse Data

Now we train two Lasso regression models, one on the dense data and one on the sparse data. We set the alpha parameter to 0.1 and the maximum number of iterations to 10000.

```python
alpha = 0.1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000)
```

### Step 8: Fit Lasso to Sparse Data

We fit the Lasso regression models to the sparse data using Scikit-learn's `fit` function. We also time the fitting process and print the time for each Lasso model.

```python
t0 = time()
sparse_lasso.fit(Xs_sp, y)
print(f"Sparse Lasso done in {(time() - t0):.3f}s")

t0 = time()
dense_lasso.fit(Xs, y)
print(f"Dense Lasso done in  {(time() - t0):.3f}s")
```

### Step 9: Compare Coefficients of Dense Lasso and Sparse Lasso

We compare the coefficients of the dense Lasso model and the sparse Lasso model to ensure that they are producing the same results. We compute the Euclidean norm of the difference between the coefficients.

```python
coeff_diff = linalg.norm(sparse_lasso.coef_ - dense_lasso.coef_)
print(f"Distance between coefficients : {coeff_diff:.2e}")
```

## Summary

In this lab, we demonstrated the use of Scikit-learn's Lasso regression algorithm on dense and sparse data. We showed that the Lasso algorithm provides the same results for dense and sparse data, and that in the case of sparse data, the algorithm is faster.
