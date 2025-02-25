# Lokalisierung von Datumsformaten

Datumsformate können lokalisiert werden, wenn die Standardformate nicht erwünscht sind, indem man eine von drei Zeichenkettenlisten manipuliert. Wir ändern die Beschriftungen zu "Tag Monat Jahr" anstelle des ISO-Standards "Jahr Monat Tag".

```python
fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))

for nn, ax in enumerate(axs):
    locator = mdates.AutoDateLocator()
    formatter = mdates.ConciseDateFormatter(locator)
    formatter.formats = ['%y',  # Die Markierungen sind meistens Jahre
                         '%b',       # Die Markierungen sind meistens Monate
                         '%d',       # Die Markierungen sind meistens Tage
                         '%H:%M',    # Stunden
                         '%H:%M',    # Minuten
                         '%S.%f', ]  # Sekunden
    # Dies sind hauptsächlich die Ebene darüber...
    formatter.zero_formats = [''] + formatter.formats[:-1]
    #...außer für Markierungen, die meistens Stunden sind, dann ist es schön,
    # Monat-Tag zu haben:
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
