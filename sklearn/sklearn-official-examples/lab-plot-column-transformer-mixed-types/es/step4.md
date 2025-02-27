# Definir el preprocesador

En este paso, definiremos el `ColumnTransformer` que se utilizará para preprocesar nuestros datos.

```python
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)
```
