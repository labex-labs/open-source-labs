# 定义数据预处理步骤

在这一步中，我们将定义用于预处理数据的 `ColumnTransformer`。

```python
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)
```
