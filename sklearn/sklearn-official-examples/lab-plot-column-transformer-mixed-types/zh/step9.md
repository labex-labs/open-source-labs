# 通过数据类型选择列来使用 ColumnTransformer

在这一步中，我们将通过按数据类型选择列来使用 `ColumnTransformer`。我们将使用 `make_column_selector` 根据数据类型选择列。

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
