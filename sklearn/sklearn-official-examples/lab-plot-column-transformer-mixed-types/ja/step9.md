# データ型に基づいて列を選択してColumnTransformerを使用する

このステップでは、データ型に基づいて列を選択して`ColumnTransformer`を使用します。列を選択するために`make_column_selector`を使用します。

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
