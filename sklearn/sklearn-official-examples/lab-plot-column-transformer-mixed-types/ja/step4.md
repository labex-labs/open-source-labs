# 前処理器を定義する

このステップでは、データを前処理するために使用する `ColumnTransformer` を定義します。

```python
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)
```
