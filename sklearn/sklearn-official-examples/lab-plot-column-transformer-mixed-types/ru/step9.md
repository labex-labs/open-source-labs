# Использовать ColumnTransformer для выбора столбцов по типам данных

В этом шаге мы будем использовать `ColumnTransformer` для выбора столбцов по типам данных. Мы будем использовать `make_column_selector` для выбора столбцов на основе их типов данных.

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
