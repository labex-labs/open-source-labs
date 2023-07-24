# Scikit-Learn Tutorial

## Introduction

This tutorial is a step-by-step guide to learn about the new features of scikit-learn 1.2. Scikit-learn is a popular machine learning library in Python that provides a range of tools for machine learning, including classification, regression, clustering, and dimensionality reduction. The latest release of scikit-learn 1.2 has several new features and improvements, including pandas output with the set_output API, interaction constraints in histogram-based gradient boosting trees, and more.

## Steps

### Step 1: Install scikit-learn 1.2

To get started with the latest version of scikit-learn, you need to install it using pip or conda. Here's how to install it using pip:

```python
pip install --upgrade scikit-learn
```

Or, if you are using conda:

```python
conda install -c conda-forge scikit-learn
```

### Step 2: Pandas Output with set_output API

Scikit-learn's transformers now support pandas output with the `set_output` API. To learn more about the `set_output` API, see the example: `sphx_glr_auto_examples_miscellaneous_plot_set_output.py` and this video, pandas DataFrame output for scikit-learn transformers (some examples).

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler, KBinsDiscretizer
from sklearn.compose import ColumnTransformer

X, y = load_iris(as_frame=True, return_X_y=True)
sepal_cols = ["sepal length (cm)", "sepal width (cm)"]
petal_cols = ["petal length (cm)", "petal width (cm)"]

preprocessor = ColumnTransformer(
    [
        ("scaler", StandardScaler(), sepal_cols),
        ("kbin", KBinsDiscretizer(encode="ordinal"), petal_cols),
    ],
    verbose_feature_names_out=False,
).set_output(transform="pandas")

X_out = preprocessor.fit_transform(X)
X_out.sample(n=5, random_state=0)
```

### Step 3: Interaction Constraints in Histogram-based Gradient Boosting Trees

`HistGradientBoostingRegressor` and `HistGradientBoostingClassifier` now support interaction constraints with the `interaction_cst` parameter. For details, see the User Guide.

```python
from sklearn.datasets import load_diabetes
from sklearn.ensemble import HistGradientBoostingRegressor

X, y = load_diabetes(return_X_y=True, as_frame=True)

hist_no_interact = HistGradientBoostingRegressor(
    interaction_cst=[[i] for i in range(X.shape[1])], random_state=0
)
hist_no_interact.fit(X, y)
```

### Step 4: New and Enhanced Displays

`PredictionErrorDisplay` provides a way to analyze regression models in a qualitative manner.

```python
import matplotlib.pyplot as plt
from sklearn.metrics import PredictionErrorDisplay

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
_ = PredictionErrorDisplay.from_estimator(
    hist_no_interact, X, y, kind="actual_vs_predicted", ax=axs[0]
)
_ = PredictionErrorDisplay.from_estimator(
    hist_no_interact, X, y, kind="residual_vs_predicted", ax=axs[1]
)
```

`LearningCurveDisplay` is now available to plot results from `learning_curve`.

```python
from sklearn.model_selection import LearningCurveDisplay

_ = LearningCurveDisplay.from_estimator(
    hist_no_interact, X, y, cv=5, n_jobs=2, train_sizes=np.linspace(0.1, 1, 5)
)
```

`PartialDependenceDisplay` exposes a new parameter `categorical_features` to display partial dependence for categorical features using bar plots and heatmaps.

```python
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import make_pipeline
from sklearn.inspection import PartialDependenceDisplay

X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
X = X.select_dtypes(["number", "category"]).drop(columns=["body"])

categorical_features = ["pclass", "sex", "embarked"]
model = make_pipeline(
    ColumnTransformer(
        transformers=[("cat", OrdinalEncoder(), categorical_features)],
        remainder="passthrough",
    ),
    HistGradientBoostingRegressor(random_state=0),
).fit(X, y)

fig, ax = plt.subplots(figsize=(14, 4), constrained_layout=True)
_ = PartialDependenceDisplay.from_estimator(
    model,
    X,
    features=["age", "sex", ("pclass", "sex")],
    categorical_features=categorical_features,
    ax=ax,
)
```

### Step 5: Faster Parser in fetch_openml

`fetch_openml` now supports a new "pandas" parser that is more memory and CPU efficient. In v1.4, the default will change to parser="auto" which will automatically use the "pandas" parser for dense data and "liac-arff" for sparse data.

```python
X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
X.head()
```

### Step 6: Experimental Array API Support in LinearDiscriminantAnalysis

Experimental support for the Array API specification was added to LinearDiscriminantAnalysis. The estimator can now run on any Array API compliant libraries such as CuPy, a GPU-accelerated array library. For details, see the User Guide.

## Summary

In this tutorial, we learned about the new features of scikit-learn 1.2, including pandas output with the set_output API, interaction constraints in histogram-based gradient boosting trees, and more. We also covered how to install scikit-learn 1.2 and demonstrated the use of several new and enhanced displays. Finally, we discussed the experimental support for the Array API specification in LinearDiscriminantAnalysis.
