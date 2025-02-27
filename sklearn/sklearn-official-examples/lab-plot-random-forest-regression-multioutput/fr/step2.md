# Création d'un ensemble de données aléatoire

Ensuite, nous allons créer un ensemble de données aléatoire pour notre régression. Nous utiliserons `numpy` pour créer un ensemble de 600 valeurs de x entre -100 et 100, et les valeurs de y correspondantes calculées à partir de la fonction sinus et cosinus des valeurs de x plus un certain bruit aléatoire.

```python
rng = np.random.RandomState(1)
X = np.sort(200 * rng.rand(600, 1) - 100, axis=0)
y = np.array([np.pi * np.sin(X).ravel(), np.pi * np.cos(X).ravel()]).T
y += 0.5 - rng.rand(*y.shape)
```
