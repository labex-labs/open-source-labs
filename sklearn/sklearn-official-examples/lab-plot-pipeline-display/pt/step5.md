# Construindo uma Busca em Grade sobre um Pipeline com um Classificador

Neste passo, construiremos uma busca em grade sobre um pipeline com um classificador e exibiremos sua representação visual.

Primeiro, importamos os módulos necessários:

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

Em seguida, definimos as etapas de pré-processamento para as características numéricas e categóricas:

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

Então, criamos o transformador de colunas:

```python
preprocessor = ColumnTransformer(
    [
        ("categorical", categorical_preprocessor, ["state", "gender"]),
        ("numerical", numeric_preprocessor, ["age", "weight"]),
    ]
)
```

Em seguida, criamos o pipeline:

```python
pipe = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", RandomForestClassifier())]
)
```

Então, definimos a grade de parâmetros para a busca em grade:

```python
param_grid = {
    "classifier__n_estimators": [200, 500],
    "classifier__max_features": ["auto", "sqrt", "log2"],
    "classifier__max_depth": [4, 5, 6, 7, 8],
    "classifier__criterion": ["gini", "entropy"],
}
```

Finalmente, criamos a busca em grade:

```python
grid_search = GridSearchCV(pipe, param_grid=param_grid, n_jobs=1)
```

E exibimos a representação visual da busca em grade:

```python
grid_search
```
