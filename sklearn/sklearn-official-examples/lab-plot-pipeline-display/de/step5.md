# Ein Grid Search über eine Pipeline mit einem Klassifizierer erstellen

In diesem Schritt werden wir einen Grid Search über eine Pipeline mit einem Klassifizierer erstellen und seine visuelle Darstellung anzeigen.

Zunächst importieren wir die erforderlichen Module:

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

Als nächstes definieren wir die Vorverarbeitungsschritte für die numerischen und kategorischen Merkmale:

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

Dann erstellen wir den Spaltentransformator:

```python
preprocessor = ColumnTransformer(
    [
        ("categorical", categorical_preprocessor, ["state", "gender"]),
        ("numerical", numeric_preprocessor, ["age", "weight"]),
    ]
)
```

Als nächstes erstellen wir die Pipeline:

```python
pipe = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", RandomForestClassifier())]
)
```

Dann definieren wir das Parameter-Gitter für den Grid Search:

```python
param_grid = {
    "classifier__n_estimators": [200, 500],
    "classifier__max_features": ["auto", "sqrt", "log2"],
    "classifier__max_depth": [4, 5, 6, 7, 8],
    "classifier__criterion": ["gini", "entropy"],
}
```

Schließlich erstellen wir den Grid Search:

```python
grid_search = GridSearchCV(pipe, param_grid=param_grid, n_jobs=1)
```

Und zeigen die visuelle Darstellung des Grid Searchs an:

```python
grid_search
```
