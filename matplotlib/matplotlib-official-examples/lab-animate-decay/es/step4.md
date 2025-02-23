# Definir la función de inicialización

Necesitamos definir una función de inicialización que establezca el estado inicial de la trama. En esta función, estableceremos los límites del eje y y limpiaremos los datos del objeto de línea.

```python
def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 1)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,
```
