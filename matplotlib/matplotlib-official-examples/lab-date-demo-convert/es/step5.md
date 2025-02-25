# Establecer el eje x y formatear las fechas

Para que el gráfico sea más legible, estableceremos los límites del eje x en la primera y última fechas del rango. También estableceremos los localizadores principales y secundarios en DayLocator y HourLocator, respectivamente. Finalmente, formatearemos las fechas utilizando la función DateFormatter. Copie y pegue el siguiente código:

```python
ax.set_xlim(dates[0], dates[-1])
ax.xaxis.set_major_locator(DayLocator())
ax.xaxis.set_minor_locator(HourLocator(range(0, 25, 6)))
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
```
