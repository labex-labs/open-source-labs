# Definir los métodos `fill` y `plot`

Dentro de la clase `RadarAxes`, definiremos los métodos `fill` y `plot`. Estos métodos se utilizarán para llenar el área dentro del gráfico y trazar los puntos de datos, respectivamente.

```python
class RadarAxes(PolarAxes):
    # código de la clase RadarAxes va aquí

    def fill(self, *args, closed=True, **kwargs):
        # sobrescribir el método fill
        return super().fill(closed=closed, *args, **kwargs)

    def plot(self, *args, **kwargs):
        # sobrescribir el método plot
        lines = super().plot(*args, **kwargs)
        for line in lines:
            self._close_line(line)

    def _close_line(self, line):
        # método auxiliar para cerrar la línea
        x, y = line.get_data()
        if x[0]!= x[-1]:
            x = np.append(x, x[0])
            y = np.append(y, y[0])
            line.set_data(x, y)
```
