# Générer des données

Ensuite, nous allons générer les données que nous utiliserons pour créer le tracé de trame. Dans ce laboratoire, nous utiliserons la fonction `np.meshgrid()` pour créer les coordonnées X, Y et Z.

```python
# Générer des données
X, Y = np.meshgrid(np.arange(-5, 5, 0.25), np.arange(-5, 5, 0.25))
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```
