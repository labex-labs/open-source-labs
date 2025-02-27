# Créer l'ensemble de données

Dans cette étape, nous allons créer un ensemble de données avec une caractéristique d'entrée continue et une caractéristique de sortie continue. Nous utiliserons la méthode `numpy.random.RandomState()` pour générer des nombres aléatoires pour la caractéristique d'entrée, et la méthode `numpy.sin()` pour générer la caractéristique de sortie.

```python
rnd = np.random.RandomState(42)
X = rnd.uniform(-3, 3, size=100)
y = np.sin(X) + rnd.normal(size=len(X)) / 3
X = X.reshape(-1, 1)
```
