# Construyendo una tubería compleja con un transformador de columnas en cadena

En este paso, construiremos una tubería compleja con un transformador de columnas y un clasificador, y mostraremos su representación visual.

Primero, importamos los módulos necesarios:

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
```

Luego, definimos los pasos de preprocesamiento para las características numéricas y categóricas:

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

Después, creamos el transformador de columnas:

```python
preprocessor = ColumnTransformer(
    [
        ("categorical", categorical_preprocessor, ["state", "gender"]),
        ("numerical", numeric_preprocessor, ["age", "weight"]),
    ]
)
```

Luego, creamos la tubería:

```python
pipe = make_pipeline(preprocessor, LogisticRegression(max_iter=500))
```

Finalmente, mostramos la representación visual de la tubería:

```python
pipe
```
