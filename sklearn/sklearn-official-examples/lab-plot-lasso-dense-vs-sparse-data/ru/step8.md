# Применяем Lasso к разреженным данным

Мы применяем модели Lasso-регрессии к разреженным данным с использованием функции `fit` из Scikit-learn. Также мы засекаем время процесса подгонки и выводим время для каждой модели Lasso.

```python
t0 = time()
sparse_lasso.fit(Xs_sp, y)
print(f"Sparse Lasso done in {(time() - t0):.3f}s")

t0 = time()
dense_lasso.fit(Xs, y)
print(f"Dense Lasso done in  {(time() - t0):.3f}s")
```
