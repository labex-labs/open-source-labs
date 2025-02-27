# Création d'un ensemble de données

Nous allons créer un ensemble de données avec 3 caractéristiques, où la première caractéristique a une relation linéaire avec la cible, la deuxième caractéristique a une relation non linéaire avec la cible et la troisième caractéristique est complètement inutile. Nous allons créer 1000 échantillons pour cet ensemble de données.

```python
np.random.seed(0)
X = np.random.rand(1000, 3)
y = X[:, 0] + np.sin(6 * np.pi * X[:, 1]) + 0.1 * np.random.randn(1000)
```
