# Définir le prétraitement

Dans cette étape, nous allons définir le `ColumnTransformer` qui sera utilisé pour prétraiter nos données.

```python
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)
```
