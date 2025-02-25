# Création des données

Ensuite, nous devons créer les données que nous utiliserons pour tracer les lignes. Nous utiliserons `numpy` pour créer un tableau 2D de valeurs `x` et `y`.

```python
x = np.arange(100)
ys = x[:50, np.newaxis] + x[np.newaxis, :]
```
