# Construyendo una búsqueda en cuadrícula sobre una tubería con un clasificador

En este paso, construiremos una búsqueda en cuadrícula sobre una tubería con un clasificador, y mostraremos su representación visual.

Primero, importamos los módulos necesarios:

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
pipe = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", RandomForestClassifier())]
)
```

Después, definimos la cuadrícula de parámetros para la búsqueda en cuadrícula:

```python
param_grid = {
    "classifier__n_estimators": [200, 500],
    "classifier__max_features": ["auto", "sqrt", "log2"],
    "classifier__max_depth": [4, 5, 6, 7, 8],
    "classifier__criterion": ["gini", "entropy"],
}
```

Finalmente, creamos la búsqueda en cuadrícula:

```python
grid_search = GridSearchCV(pipe, param_grid=param_grid, n_jobs=1)
```

Y mostramos la representación visual de la búsqueda en cuadrícula:

```python
grid_search
```
