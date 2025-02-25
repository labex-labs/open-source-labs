# Establecer los localizadores y formatos principales y secundarios

Para centrar las etiquetas entre las marcas de graduación, necesitamos establecer los localizadores y formatos principales y secundarios para el eje x. Utilizaremos la función `dates.MonthLocator()` para establecer los localizadores principales y secundarios en el mes y la función `dates.DateFormatter()` para formatear las etiquetas de las marcas de graduación menores con la abreviatura del mes.

```python
import matplotlib.dates as dates
import matplotlib.ticker as ticker

ax.xaxis.set_major_locator(dates.MonthLocator())
# 16 es una aproximación leve ya que los meses difieren en el número de días.
ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=16))

ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
```
