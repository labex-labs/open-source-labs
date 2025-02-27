# ネイティブカテゴリカルサポートパイプライン

HistGradientBoostingRegressor推定器のネイティブカテゴリカルサポートを使ってカテゴリカル特徴を処理するパイプラインを作成します。データの前処理には依然としてOrdinalEncoderを使用します。

```python
hist_native = make_pipeline(
    ordinal_encoder,
    HistGradientBoostingRegressor(
        random_state=42,
        categorical_features=categorical_columns,
    ),
).set_output(transform="pandas")
```
