# Constructing a Complex Pipeline Chaining a Column Transformer

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


