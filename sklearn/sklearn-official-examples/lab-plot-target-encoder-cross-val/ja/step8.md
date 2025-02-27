# 交差検証を用いない線形モデルの係数を評価する

Ridge モデルは、有益な特徴量に比べてカーディナリティが非常に高い特徴量により多くの重みを割り当てるため、過学習（overfit）します。以下のコードを実行して、交差検証を用いない線形モデルの係数を評価してください。

```python
coefs_no_cv = pd.Series(
    model_no_cv.coef_, index=model_no_cv.feature_names_in_
).sort_values()
_ = coefs_no_cv.plot(kind="barh")
```
