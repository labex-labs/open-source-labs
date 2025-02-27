# Tubo de soporte nativo para variables categóricas

Crearemos un tubo en el que usaremos el soporte nativo para variables categóricas del estimador HistGradientBoostingRegressor para manejar las características categóricas. Todavía usaremos un OrdinalEncoder para pre-procesar los datos.

```python
hist_native = make_pipeline(
    ordinal_encoder,
    HistGradientBoostingRegressor(
        random_state=42,
        categorical_features=categorical_columns,
    ),
).set_output(transform="pandas")
```
