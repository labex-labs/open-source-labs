# 制約なしでモデルをフィットさせる

制約なしで生成されたデータにモデルをフィットさせ、制約なしでモデルがどのように機能するかを確認します。

```python
gbdt_no_cst = HistGradientBoostingRegressor()
gbdt_no_cst.fit(X, y)
```
