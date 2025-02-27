# Definiere den Vorverarbeiter

In diesem Schritt definieren wir den `ColumnTransformer`, der zur Vorverarbeitung unserer Daten verwendet werden wird.

```python
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)
```
