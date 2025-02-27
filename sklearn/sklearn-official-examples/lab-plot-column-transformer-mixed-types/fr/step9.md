# Utiliser ColumnTransformer pour sélectionner des colonnes en fonction des types de données

Dans cette étape, nous allons utiliser `ColumnTransformer` pour sélectionner des colonnes en fonction de leurs types de données. Nous allons utiliser `make_column_selector` pour sélectionner des colonnes en fonction de leurs types de données.

```python
from sklearn.compose import make_column_selector as selector

subset_feature = ["embarked", "sex", "pclass", "age", "fare"]
X_train, X_test = X_train[subset_feature], X_test[subset_feature]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, selector(dtype_exclude="category")),
        ("cat", categorical_transformer, selector(dtype_include="category")),
    ]
)
clf = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression())]
)
```
