# Construction d'une recherche en grille sur un pipeline avec un classifieur

Dans cette étape, nous allons construire une recherche en grille sur un pipeline avec un classifieur, et afficher sa représentation visuelle.

Tout d'abord, nous importons les modules nécessaires :

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
pipe = Pipeline(
    steps=[("preprocesseur", preprocesseur), ("classifieur", RandomForestClassifier())]
)
```

Ensuite, nous définissons la grille de paramètres pour la recherche en grille :

```python
param_grid = {
    "classifieur__n_estimators": [200, 500],
    "classifieur__max_features": ["auto", "sqrt", "log2"],
    "classifieur__max_depth": [4, 5, 6, 7, 8],
    "classifieur__criterion": ["gini", "entropie"],
}
```

Enfin, nous créons la recherche en grille :

```python
grid_search = GridSearchCV(pipe, param_grid=param_grid, n_jobs=1)
```

Et affichons la représentation visuelle de la recherche en grille :

```python
grid_search
```
