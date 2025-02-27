# Ajustar Lasso a datos densos

Ajustamos los modelos de regresión Lasso a los datos densos utilizando la función `fit` de Scikit-learn. También medimos el tiempo del proceso de ajuste y mostramos el tiempo para cada modelo Lasso.

```python
t0 = time()
sparse_lasso.fit(X_sp, y)
print(f"Sparse Lasso hecho en {(time() - t0):.3f}s")

t0 = time()
dense_lasso.fit(X, y)
print(f"Dense Lasso hecho en {(time() - t0):.3f}s")
```
