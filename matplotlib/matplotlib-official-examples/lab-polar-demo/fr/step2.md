# Générez les données

Ensuite, nous devons générer les données pour le graphique en ligne. Nous utiliserons la bibliothèque `numpy` pour générer un tableau de valeurs pour `r` et `theta`.

```python
r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
```
