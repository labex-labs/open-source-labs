# Crear conjunto de datos

Crearemos un conjunto de datos con 3 características, donde la primera característica tiene una relación lineal con la variable objetivo, la segunda característica tiene una relación no lineal con la variable objetivo y la tercera característica es completamente irrelevante. Crearemos 1000 muestras para este conjunto de datos.

```python
np.random.seed(0)
X = np.random.rand(1000, 3)
y = X[:, 0] + np.sin(6 * np.pi * X[:, 1]) + 0.1 * np.random.randn(1000)
```
