# Native Categorical Support Pipeline

We will create a pipeline where we use the native categorical support of the HistGradientBoostingRegressor estimator to handle categorical features. We will still use an OrdinalEncoder to pre-process the data.

```python
hist_native = make_pipeline(
    ordinal_encoder,
    HistGradientBoostingRegressor(
        random_state=42,
        categorical_features=categorical_columns,
    ),
).set_output(transform="pandas")
```


