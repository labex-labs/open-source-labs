# Cross-validation with Linear Models

## Introduction

In this lab, we will be using cross-validation with linear models. We will be using the diabetes dataset and applying GridSearchCV to find the best alpha value for Lasso regression. We will then plot the errors and use LassoCV to see how much we can trust the selection of alpha.

## Steps

### Step 1: Load and prepare the dataset

First, we will load and prepare the diabetes dataset. We will only use the first 150 samples for this exercise.

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

X, y = datasets.load_diabetes(return_X_y=True)
X = X[:150]
y = y[:150]
```

### Step 2: Apply GridSearchCV

Next, we will apply GridSearchCV to find the best alpha value for Lasso regression. We will use a range of alpha values from 10^-4 to 10^-0.5 with 30 values in between. We will use 5 folds for cross-validation.

```python
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV

lasso = Lasso(random_state=0, max_iter=10000)
alphas = np.logspace(-4, -0.5, 30)

tuned_parameters = [{"alpha": alphas}]
n_folds = 5

clf = GridSearchCV(lasso, tuned_parameters, cv=n_folds, refit=False)
clf.fit(X, y)
```

### Step 3: Plot the errors

We will now plot the errors to see the best alpha value. We will plot the mean test scores and the standard errors of the scores.

```python
scores = clf.cv_results_["mean_test_score"]
scores_std = clf.cv_results_["std_test_score"]

plt.figure().set_size_inches(8, 6)
plt.semilogx(alphas, scores)

std_error = scores_std / np.sqrt(n_folds)

plt.semilogx(alphas, scores + std_error, "b--")
plt.semilogx(alphas, scores - std_error, "b--")

plt.fill_between(alphas, scores + std_error, scores - std_error, alpha=0.2)

plt.ylabel("CV score +/- std error")
plt.xlabel("alpha")
plt.axhline(np.max(scores), linestyle="--", color=".5")
plt.xlim([alphas[0], alphas[-1]])
```

### Step 4: Use LassoCV to check alpha selection

Finally, we will use LassoCV to see how much we can trust the selection of alpha. We will use KFold with 3 folds.

```python
from sklearn.linear_model import LassoCV
from sklearn.model_selection import KFold

lasso_cv = LassoCV(alphas=alphas, random_state=0, max_iter=10000)
k_fold = KFold(3)

print("Answer to the bonus question:", "how much can you trust the selection of alpha?")
print()
print("Alpha parameters maximising the generalization score on different")
print("subsets of the data:")
for k, (train, test) in enumerate(k_fold.split(X, y)):
    lasso_cv.fit(X[train], y[train])
    print(
        "[fold {0}] alpha: {1:.5f}, score: {2:.5f}".format(
            k, lasso_cv.alpha_, lasso_cv.score(X[test], y[test])
        )
    )

print()
print("Answer: Not very much since we obtained different alphas for different")
print("subsets of the data and moreover, the scores for these alphas differ")
print("quite substantially.")
```

## Summary

In this lab, we learned how to use cross-validation with linear models. We used GridSearchCV to find the best alpha value for Lasso regression and plotted the errors to visualize the selection. We also used LassoCV to check the selection of alpha.
