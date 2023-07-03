# Pipelines and Composite Estimators

## Introduction

In scikit-learn, pipelines and composite estimators are used to combine multiple transformers and estimators into a single model. This is useful when there is a fixed sequence of steps for processing the data, such as feature selection, normalization, and classification. Pipelines can also be used for joint parameter selection and to ensure that statistics from the test data do not leak into the trained model during cross-validation.

## Steps

### Step 1: Pipeline - Chaining Estimators

The `Pipeline` class in scikit-learn is used to chain multiple estimators into one. This allows you to call `fit` and `predict` once on your data to fit a whole sequence of estimators. It also allows for joint parameter selection and helps avoid data leakage in cross-validation.

To create a pipeline, you need to provide a list of `(key, value)` pairs, where the `key` is a string to identify each step and the `value` is an estimator object. Below is an example of creating a pipeline with a PCA transformer and an SVM classifier:

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA

estimators = [('reduce_dim', PCA()), ('clf', SVC())]
pipe = Pipeline(estimators)
```

You can access the steps of a pipeline using indexing or by name:

```python
pipe.steps[0]  # access by index
pipe[0]  # equivalent to above
pipe['reduce_dim']  # access by name
```

You can also use the `make_pipeline` function as a shorthand for constructing pipelines:

```python
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import Binarizer

make_pipeline(Binarizer(), MultinomialNB())
```

### Step 2: Nested Parameters

You can access the parameters of the estimators in a pipeline using the syntax `<estimator>__<parameter>`. This is useful for doing grid searches over the parameters of all estimators in the pipeline. Here is an example:

```python
pipe.set_params(clf__C=10)
```

### Step 3: Caching Transformers

Fitting transformers can be computationally expensive. To avoid repeated computation, you can enable caching transformers in a pipeline using the `memory` parameter. This parameter can be set to a directory where the transformers will be cached, or to a `joblib.Memory` object. Here is an example:

```python
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from tempfile import mkdtemp
from shutil import rmtree

estimators = [('reduce_dim', PCA()), ('clf', SVC())]
cachedir = mkdtemp()
pipe = Pipeline(estimators, memory=cachedir)

# Clear the cache directory when no longer needed
rmtree(cachedir)
```

### Step 4: TransformedTargetRegressor

The `TransformedTargetRegressor` class is used to transform the target variable in a regression problem before fitting a regression model. This is useful when you want to apply a transformation to the target variable, such as taking the logarithm. The predictions are mapped back to the original space via an inverse transform. Here is an example of using `TransformedTargetRegressor` with a linear regression model and a quantile transformer:

```python
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.compose import TransformedTargetRegressor
from sklearn.preprocessing import QuantileTransformer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X, y = fetch_california_housing(return_X_y=True)
transformer = QuantileTransformer(output_distribution='normal')
regressor = LinearRegression()
regr = TransformedTargetRegressor(regressor=regressor, transformer=transformer)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
regr.fit(X_train, y_train)
regr.score(X_test, y_test)
```

### Step 5: FeatureUnion - Composite Feature Spaces

The `FeatureUnion` class is used to combine multiple transformer objects into a new transformer that combines their output. This is useful when you want to apply different transformations to different features of the data, such as preprocessing text, floats, and dates separately. The transformers are applied in parallel, and the feature matrices they output are concatenated side-by-side into a larger matrix. Here is an example:

```python
from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA

estimators = [('linear_pca', PCA()), ('kernel_pca', KernelPCA())]
combined = FeatureUnion(estimators)
```

## Summary

Pipelines and composite estimators are powerful tools in scikit-learn for combining transformers and estimators into a single model. They provide convenience, parameter selection, and data safety. Pipelines allow for chaining estimators, nested parameters, and caching transformers. Composite estimators like `TransformedTargetRegressor` and `FeatureUnion` provide transformations and feature combination, respectively. These concepts are essential for building complex machine learning models that preprocess and handle heterogeneous data effectively.
