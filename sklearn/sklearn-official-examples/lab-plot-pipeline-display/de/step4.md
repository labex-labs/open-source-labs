# Ein komplexes Pipeline erstellen, das einen Spaltentransformator verkettet

In diesem Schritt werden wir eine komplexe Pipeline mit einem Spaltentransformator und einem Klassifizierer erstellen und seine visuelle Darstellung anzeigen.

Zunächst importieren wir die erforderlichen Module:

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
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
pipe = make_pipeline(preprocessor, LogisticRegression(max_iter=500))
```

Schließlich zeigen wir die visuelle Darstellung der Pipeline an:

```python
pipe
```
