# Usar un objeto llamable para el formateador

En lugar de pasar una función a `.Axis.set_major_formatter`, podemos usar cualquier otro objeto llamable, como una instancia de una clase que implemente `__call__`. En este paso, crearemos una clase `MyFormatter` que formatea las marcas de graduación como fechas.

```python
# Usar un objeto llamable para el formateador
class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%a'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        """Devuelve la etiqueta para el tiempo x en la posición pos."""
        try:
            return self.dates[round(x)].item().strftime(self.fmt)
        except IndexError:
            pass

ax2.xaxis.set_major_formatter(MyFormatter(r.date, '%a'))
```
