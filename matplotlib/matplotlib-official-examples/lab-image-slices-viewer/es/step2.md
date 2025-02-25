# Crear los datos

Vamos a crear datos tridimensionales utilizando la función `ogrid` de NumPy.

```python
x, y, z = np.ogrid[-10:10:100j, -10:10:100j, 1:10:20j]
X = np.sin(x * y * z) / (x * y * z)
```
