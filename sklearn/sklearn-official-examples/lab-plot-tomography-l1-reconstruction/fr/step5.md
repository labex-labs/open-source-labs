# Reconstruction d'une image avec pénalisation L1

Dans cette étape, nous allons reconstruire l'image en utilisant la pénalisation L1 (Lasso).

```python
rgr_lasso = Lasso(alpha=0.001)
rgr_lasso.fit(proj_operator, proj.ravel())
rec_l1 = rgr_lasso.coef_.reshape(l, l)
```
