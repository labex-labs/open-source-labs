# Daten erstellen

Wir werden 3D-Daten mit der `ogrid`-Funktion von NumPy erstellen.

```python
x, y, z = np.ogrid[-10:10:100j, -10:10:100j, 1:10:20j]
X = np.sin(x * y * z) / (x * y * z)
```
