# Reconstruction d'une image avec pénalisation L2

Dans cette étape, nous allons reconstruire l'image en utilisant la pénalisation L2 (Ridge).

```python
rgr_ridge = Ridge(alpha=0.2)
rgr_ridge.fit(proj_operator, proj.ravel())
rec_l2 = rgr_ridge.coef_.reshape(l, l)
```
