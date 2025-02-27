# Reconstruir imagen con penalización L2

En este paso, reconstruiremos la imagen utilizando la penalización L2 (Ridge).

```python
rgr_ridge = Ridge(alpha=0.2)
rgr_ridge.fit(proj_operator, proj.ravel())
rec_l2 = rgr_ridge.coef_.reshape(l, l)
```
