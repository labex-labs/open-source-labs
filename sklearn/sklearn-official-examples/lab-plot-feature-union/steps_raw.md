# Concatenating Multiple Feature Extraction Methods

## Introduction

In this lab, we will learn how to concatenate multiple feature extraction methods using Python's scikit-learn library. We will use the `FeatureUnion` transformer to combine features obtained by PCA and univariate selection. Combining features using this transformer has the benefit that it allows cross-validation and grid searches over the whole process.

## Steps

### Step 1: Import Libraries

We will begin by importing the required libraries. We will be using scikit-learn's `Pipeline`, `FeatureUnion`, `GridSearchCV`, `SVC`, `load_iris`, `PCA`, and `SelectKBest` classes.

```python
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
```

### Step 2: Load the Dataset

Next, we will load the iris dataset using the `load_iris` function.

```python
iris = load_iris()

X, y = iris.data, iris.target
```

### Step 3: Feature Extraction

Since the iris dataset is high-dimensional, we will perform feature extraction using PCA and univariate selection.

#### PCA

We will use PCA to reduce the dimensionality of the dataset.

```python
pca = PCA(n_components=2)
```

#### Univariate Selection

We will use univariate selection to select the most significant features.

```python
selection = SelectKBest(k=1)
```

#### Combined Features

We will combine the features obtained from PCA and univariate selection using the `FeatureUnion` transformer.

```python
combined_features = FeatureUnion([("pca", pca), ("univ_select", selection)])
```

#### Transformed Dataset

We will use the combined features to transform the dataset.

```python
X_features = combined_features.fit(X, y).transform(X)
print("Combined space has", X_features.shape[1], "features")
```

### Step 4: Model Training

We will train a support vector machine (SVM) model using the transformed dataset.

```python
svm = SVC(kernel="linear")
```

### Step 5: Grid Search

We will perform a grid search over the hyperparameters of the pipeline using `GridSearchCV`.

```python
pipeline = Pipeline([("features", combined_features), ("svm", svm)])

param_grid = dict(
    features__pca__n_components=[1, 2, 3],
    features__univ_select__k=[1, 2],
    svm__C=[0.1, 1, 10],
)

grid_search = GridSearchCV(pipeline, param_grid=param_grid, verbose=10)
grid_search.fit(X, y)
print(grid_search.best_estimator_)
```

## Summary

In this lab, we learned how to concatenate multiple feature extraction methods using Python's scikit-learn library. We used the `FeatureUnion` transformer to combine features obtained by PCA and univariate selection. We also trained a support vector machine (SVM) model and performed a grid search over the hyperparameters of the pipeline.
