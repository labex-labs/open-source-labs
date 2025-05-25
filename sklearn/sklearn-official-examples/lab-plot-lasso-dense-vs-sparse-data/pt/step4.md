# Ajustar Lasso a Dados Densos

Ajustamos os modelos de regressão Lasso aos dados densos usando a função `fit` do Scikit-learn. Também medimos o tempo do processo de ajuste e imprimimos o tempo para cada modelo Lasso.

```python
t0 = time()
sparse_lasso.fit(X_sp, y)
print(f"Sparse Lasso concluído em {(time() - t0):.3f}s")

t0 = time()
dense_lasso.fit(X, y)
print(f"Dense Lasso concluído em {(time() - t0):.3f}s")
```
