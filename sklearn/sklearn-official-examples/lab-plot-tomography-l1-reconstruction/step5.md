# Reconstruct Image with L1 Penalization

In this step, we will reconstruct the image using L1 (Lasso) penalization.

```python
rgr_lasso = Lasso(alpha=0.001)
rgr_lasso.fit(proj_operator, proj.ravel())
rec_l1 = rgr_lasso.coef_.reshape(l, l)
```


