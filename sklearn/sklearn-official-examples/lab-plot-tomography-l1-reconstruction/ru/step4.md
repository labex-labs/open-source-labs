# реконструкция изображения с использованием штрафования L2

В этом шаге мы будем реконструировать изображение с использованием штрафования L2 (Ridge).

```python
rgr_ridge = Ridge(alpha=0.2)
rgr_ridge.fit(proj_operator, proj.ravel())
rec_l2 = rgr_ridge.coef_.reshape(l, l)
```
