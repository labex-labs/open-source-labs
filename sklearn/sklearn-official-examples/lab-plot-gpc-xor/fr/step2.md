# Création de l'ensemble de données XOR

Dans cette étape, nous allons créer un ensemble de données XOR à l'aide de numpy. Nous utiliserons la fonction logical_xor pour créer des étiquettes basées sur les caractéristiques d'entrée.

```python
xx, yy = np.meshgrid(np.linspace(-3, 3, 50), np.linspace(-3, 3, 50))
rng = np.random.RandomState(0)
X = rng.randn(200, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
```
