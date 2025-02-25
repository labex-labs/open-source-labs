# Crear datos para el gráfico

A continuación, creemos algunos datos que utilizaremos para trazar. Utilizaremos la función `numpy.arange()` para crear una matriz de valores del 0 al 14 y almacenarla en la variable `x`. También utilizaremos la función `numpy.sin()` para crear una matriz de valores que son el seno de cada valor en `x` dividido por 2, y almacenarla en la variable `y`.

```python
x = np.arange(14)
y = np.sin(x / 2)
```
