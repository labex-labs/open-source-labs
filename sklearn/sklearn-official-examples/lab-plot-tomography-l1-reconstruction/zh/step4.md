# 使用 L2 惩罚重建图像

在这一步中，我们将使用 L2（岭回归）惩罚来重建图像。

```python
rgr_ridge = Ridge(alpha=0.2)
rgr_ridge.fit(proj_operator, proj.ravel())
rec_l2 = rgr_ridge.coef_.reshape(l, l)
```
