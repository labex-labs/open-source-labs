# Chargez l'ensemble de données

Ensuite, nous allons charger un ensemble de données d'échantillonnage pour démontrer les algorithmes de décomposition croisée. Pour simplifier, nous allons créer deux matrices `X` et `Y` avec des valeurs aléatoires.

```python
np.random.seed(0)
X = np.random.random((100, 5))
Y = np.random.random((100, 3))
```
