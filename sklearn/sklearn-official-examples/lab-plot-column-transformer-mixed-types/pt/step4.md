# Definir o Pré-processador

Neste passo, definiremos o `ColumnTransformer` que será utilizado para pré-processar os nossos dados.

```python
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)
```
