# Definir la función de animación

Ahora, necesitamos definir la función que actualizará la trama para cada fotograma de la animación. Esta función tomará los datos generados por la función `data_gen()` y actualizará la trama con los nuevos datos. También actualizaremos los límites del eje x a medida que avanza la animación.

```python
def run(data):
    # actualizar los datos
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,
```
