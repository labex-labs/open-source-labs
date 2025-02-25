# Definir la función de paseo aleatorio

Definimos una función que genera un paseo aleatorio con un número dado de pasos y un tamaño máximo de paso. La función toma dos entradas: `num_steps` es el número total de pasos en el paseo aleatorio y `max_step` es el tamaño máximo de cada paso. Utilizamos `numpy.random` para generar números aleatorios para los pasos y `numpy.cumsum` para calcular la suma acumulativa de los pasos para obtener la posición final.

```python
def random_walk(num_steps, max_step=0.05):
    """Return a 3D random walk as (num_steps, 3) array."""
    start_pos = np.random.random(3)
    steps = np.random.uniform(-max_step, max_step, size=(num_steps, 3))
    walk = start_pos + np.cumsum(steps, axis=0)
    return walk
```
