# Column Transformer with Mixed Types

## Introduction

This lab illustrates how to apply different preprocessing and feature extraction pipelines to different subsets of features, using `ColumnTransformer`. This is particularly handy for the case of datasets that contain heterogeneous data types, since we may want to scale the numeric features and one-hot encode the categorical ones.

In this lab, we will be using the Titanic dataset from OpenML to build a pipeline that preprocesses both categorical and numeric data using `ColumnTransformer` and use that to train a logistic regression model.

## Steps

### Step 1: Import Libraries

In this step, we will import the necessary libraries for building our pipeline.

```python
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.datasets import fetch_openml
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.feature_selection import SelectPercentile, chi2
```

### Step 2: Load the Dataset

In this step, we will load the Titanic dataset from OpenML using `fetch_openml`.

```python
X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
```

### Step 3: Define Numeric and Categorical Features

In this step, we will define the numeric and categorical features that we will be using for our pipeline. We will also define the preprocessing pipelines for both numeric and categorical data.

```python
numeric_features = ["age", "fare"]
numeric_transformer = Pipeline(
    steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
)

categorical_features = ["embarked", "sex", "pclass"]
categorical_transformer = Pipeline(
    steps=[
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ("selector", SelectPercentile(chi2, percentile=50)),
    ]
)
```

### Step 4: Define the Preprocessor

In this step, we will define the `ColumnTransformer` that will be used to preprocess our data.

```python
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)
```

### Step 5: Append the Classifier to Preprocessing Pipeline

In this step, we will append the logistic regression classifier to our preprocessing pipeline using `Pipeline`.

```python
clf = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression())]
)
```

### Step 6: Split the Data

In this step, we will split our data into training and testing sets using `train_test_split`.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
```

### Step 7: Fit the Pipeline

In this step, we will fit our pipeline to our training data.

```python
clf.fit(X_train, y_train)
```

### Step 8: Evaluate the Pipeline

In this step, we will evaluate the performance of our pipeline by calculating the model score.

```python
print("model score: %.3f" % clf.score(X_test, y_test))
```

### Step 9: Use ColumnTransformer by Selecting Columns by Data Types

In this step, we will use `ColumnTransformer` by selecting columns by data types. We will use `make_column_selector` to select columns based on their data types.

```python
from sklearn.compose import make_column_selector as selector

subset_feature = ["embarked", "sex", "pclass", "age", "fare"]
X_train, X_test = X_train[subset_feature], X_test[subset_feature]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, selector(dtype_exclude="category")),
        ("cat", categorical_transformer, selector(dtype_include="category")),
    ]
)
clf = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression())]
)
```

### Step 10: Use Grid Search to Tune Hyperparameters

In this step, we will use grid search to tune the hyperparameters of our pipeline.

```python
param_grid = {
    "preprocessor__num__imputer__strategy": ["mean", "median"],
    "preprocessor__cat__selector__percentile": [10, 30, 50, 70],
    "classifier__C": [0.1, 1.0, 10, 100],
}

search_cv = RandomizedSearchCV(clf, param_grid, n_iter=10, random_state=0)
search_cv.fit(X_train, y_train)

print("Best params:")
print(search_cv.best_params_)
print(f"Internal CV score: {search_cv.best_score_:.3f}")
```

## Summary

In this lab, we learned how to use `ColumnTransformer` to preprocess both categorical and numeric data in a pipeline and how to use grid search to tune the hyperparameters of our pipeline.
