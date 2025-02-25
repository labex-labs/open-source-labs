# Preparar los datos

En este paso, se preparan los datos para el gráfico. Crearemos una lista con los nombres de las personas, su rendimiento y la tasa de error.

```python
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))
```
