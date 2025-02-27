# 密集Lassoと疎Lassoの係数を比較する

密集Lassoモデルと疎Lassoモデルの係数を比較して、同じ結果が得られていることを確認します。係数の差のユークリッドノルムを計算します。

```python
coeff_diff = linalg.norm(sparse_lasso.coef_ - dense_lasso.coef_)
print(f"Distance between coefficients : {coeff_diff:.2e}")
```
