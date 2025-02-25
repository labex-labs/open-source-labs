# Registrar un conversor con localización

También podemos registrar un conversor con localización pasando argumentos de palabras clave a `~.dates.ConciseDateConverter` y registrando los tipos de datos que se utilizarán con el registro de unidades.

```python
import datetime

formats = ['%y',          # ticks son en su mayoría años
           '%b',     # ticks son en su mayoría meses
           '%d',     # ticks son en su mayoría días
           '%H:%M',  # horas
           '%H:%M',  # minutos
           '%S.%f', ]  # segundos
# estos pueden ser los mismos, excepto desplazados un nivel....
zero_formats = [''] + formats[:-1]
#...excepto para los ticks que son en su mayoría horas, entonces es bueno tener día-mes
zero_formats[3] = '%d-%b'
offset_formats = ['',
                  '%Y',
                  '%b %Y',
                  '%d %b %Y',
                  '%d %b %Y',
                  '%d %b %Y %H:%M', ]

converter = mdates.ConciseDateConverter(
    formats=formats, zero_formats=zero_formats, offset_formats=offset_formats)

munits.registry[np.datetime64] = converter
munits.registry[datetime.date] = converter
munits.registry[datetime.datetime] = converter

fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))
for nn, ax in enumerate(axs):
    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
axs[0].set_title('Concise Date Formatter registered non-default')
plt.show()
```
