# Generar datos sintéticos

A continuación, generemos algunos datos sintéticos con los que trabajar. Crearemos una función objetivo senoidal y le agregaremos algo de ruido aleatorio.

```python
# Generate input data
np.random.seed(0)
X = np.sort(5 * np.random.rand(100, 1), axis=0)
y = np.sin(X).ravel()
y += 0.5 * (0.5 - np.random.rand(y.size))
```
