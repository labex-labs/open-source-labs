# L2 罰則を用いた画像の再構築

このステップでは、L2（Ridge）罰則を用いて画像を再構築します。

```python
rgr_ridge = Ridge(alpha=0.2)
rgr_ridge.fit(proj_operator, proj.ravel())
rec_l2 = rgr_ridge.coef_.reshape(l, l)
```
