# Generar datos

En este paso, generamos puntos de datos aleatorios utilizando numpy.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Generate random data points
x, y = 4*(np.random.rand(2, 100) -.5)
```
