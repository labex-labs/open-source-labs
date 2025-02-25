# Crear los botones `Siguiente` y `Anterior`

Ahora, crearemos los botones `Siguiente` y `Anterior` utilizando la función `add_axes` de `matplotlib.pyplot`, y les asignaremos las funciones de devolución de llamada que creamos anteriormente utilizando `on_clicked`.

```python
axprev = fig.add_axes([0.7, 0.05, 0.1, 0.075])
axnext = fig.add_axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)
```
