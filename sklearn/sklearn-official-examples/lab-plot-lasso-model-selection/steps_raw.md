# Model Selection for Lasso Regression

## Introduction

In this lab, we will learn about selecting the best hyperparameter alpha for Lasso regression models. Two approaches will be discussed: (1) selecting the optimal value of alpha by only using the training set and some information criterion, and (2) selecting the best hyperparameter using cross-validation. We will use the diabetes dataset in this example.

## Steps

### Step 1: Dataset

First, we will load the diabetes dataset using the `load_diabetes` function from `sklearn.datasets`. The dataset consists of 10 baseline variables, age, sex, body mass index, average blood pressure, and six blood serum measurements, and a quantitative measure of disease progression one year after baseline.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True, as_frame=True)
X.head()
```

### Step 2: Adding Random Features

We will add some random features to the original data to better illustrate the feature selection performed by the Lasso model. Random features will be generated using the `RandomState` function from `numpy`.

```python
import numpy as np
import pandas as pd

rng = np.random.RandomState(42)
n_random_features = 14
X_random = pd.DataFrame(
    rng.randn(X.shape[0], n_random_features),
    columns=[f"random_{i:02d}" for i in range(n_random_features)],
)
X = pd.concat([X, X_random], axis=1)
X[X.columns[::3]].head()
```

### Step 3: Selecting Lasso via an Information Criterion

We will use the `LassoLarsIC` function from `sklearn.linear_model` to provide a Lasso estimator that uses the Akaike information criterion (AIC) or the Bayes information criterion (BIC) to select the optimal value of the regularization parameter alpha. We will first fit a Lasso model with the AIC criterion.

```python
import time
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

start_time = time.time()
lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
fit_time = time.time() - start_time
```

### Step 4: Storing Results and Checking Optimal Alpha

We will store the AIC metric for each value of alpha used during `fit`. We will then perform the same analysis using the BIC criterion. Finally, we will check which value of `alpha` leads to the minimum AIC and BIC.

```python
results = pd.DataFrame(
    {
        "alphas": lasso_lars_ic[-1].alphas_,
        "AIC criterion": lasso_lars_ic[-1].criterion_,
    }
).set_index("alphas")
alpha_aic = lasso_lars_ic[-1].alpha_

lasso_lars_ic.set_params(lassolarsic__criterion="bic").fit(X, y)
results["BIC criterion"] = lasso_lars_ic[-1].criterion_
alpha_bic = lasso_lars_ic[-1].alpha_

def highlight_min(x):
    x_min = x.min()
    return ["font-weight: bold" if v == x_min else "" for v in x]

results.style.apply(highlight_min)
```

### Step 5: Plotting AIC and BIC Values

Finally, we will plot the AIC and BIC values for the different alpha values. The vertical lines in the plot correspond to the alpha chosen for each criterion. The selected alpha corresponds to the minimum of the AIC or BIC criterion.

```python
ax = results.plot()
ax.vlines(
    alpha_aic,
    results["AIC criterion"].min(),
    results["AIC criterion"].max(),
    label="alpha: AIC estimate",
    linestyles="--",
    color="tab:blue",
)
ax.vlines(
    alpha_bic,
    results["BIC criterion"].min(),
    results["BIC criterion"].max(),
    label="alpha: BIC estimate",
    linestyle="--",
    color="tab:orange",
)
ax.set_xlabel(r"$\alpha$")
ax.set_ylabel("criterion")
ax.set_xscale("log")
ax.legend()
_ = ax.set_title(
    f"Information-criterion for model selection (training time {fit_time:.2f}s)"
)
```

### Step 6: Selecting Lasso via Cross-Validation

We will use two different estimators to select the best hyperparameter alpha with integrated cross-validation: `LassoCV` and `LassoLarsCV`. For both algorithms, we will use a 20-fold cross-validation strategy.

#### Lasso via Coordinate Descent

We will make the hyperparameter tuning using `LassoCV`.

```python
from sklearn.linear_model import LassoCV

start_time = time.time()
model = make_pipeline(StandardScaler(), LassoCV(cv=20)).fit(X, y)
fit_time = time.time() - start_time
```

#### Lasso via Least Angle Regression

We will make the hyperparameter tuning using `LassoLarsCV`.

```python
from sklearn.linear_model import LassoLarsCV

start_time = time.time()
model = make_pipeline(StandardScaler(), LassoLarsCV(cv=20)).fit(X, y)
fit_time = time.time() - start_time
```

### Step 7: Summary of Cross-Validation Approach

Both algorithms give roughly the same results. Lars computes a solution path only for each kink in the path. As a result, it is very efficient when there are only of few kinks, which is the case if there are few features or samples. On the opposite, coordinate descent computes the path points on a pre-specified grid (here we use the default). Thus it is more efficient if the number of grid points is smaller than the number of kinks in the path. Such a strategy can be interesting if the number of features is really large and there are enough samples to be selected in each of the cross-validation fold. In terms of numerical errors, for heavily correlated variables, Lars will accumulate more errors, while the coordinate descent algorithm will only sample the path on a grid.

## Summary

In this lab, we learned about selecting the best hyperparameter alpha for Lasso regression models. We discussed two approaches: (1) selecting the optimal value of alpha by only using the training set and some information criterion, and (2) selecting the best hyperparameter using cross-validation. We used the diabetes dataset in this example. Both approaches can work similarly, but in-sample hyperparameter selection shows its efficacy in terms of computational performance. However, it can only be used when the number of samples is large enough compared to the number of features. Hyperparameter optimization via cross-validation is a safe strategy that works in different settings.
