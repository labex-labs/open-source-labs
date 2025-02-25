# Creando la animación

El último paso es crear la animación. Hacemos esto utilizando la función `FuncAnimation` del módulo `animation`. Esta función toma varios argumentos, incluyendo el objeto de figura, la función que actualizará el diagrama y el número de fotogramas a utilizar.

```python
def animate(i):
    scat.set_offsets((x[i], 0))
    return scat,

ani = animation.FuncAnimation(fig, animate, repeat=True,
                                    frames=len(x) - 1, interval=50)
```
