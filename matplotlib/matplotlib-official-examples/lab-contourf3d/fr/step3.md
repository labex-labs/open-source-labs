# Générez les données

Nous allons maintenant générer les données à utiliser dans le tracé de contour 3D. Nous utiliserons la méthode `axes3d.get_test_data()` pour générer les données. Cette méthode génère des données de test pour un tracé 3D.

```python
X, Y, Z = axes3d.get_test_data(0.05)
```
