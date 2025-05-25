# Construindo um Pipeline Complexo Encadeando um Transformador de Colunas

Neste passo, construiremos um pipeline complexo com um transformador de colunas e um classificador, e exibiremos sua representação visual.

Primeiro, importamos os módulos necessários:

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
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
pipe = make_pipeline(preprocessor, LogisticRegression(max_iter=500))
```

Finalmente, exibimos a representação visual do pipeline:

```python
pipe
```
