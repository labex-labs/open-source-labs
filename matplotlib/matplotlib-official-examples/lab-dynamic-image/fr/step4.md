# Générer les données

Nous utiliserons la méthode linspace de la bibliothèque Numpy pour générer les données de l'animation. Nous allons générer deux ensembles de données, x et y, puis redimensionner les données y pour créer un tableau à deux dimensions.

```python
x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
```
