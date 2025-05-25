# Ajustar Lasso a Dados Esparsos

Ajustamos os modelos de regressão Lasso aos dados esparsos usando a função `fit` do Scikit-learn. Também medimos o tempo do processo de ajuste e imprimimos o tempo para cada modelo Lasso.

```python
t0 = time()
sparse_lasso.fit(Xs_sp, y)
print(f"Sparse Lasso concluído em {(time() - t0):.3f}s")

t0 = time()
dense_lasso.fit(Xs, y)
print(f"Dense Lasso concluído em  {(time() - t0):.3f}s")
```
