# Création des données

L'étape suivante consiste à créer les données pour la surface 3D. Nous devons définir `u`, `v`, `x`, `y` et `z`. Ces variables représenteront les angles et les coordonnées nécessaires pour tracer la surface. La fonction `linspace()` de NumPy est utilisée pour créer les angles, et la fonction `outer()` est utilisée pour créer les coordonnées.

```python
# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
```
