# Générer des données creuses

Ensuite, nous générons quelques données creuses que nous utiliserons pour la régression Lasso. Nous copions les données denses de l'étape précédente et remplaçons toutes les valeurs inférieures à 2,5 par 0. Nous convertissons également les données creuses au format Compressed Sparse Column de Scipy.

```python
Xs = X.copy()
Xs[Xs < 2.5] = 0.0
Xs_sp = sparse.coo_matrix(Xs)
Xs_sp = Xs_sp.tocsc()
```
