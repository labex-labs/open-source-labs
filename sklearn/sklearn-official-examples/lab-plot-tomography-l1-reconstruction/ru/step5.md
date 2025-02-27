# реконструкция изображения с использованием штрафования L1

В этом шаге мы будем реконструировать изображение с использованием штрафования L1 (Lasso).

```python
rgr_lasso = Lasso(alpha=0.001)
rgr_lasso.fit(proj_operator, proj.ravel())
rec_l1 = rgr_lasso.coef_.reshape(l, l)
```
