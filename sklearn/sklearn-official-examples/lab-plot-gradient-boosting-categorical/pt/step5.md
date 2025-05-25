# Pipeline de Suporte Categórico Nativo

Criaremos um pipeline onde usaremos o suporte categórico nativo do estimador `HistGradientBoostingRegressor` para lidar com as características categóricas. Continuaremos a usar um `OrdinalEncoder` para pré-processar os dados.

```python
hist_native = make_pipeline(
    ordinal_encoder,
    HistGradientBoostingRegressor(
        random_state=42,
        categorical_features=categorical_columns,
    ),
).set_output(transform="pandas")
```
