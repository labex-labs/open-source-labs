# Reconstruct Image with L2 Penalization

In this step, we will reconstruct the image using L2 (Ridge) penalization.

```python
rgr_ridge = Ridge(alpha=0.2)
rgr_ridge.fit(proj_operator, proj.ravel())
rec_l2 = rgr_ridge.coef_.reshape(l, l)
```


