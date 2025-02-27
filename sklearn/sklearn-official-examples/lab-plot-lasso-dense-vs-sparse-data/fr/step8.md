# Ajuster Lasso aux données creuses

Nous ajustons les modèles de régression Lasso aux données creuses en utilisant la fonction `fit` de Scikit-learn. Nous mesurons également le temps d'ajustement et affichons le temps pour chaque modèle Lasso.

```python
t0 = time()
sparse_lasso.fit(Xs_sp, y)
print(f"Sparse Lasso effectué en {(time() - t0):.3f}s")

t0 = time()
dense_lasso.fit(Xs, y)
print(f"Dense Lasso effectué en  {(time() - t0):.3f}s")
```
