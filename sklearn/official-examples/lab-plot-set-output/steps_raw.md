# Using `set_output` API

## Introduction

In this lab, we will learn how to use the `set_output` API in Scikit-Learn to configure transformers to output pandas DataFrames. This feature is useful when working with heterogeneous data and pipelines in Scikit-Learn.

## Steps

### Step 1: Load the Iris dataset

First, we will load the Iris dataset as a DataFrame to demonstrate the `set_output` API.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(as_frame=True, return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
X_train.head()
```

### Step 2: Configure a transformer to output DataFrames

To configure an estimator such as `preprocessing.StandardScaler` to return DataFrames, call `set_output`.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().set_output(transform="pandas")

scaler.fit(X_train)
X_test_scaled = scaler.transform(X_test)
X_test_scaled.head()
```

### Step 3: Configure `transform` after `fit`

`set_output` can be called after `fit` to configure `transform` after the fact.

```python
scaler2 = StandardScaler()

scaler2.fit(X_train)
X_test_np = scaler2.transform(X_test)
print(f"Default output type: {type(X_test_np).__name__}")

scaler2.set_output(transform="pandas")
X_test_df = scaler2.transform(X_test)
print(f"Configured pandas output type: {type(X_test_df).__name__}")
```

### Step 4: Configure a pipeline to output DataFrames

In a `pipeline.Pipeline`, `set_output` configures all steps to output DataFrames.

```python
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectPercentile

clf = make_pipeline(
    StandardScaler(), SelectPercentile(percentile=75), LogisticRegression()
)
clf.set_output(transform="pandas")
clf.fit(X_train, y_train)
```

### Step 5: Load the Titanic dataset

Next, we will load the Titanic dataset to demonstrate `set_output` with `compose.ColumnTransformer` and heterogeneous data.

```python
from sklearn.datasets import fetch_openml

X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)
```

### Step 6: Configure `set_output` globally

The `set_output` API can be configured globally by using `set_config` and setting `transform_output` to `"pandas"`.

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn import set_config

set_config(transform_output="pandas")

num_pipe = make_pipeline(SimpleImputer(), StandardScaler())
num_cols = ["age", "fare"]
ct = ColumnTransformer(
    (
        ("numerical", num_pipe, num_cols),
        (
            "categorical",
            OneHotEncoder(
                sparse_output=False, drop="if_binary", handle_unknown="ignore"
            ),
            ["embarked", "sex", "pclass"],
        ),
    ),
    verbose_feature_names_out=False,
)
clf = make_pipeline(ct, SelectPercentile(percentile=50), LogisticRegression())
clf.fit(X_train, y_train)
```

### Step 7: Configure `set_output` with `config_context`

When configuring the output type with `config_context`, the configuration at the time when `transform` or `fit_transform` are called is what counts.

```python
scaler = StandardScaler()
scaler.fit(X_train[num_cols])

with config_context(transform_output="pandas"):
    X_test_scaled = scaler.transform(X_test[num_cols])
X_test_scaled.head()
```

## Summary

In this lab, we learned how to use the `set_output` API in Scikit-Learn to configure transformers to output pandas DataFrames. We demonstrated how to configure an estimator to output DataFrames, configure a pipeline to output DataFrames, and configure `set_output` globally with `set_config`. We also learned how to configure `set_output` with `config_context`.
