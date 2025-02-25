# Créez une figure 3D et des données

Dans cette étape, nous allons créer une figure 3D et obtenir des données de test pour le tracé de surface.

```python
# Créez une figure 3D
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Obtenez des données de test pour le tracé de surface
X, Y, Z = axes3d.get_test_data(0.05)
```
