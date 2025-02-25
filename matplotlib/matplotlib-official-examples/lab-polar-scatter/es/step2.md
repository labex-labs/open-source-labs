# Generar datos aleatorios

Generaremos datos aleatorios para el diagrama de dispersión utilizando NumPy. Crearemos 150 puntos de datos con valores aleatorios de radio y ángulo, y calcularemos el área y el color de cada punto.

```python
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2
colors = theta
```
