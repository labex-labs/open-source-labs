# Lasso and Elastic Net Tutorial

## Introduction

In this tutorial, we will learn about Lasso and Elastic Net, which are techniques used for linear regression and implemented using a coordinate descent. We will learn how to compute regularization paths using the Lasso and Elastic Net, and how to display the results using matplotlib.

## Steps

### Step 1: Load the Dataset

In this step, we will load the diabetes dataset from scikit-learn library and standardize the data.

```python
from sklearn import datasets

# Load the diabetes dataset
X, y = datasets.load_diabetes(return_X_y=True)

# Standardize data
X /= X.std(axis=0)
```

### Step 2: Compute Regularization Path Using Lasso

In this step, we will compute the regularization path using the Lasso technique and display the results using matplotlib.

```python
from sklearn.linear_model import lasso_path
import numpy as np
import matplotlib.pyplot as plt

# Set the value of eps
eps = 5e-3

# Compute regularization path using the Lasso
alphas_lasso, coefs_lasso, _ = lasso_path(X, y, eps=eps)

# Display the results using matplotlib
plt.figure(1)
colors = cycle(["b", "r", "g", "c", "k"])
neg_log_alphas_lasso = -np.log10(alphas_lasso)
for coef_l, c in zip(coefs_lasso, colors):
    l1 = plt.plot(neg_log_alphas_lasso, coef_l, c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("coefficients")
plt.title("Lasso Path")
plt.axis("tight")
plt.show()
```

### Step 3: Compute Regularization Path Using Positive Lasso

In this step, we will compute the regularization path using the positive Lasso technique and display the results using matplotlib.

```python
# Compute regularization path using the positive Lasso
alphas_positive_lasso, coefs_positive_lasso, _ = lasso_path(X, y, eps=eps, positive=True)

# Display the results using matplotlib
plt.figure(2)
neg_log_alphas_positive_lasso = -np.log10(alphas_positive_lasso)
for coef_l, coef_pl, c in zip(coefs_lasso, coefs_positive_lasso, colors):
    l1 = plt.plot(neg_log_alphas_lasso, coef_l, c=c)
    l2 = plt.plot(neg_log_alphas_positive_lasso, coef_pl, linestyle="--", c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("coefficients")
plt.title("Lasso and Positive Lasso")
plt.legend((l1[-1], l2[-1]), ("Lasso", "Positive Lasso"), loc="lower left")
plt.axis("tight")
plt.show()
```

### Step 4: Compute Regularization Path Using Elastic Net

In this step, we will compute the regularization path using the Elastic Net technique and display the results using matplotlib.

```python
from sklearn.linear_model import enet_path

# Compute regularization path using the Elastic Net
alphas_enet, coefs_enet, _ = enet_path(X, y, eps=eps, l1_ratio=0.8)

# Display the results using matplotlib
plt.figure(3)
neg_log_alphas_enet = -np.log10(alphas_enet)
for coef_e, c in zip(coefs_enet, colors):
    l1 = plt.plot(neg_log_alphas_enet, coef_e, c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("coefficients")
plt.title("Elastic Net Path")
plt.axis("tight")
plt.show()
```

### Step 5: Compute Regularization Path Using Positive Elastic Net

In this step, we will compute the regularization path using the positive Elastic Net technique and display the results using matplotlib.

```python
# Compute regularization path using the positive Elastic Net
alphas_positive_enet, coefs_positive_enet, _ = enet_path(X, y, eps=eps, l1_ratio=0.8, positive=True)

# Display the results using matplotlib
plt.figure(4)
neg_log_alphas_positive_enet = -np.log10(alphas_positive_enet)
for coef_e, coef_pe, c in zip(coefs_enet, coefs_positive_enet, colors):
    l1 = plt.plot(neg_log_alphas_enet, coef_e, c=c)
    l2 = plt.plot(neg_log_alphas_positive_enet, coef_pe, linestyle="--", c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("coefficients")
plt.title("Elastic Net and Positive Elastic Net")
plt.legend((l1[-1], l2[-1]), ("Elastic Net", "Positive Elastic Net"), loc="lower left")
plt.axis("tight")
plt.show()
```

## Summary

In this tutorial, we learned about Lasso and Elastic Net, which are techniques used for linear regression. We learned how to compute regularization paths using the Lasso and Elastic Net, and how to display the results using matplotlib. We also learned how to compute the regularization path using positive Lasso and positive Elastic Net techniques.
