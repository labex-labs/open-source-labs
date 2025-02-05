# 使用 L1 惩罚重建图像

在这一步中，我们将使用 L1（套索）惩罚来重建图像。

```python
rgr_lasso = Lasso(alpha=0.001)
rgr_lasso.fit(proj_operator, proj.ravel())
rec_l1 = rgr_lasso.coef_.reshape(l, l)
```
