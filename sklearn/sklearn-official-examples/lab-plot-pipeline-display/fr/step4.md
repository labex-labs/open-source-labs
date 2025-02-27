# Construction d'un pipeline complexe enchaînant un ColumnTransformer

Dans cette étape, nous allons construire un pipeline complexe avec un ColumnTransformer et un classifieur, et afficher sa représentation visuelle.

Tout d'abord, nous importons les modules nécessaires :

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
```

Ensuite, nous définissons les étapes de prétraitement pour les caractéristiques numériques et catégorielles :

```python
preprocesseur_numerique = Pipeline(
    steps=[
        ("imputation_moyenne", SimpleImputer(missing_values=np.nan, strategy="mean")),
        ("scalage", StandardScaler()),
    ]
)

preprocesseur_categorique = Pipeline(
    steps=[
        (
            "imputation_constante",
            SimpleImputer(fill_value="manquant", strategy="constant"),
        ),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ]
)
```

Ensuite, nous créons le ColumnTransformer :

```python
preprocesseur = ColumnTransformer(
    [
        ("catégorique", preprocesseur_categorique, ["état", "genre"]),
        ("numérique", preprocesseur_numerique, ["âge", "poids"]),
    ]
)
```

Ensuite, nous créons le pipeline :

```python
pipe = make_pipeline(preprocesseur, LogisticRegression(max_iter=500))
```

Enfin, nous affichons la représentation visuelle du pipeline :

```python
pipe
```
