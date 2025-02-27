# Création d'un ensemble de données aléatoire

Dans cette étape, nous allons créer un ensemble de données aléatoire. Nous utiliserons la bibliothèque `numpy` pour créer un tableau trié de 100 éléments, avec des valeurs aléatoires comprises entre 0 et 200, puis soustraire 100 à chaque élément. Ensuite, nous utiliserons `numpy` pour calculer le sinus et le cosinus de chaque élément, et joindre ces tableaux ensemble pour former un tableau 2D de forme (100, 2) pour créer le tableau `y`. Nous ajouterons également du bruit aléatoire à chaque cinquième élément.

```python
# Create a random dataset
rng = np.random.RandomState(1)
X = np.sort(200 * rng.rand(100, 1) - 100, axis=0)
y = np.array([np.pi * np.sin(X).ravel(), np.pi * np.cos(X).ravel()]).T
y[::5, :] += 0.5 - rng.rand(20, 2)
```
