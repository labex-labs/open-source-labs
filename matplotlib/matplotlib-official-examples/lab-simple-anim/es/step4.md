# Definir la función de animación

La función de animación será llamada por la función `FuncAnimation()` y se utilizará para actualizar el gráfico con nuevos datos. En este ejemplo, actualizaremos los valores del eje y del gráfico de líneas con una onda senoidal que tiene una amplitud que cambia con el tiempo.

```python
def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # actualizar los datos.
    return line,
```
