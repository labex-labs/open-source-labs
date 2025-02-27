# Конвейер с встроенной поддержкой категориальных признаков

Мы создадим конвейер, в котором мы будем использовать встроенную поддержку категориальных признаков у оценщика HistGradientBoostingRegressor для обработки категориальных признаков. Мы по-прежнему будем использовать OrdinalEncoder для предварительной обработки данных.

```python
hist_native = make_pipeline(
    ordinal_encoder,
    HistGradientBoostingRegressor(
        random_state=42,
        categorical_features=categorical_columns,
    ),
).set_output(transform="pandas")
```
