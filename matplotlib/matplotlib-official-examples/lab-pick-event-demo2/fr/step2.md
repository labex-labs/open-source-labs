# Calculer la moyenne et l'écart-type

Ensuite, nous allons calculer la moyenne et l'écart-type de chacun des 100 jeux de données. Nous utiliserons les fonctions `mean` et `std` de `numpy` pour calculer ces valeurs.

```python
xs = np.mean(X, axis=1)
ys = np.std(X, axis=1)
```
