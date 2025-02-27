# Crear un conjunto de datos aleatorio

En este paso, crearemos un conjunto de datos aleatorio. Utilizaremos la biblioteca `numpy` para crear una matriz ordenada de 100 elementos, con valores aleatorios entre 0 y 200, y luego restaremos 100 a cada elemento. Luego usaremos `numpy` para calcular el seno y el coseno de cada elemento, y uniremos estas matrices en una matriz bidimensional de forma (100, 2) para crear la matriz `y`. También agregaremos ruido aleatorio a cada quinto elemento.

```python
# Create a random dataset
rng = np.random.RandomState(1)
X = np.sort(200 * rng.rand(100, 1) - 100, axis=0)
y = np.array([np.pi * np.sin(X).ravel(), np.pi * np.cos(X).ravel()]).T
y[::5, :] += 0.5 - rng.rand(20, 2)
```
