# 比较密集 Lasso 和稀疏 Lasso 的系数

我们比较密集 Lasso 模型和稀疏 Lasso 模型的系数，以确保它们产生相同的结果。我们计算系数之间差异的欧几里得范数。

```python
coeff_diff = linalg.norm(sparse_lasso.coef_ - dense_lasso.coef_)
print(f"Distance between coefficients : {coeff_diff:.2e}")
```
