# Création des données

Nous allons créer un ensemble de données de 20 points, où les 10 premiers points appartiennent à la classe 1 et les 10 derniers points appartiennent à la classe -1.

```python
np.random.seed(0)
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
y = [1] * 10 + [-1] * 10
```
