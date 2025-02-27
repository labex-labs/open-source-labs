# 交差検証を用いた線形モデルの係数を評価する

線形モデルの係数は、ほとんどの重みが列インデックス 0 の特徴量（有益な特徴量）にあることを示しています。以下のコードを実行して、交差検証を用いた線形モデルの係数を評価してください。

```python
coefs_cv = pd.Series(
    model_with_cv[-1].coef_, index=model_with_cv[-1].feature_names_in_
).sort_values()
_ = coefs_cv.plot(kind="barh")
```
