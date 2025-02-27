# 推定係数の比較

真のモデル、線形モデル、および RANSAC 回帰器の推定係数を比較します。

```python
# Compare estimated coefficients
print("Estimated coefficients (true, linear regression, RANSAC):")
print(coef, lr.coef_, ransac.estimator_.coef_)
```
