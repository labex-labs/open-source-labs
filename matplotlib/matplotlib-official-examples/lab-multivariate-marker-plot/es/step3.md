# Generar datos aleatorios

En este paso, generará datos aleatorios para la habilidad del lanzador, el ángulo de despegue, la fuerza, el éxito y la posición. En particular, generará 25 puntos de datos para cada variable, excepto para la posición, que tendrá 2 coordenadas para cada punto de datos.

```python
N = 25
np.random.seed(42)
skills = np.random.uniform(5, 80, size=N) * 0.1 + 5
takeoff_angles = np.random.normal(0, 90, N)
thrusts = np.random.uniform(size=N)
successful = np.random.randint(0, 3, size=N)
positions = np.random.normal(size=(N, 2)) * 5
data = zip(skills, takeoff_angles, thrusts, successful, positions)
```
