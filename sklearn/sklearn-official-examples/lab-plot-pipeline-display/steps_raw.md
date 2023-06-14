# Scikit-Learn Pipeline

## Introduction

This lab is a step-by-step guide on how to construct and display pipelines in Scikit-Learn.

## Steps

### Step 1: Constructing a Simple Pipeline with a Preprocessing Step and Classifier

In this step, we will construct a simple pipeline with a preprocessing step and a classifier, and display its visual representation.

First, we import the necessary modules:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import set_config
```

Next, we define the steps of the pipeline:

```python
steps = [
    ("preprocessing", StandardScaler()),
    ("classifier", LogisticRegression()),
]
```

Then, we create the pipeline:

```python
pipe = Pipeline(steps)
```

Finally, we display the visual representation of the pipeline:

```python
set_config(display="diagram")
pipe
```

### Step 2: Constructing a Pipeline Chaining Multiple Preprocessing Steps & Classifier

In this step, we will construct a pipeline with multiple preprocessing steps and a classifier, and display its visual representation.

First, we import the necessary modules:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LogisticRegression
```

Next, we define the steps of the pipeline:

```python
steps = [
    ("standard_scaler", StandardScaler()),
    ("polynomial", PolynomialFeatures(degree=3)),
    ("classifier", LogisticRegression(C=2.0)),
]
```

Then, we create the pipeline:

```python
pipe = Pipeline(steps)
```

Finally, we display the visual representation of the pipeline:

```python
pipe
```

### Step 3: Constructing a Pipeline with Dimensionality Reduction and Classifier

In this step, we will construct a pipeline with a dimensionality reduction step and a classifier, and display its visual representation.

First, we import the necessary modules:

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA
```

Next, we define the steps of the pipeline:

```python
steps = [("reduce_dim", PCA(n_components=4)), ("classifier", SVC(kernel="linear"))]
```

Then, we create the pipeline:

```python
pipe = Pipeline(steps)
```

Finally, we display the visual representation of the pipeline:

```python
pipe
```

### Step 4: Constructing a Complex Pipeline Chaining a Column Transformer

In this step, we will construct a complex pipeline with a column transformer and a classifier, and display its visual representation.

First, we import the necessary modules:

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
```

Next, we define the preprocessing steps for the numerical and categorical features:

```python
numeric_preprocessor = Pipeline(
    steps=[
        ("imputation_mean", SimpleImputer(missing_values=np.nan, strategy="mean")),
        ("scaler", StandardScaler()),
    ]
)

categorical_preprocessor = Pipeline(
    steps=[
        (
            "imputation_constant",
            SimpleImputer(fill_value="missing", strategy="constant"),
        ),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ]
)
```

Then, we create the column transformer:

```python
preprocessor = ColumnTransformer(
    [
        ("categorical", categorical_preprocessor, ["state", "gender"]),
        ("numerical", numeric_preprocessor, ["age", "weight"]),
    ]
)
```

Next, we create the pipeline:

```python
pipe = make_pipeline(preprocessor, LogisticRegression(max_iter=500))
```

Finally, we display the visual representation of the pipeline:

```python
pipe
```

### Step 5: Constructing a Grid Search over a Pipeline with a Classifier

In this step, we will construct a grid search over a pipeline with a classifier, and display its visual representation.

First, we import the necessary modules:

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
```

Next, we define the preprocessing steps for the numerical and categorical features:

```python
numeric_preprocessor = Pipeline(
    steps=[
        ("imputation_mean", SimpleImputer(missing_values=np.nan, strategy="mean")),
        ("scaler", StandardScaler()),
    ]
)

categorical_preprocessor = Pipeline(
    steps=[
        (
            "imputation_constant",
            SimpleImputer(fill_value="missing", strategy="constant"),
        ),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ]
)
```

Then, we create the column transformer:

```python
preprocessor = ColumnTransformer(
    [
        ("categorical", categorical_preprocessor, ["state", "gender"]),
        ("numerical", numeric_preprocessor, ["age", "weight"]),
    ]
)
```

Next, we create the pipeline:

```python
pipe = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", RandomForestClassifier())]
)
```

Then, we define the parameter grid for the grid search:

```python
param_grid = {
    "classifier__n_estimators": [200, 500],
    "classifier__max_features": ["auto", "sqrt", "log2"],
    "classifier__max_depth": [4, 5, 6, 7, 8],
    "classifier__criterion": ["gini", "entropy"],
}
```

Finally, we create the grid search:

```python
grid_search = GridSearchCV(pipe, param_grid=param_grid, n_jobs=1)
```

And display the visual representation of the grid search:

```python
grid_search
```

## Summary

This lab provided a step-by-step guide on how to construct and display pipelines in Scikit-Learn. We covered simple pipelines with a preprocessing step and classifier, pipelines chaining multiple preprocessing steps and a classifier, pipelines with dimensionality reduction and a classifier, complex pipelines chaining a column transformer and a classifier, and grid searches over pipelines with a classifier.
