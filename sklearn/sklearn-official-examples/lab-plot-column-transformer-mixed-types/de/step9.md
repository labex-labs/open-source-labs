# Verwende ColumnTransformer, um Spalten nach Datentypen auszuwählen

In diesem Schritt werden wir `ColumnTransformer` verwenden, um Spalten nach Datentypen auszuwählen. Wir werden `make_column_selector` verwenden, um Spalten basierend auf ihren Datentypen auszuwählen.

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
