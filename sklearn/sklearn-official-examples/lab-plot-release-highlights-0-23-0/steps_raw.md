# Scikit-learn Tutorial

## Introduction

This tutorial will provide a step-by-step guide on how to use the scikit-learn library to perform machine learning tasks. Scikit-learn is a free machine learning library for Python, which provides tools for data mining and analysis, supervised and unsupervised learning, and model selection and evaluation.

## Steps

### Step 1: Generalized Linear Models

The scikit-learn 0.23 release added generalized linear models with non-normal loss functions. In this step, we will use the PoissonRegressor to model positive integer counts or relative frequencies.

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PoissonRegressor

# create a dataset
n_samples, n_features = 1000, 20
rng = np.random.RandomState(0)
X = rng.randn(n_samples, n_features)
# positive integer target correlated with X[:, 5] with many zeros:
y = rng.poisson(lam=np.exp(X[:, 5]) / 2)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=rng)

# create and fit a PoissonRegressor model
glm = PoissonRegressor()
glm.fit(X_train, y_train)

# calculate the model's score
print(glm.score(X_test, y_test))
```

### Step 2: Visualizing Estimators

In scikit-learn 0.23, estimators can be visualized in notebooks by enabling the display='diagram' option. This is particularly useful to summarize the structure of pipelines and other composite estimators, with interactivity to provide detail.

```python
from sklearn import set_config
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LogisticRegression

# enable display='diagram'
set_config(display="diagram")

# create a pipeline
num_proc = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
cat_proc = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OneHotEncoder(handle_unknown="ignore"),
)
preprocessor = make_column_transformer(
    (num_proc, ("feat1", "feat3")), (cat_proc, ("feat0", "feat2"))
)
clf = make_pipeline(preprocessor, LogisticRegression())
clf
```

### Step 3: Scalability and Stability Improvements to KMeans

The KMeans estimator was entirely reworked in scikit-learn 0.23 to be faster and more stable. In addition, the Elkan algorithm is now compatible with sparse matrices. The estimator uses OpenMP based parallelism instead of relying on joblib, so the n_jobs parameter has no effect anymore.

```python
import scipy
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import completeness_score

# create a dataset
rng = np.random.RandomState(0)
X, y = make_blobs(random_state=rng)
X = scipy.sparse.csr_matrix(X)
X_train, X_test, _, y_test = train_test_split(X, y, random_state=rng)

# create and fit a KMeans model
kmeans = KMeans(n_init="auto").fit(X_train)

# calculate the completeness score
print(completeness_score(kmeans.predict(X_test), y_test))
```

### Step 4: Improvements to Histogram-based Gradient Boosting Estimators

Scikit-learn 0.23 added various improvements to Histogram-based Gradient Boosting Estimators, including support for sample weights, an automatic early-stopping criterion, and the ability to define monotonic constraints.

```python
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.inspection import PartialDependenceDisplay

# create a dataset
n_samples = 500
rng = np.random.RandomState(0)
X = rng.randn(n_samples, 2)
noise = rng.normal(loc=0.0, scale=0.01, size=n_samples)
y = 5 * X[:, 0] + np.sin(10 * np.pi * X[:, 0]) - noise

# create and fit a HistGradientBoostingRegressor model with and without monotonic constraints
gbdt_no_cst = HistGradientBoostingRegressor().fit(X, y)
gbdt_cst = HistGradientBoostingRegressor(monotonic_cst=[1, 0]).fit(X, y)

# plot the partial dependence of the first feature
disp = PartialDependenceDisplay.from_estimator(
    gbdt_no_cst,
    X,
    features=[0],
    feature_names=["feature 0"],
    line_kw={"linewidth": 4, "label": "unconstrained", "color": "tab:blue"},
)
PartialDependenceDisplay.from_estimator(
    gbdt_cst,
    X,
    features=[0],
    line_kw={"linewidth": 4, "label": "constrained", "color": "tab:orange"},
    ax=disp.axes_,
)
disp.axes_[0, 0].plot(
    X[:, 0], y, "o", alpha=0.5, zorder=-1, label="samples", color="tab:green"
)
disp.axes_[0, 0].set_ylim(-3, 3)
disp.axes_[0, 0].set_xlim(-1, 1)
plt.legend()
plt.show()
```

### Step 5: Sample-weight Support for Lasso and ElasticNet

The Lasso and ElasticNet linear regressors now support sample weights.

```python
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
from sklearn.linear_model import Lasso
import numpy as np

# create a dataset
n_samples, n_features = 1000, 20
rng = np.random.RandomState(0)
X, y = make_regression(n_samples, n_features, random_state=rng)
sample_weight = rng.rand(n_samples)
X_train, X_test, y_train, y_test, sw_train, sw_test = train_test_split(
    X, y, sample_weight, random_state=rng
)

# create and fit a Lasso model with sample weights
reg = Lasso()
reg.fit(X_train, y_train, sample_weight=sw_train)

# calculate the model's score
print(reg.score(X_test, y_test, sw_test))
```

## Summary

This tutorial provided a step-by-step guide on how to use the scikit-learn library to perform machine learning tasks. We covered generalized linear models, visualizing estimators, scalability and stability improvements to KMeans, improvements to histogram-based gradient boosting estimators, and sample-weight support for Lasso and ElasticNet. Scikit-learn is a powerful tool for machine learning, and with this tutorial, you are now equipped with the knowledge to start using it in your own projects.
