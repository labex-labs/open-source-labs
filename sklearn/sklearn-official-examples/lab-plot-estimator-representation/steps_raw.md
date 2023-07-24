# Scikit-learn Estimators and Pipelines

## Introduction

In this lab, we will learn about different ways to display estimators and pipelines using scikit-learn. Estimators and pipelines are an essential part of the scikit-learn package, allowing us to build and evaluate machine learning models.

## Steps

### Step 1: Compact Text Representation

The first way we can display estimators is through compact text representation. Estimators will only show the parameters that have been set to non-default values when displayed as a string. This reduces visual noise and makes it easier to spot the differences when comparing instances.

```python
from sklearn.linear_model import LogisticRegression

# Create an instance of Logistic Regression with l1 penalty
lr = LogisticRegression(penalty="l1")

# Display the estimator
print(lr)
```

### Step 2: Rich HTML Representation

The second way we can display estimators is through rich HTML representation. In notebooks, estimators and pipelines will use a rich HTML representation. This is particularly useful to summarize the structure of pipelines and other composite estimators, with interactivity to provide detail.

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LogisticRegression

# Create pipelines for numerical and categorical data
num_proc = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
cat_proc = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OneHotEncoder(handle_unknown="ignore"),
)

# Create a preprocessor that applies the numerical and categorical pipelines to specific columns
preprocessor = make_column_transformer(
    (num_proc, ("feat1", "feat3")), (cat_proc, ("feat0", "feat2"))
)

# Create a pipeline that applies the preprocessor and logistic regression
clf = make_pipeline(preprocessor, LogisticRegression())

# Display the pipeline
clf
```

## Summary

In this lab, we learned about two ways to display estimators and pipelines using scikit-learn: compact text representation and rich HTML representation. These representations can be useful for summarizing the structure of pipelines and other composite estimators and for comparing different instances. By using these techniques, we can improve our understanding of machine learning models and their performance.
