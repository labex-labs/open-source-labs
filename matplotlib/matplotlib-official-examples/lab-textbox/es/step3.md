# Definir la función de envío

Definimos la función `submit` que se llamará cuando el usuario envíe la entrada de texto. Esta función actualiza la función trazada en función de la entrada del usuario.

```python
def submit(expression):
    """
    Actualiza la función trazada a la nueva *expresión* matemática.

    *expresión* es una cadena que utiliza "t" como variable independiente, por ejemplo
    "t ** 3".
    """
    ydata = eval(expression, {'np': np}, {'t': t})
    l.set_ydata(ydata)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
```
