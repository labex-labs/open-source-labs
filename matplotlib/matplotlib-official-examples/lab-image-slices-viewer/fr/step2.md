# Créez les données

Nous allons créer des données 3D en utilisant la fonction `ogrid` de NumPy.

```python
x, y, z = np.ogrid[-10:10:100j, -10:10:100j, 1:10:20j]
X = np.sin(x * y * z) / (x * y * z)
```
