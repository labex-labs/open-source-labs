# Crear una figura y agregar un eje principal

Creamos una figura utilizando el método `plt.figure()` y agregamos un eje principal utilizando el método `fig.add_axes()`. El eje principal comparte la escala en x con el eje parasito.

```python
fig = plt.figure()
host = fig.add_axes([0.15, 0.1, 0.65, 0.8], axes_class=HostAxes)
```
