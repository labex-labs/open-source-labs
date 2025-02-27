# Générer des données synthétiques

Ensuite, générons quelques données synthétiques avec lesquelles travailler. Nous allons créer une fonction cible sinusoïdale et y ajouter du bruit aléatoire.

```python
# Generate input data
np.random.seed(0)
X = np.sort(5 * np.random.rand(100, 1), axis=0)
y = np.sin(X).ravel()
y += 0.5 * (0.5 - np.random.rand(y.size))
```
