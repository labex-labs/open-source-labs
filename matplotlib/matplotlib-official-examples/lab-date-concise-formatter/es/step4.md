# Localización de formatos de fecha

Los formatos de fecha se pueden localizar si los formatos predeterminados no son deseados mediante la manipulación de una de tres listas de cadenas. Modificamos las etiquetas para que sean "día mes año", en lugar del estándar ISO "año mes día".

```python
fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))

for nn, ax in enumerate(axs):
    locator = mdates.AutoDateLocator()
    formatter = mdates.ConciseDateFormatter(locator)
    formatter.formats = ['%y',  # ticks son en su mayoría años
                         '%b',       # ticks son en su mayoría meses
                         '%d',       # ticks son en su mayoría días
                         '%H:%M',    # horas
                         '%H:%M',    # minutos
                         '%S.%f', ]  # segundos
    # estos son en su mayoría solo el nivel superior...
    formatter.zero_formats = [''] + formatter.formats[:-1]
    #...excepto para los ticks que son en su mayoría horas, entonces es bueno tener
    # día-mes:
    formatter.zero_formats[3] = '%d-%b'

    formatter.offset_formats = ['',
                                '%Y',
                                '%b %Y',
                                '%d %b %Y',
                                '%d %b %Y',
                                '%d %b %Y %H:%M', ]
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
axs[0].set_title('Concise Date Formatter')
plt.show()
```
