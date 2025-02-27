# Generar datos dispersos

A continuación, generamos algunos datos dispersos que usaremos para la regresión Lasso. Copiamos los datos densos del paso anterior y reemplazamos todos los valores menores que 2.5 por 0. También convertimos los datos dispersos al formato Compressed Sparse Column de Scipy.

```python
Xs = X.copy()
Xs[Xs < 2.5] = 0.0
Xs_sp = sparse.coo_matrix(Xs)
Xs_sp = Xs_sp.tocsc()
```
