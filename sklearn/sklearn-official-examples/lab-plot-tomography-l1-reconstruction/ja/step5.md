# L1 罰則を用いた画像の再構築

このステップでは、L1（Lasso）罰則を用いて画像を再構築します。

```python
rgr_lasso = Lasso(alpha=0.001)
rgr_lasso.fit(proj_operator, proj.ravel())
rec_l1 = rgr_lasso.coef_.reshape(l, l)
```
