# Préparer le jeu de données

Nous devons aplatir les images pour transformer chaque tableau 2D de valeurs d'échelle de gris de forme `(8, 8)` en forme `(64,)`. Cela nous donnera un jeu de données de forme `(n_samples, n_features)`, où `n_samples` est le nombre d'images et `n_features` est le nombre total de pixels dans chaque image.

```python
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
```
