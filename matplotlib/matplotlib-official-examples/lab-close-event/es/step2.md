# Crear una figura y conectar el evento de cierre

En este paso, crearemos una figura y conectaremos el evento de cierre a la función `on_close` definida en el Paso 1. Esto se hace utilizando el método `mpl_connect` del lienzo de la figura.

```python
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close)
```
