# Определение препроцессора

В этом шаге мы определим `ColumnTransformer`, который будет использоваться для предварительной обработки наших данных.

```python
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)
```
