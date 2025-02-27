# Spärliche Daten generieren

Als nächstes generieren wir einige spärliche Daten, die wir für die Lasso-Regression verwenden werden. Wir kopieren die dichten Daten aus dem vorherigen Schritt und ersetzen alle Werte, die kleiner als 2,5 sind, durch 0. Wir konvertieren auch die spärlichen Daten in das Compressed Sparse Column-Format von Scipy.

```python
Xs = X.copy()
Xs[Xs < 2.5] = 0.0
Xs_sp = sparse.coo_matrix(Xs)
Xs_sp = Xs_sp.tocsc()
```
