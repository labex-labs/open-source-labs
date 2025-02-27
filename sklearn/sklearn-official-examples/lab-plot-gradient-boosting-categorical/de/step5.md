# Pipeline mit nativer Kategorienunterstützung

Wir werden eine Pipeline erstellen, in der wir die native Kategorienunterstützung des HistGradientBoostingRegressor-Schätzers verwenden, um kategorische Merkmale zu behandeln. Wir werden weiterhin einen OrdinalEncoder verwenden, um die Daten vorzubereiten.

```python
hist_native = make_pipeline(
    ordinal_encoder,
    HistGradientBoostingRegressor(
        random_state=42,
        categorical_features=categorical_columns,
    ),
).set_output(transform="pandas")
```
