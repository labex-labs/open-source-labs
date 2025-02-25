# Définir la direction des flèches

Maintenant, nous allons définir la direction des flèches. Dans cet exemple, nous allons définir la direction des flèches à l'aide des fonctions trigonométriques de NumPy. Les fonctions `sin` et `cos` sont utilisées pour créer les tableaux `u`, `v` et `w` qui représentent la direction des flèches dans les directions `x`, `y` et `z`.

```python
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))
```
