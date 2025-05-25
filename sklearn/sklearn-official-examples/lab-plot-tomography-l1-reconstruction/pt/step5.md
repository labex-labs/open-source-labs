# Reconstruir Imagem com Penalização L1

Neste passo, reconstruiremos a imagem utilizando penalização L1 (Lasso).

```python
rgr_lasso = Lasso(alpha=0.001)
rgr_lasso.fit(proj_operator, proj.ravel())
rec_l1 = rgr_lasso.coef_.reshape(l, l)
```
