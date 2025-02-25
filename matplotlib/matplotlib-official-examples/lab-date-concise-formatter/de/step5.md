# Registrieren eines Konverters mit Lokalisierung

Wir können auch einen Konverter mit Lokalisierung registrieren, indem wir Schlüsselwortargumente an `~.dates.ConciseDateConverter` übergeben und die Datentypen, die wir verwenden werden, mit der Einheitenregistrierung registrieren.

```python
import datetime

formats = ['%y',          # Die Markierungen sind meistens Jahre
           '%b',     # Die Markierungen sind meistens Monate
           '%d',     # Die Markierungen sind meistens Tage
           '%H:%M',  # Stunden
           '%H:%M',  # Minuten
           '%S.%f', ]  # Sekunden
# Dies können die gleichen sein, nur um eine Ebene verschoben...
zero_formats = [''] + formats[:-1]
#...außer für Markierungen, die meistens Stunden sind, dann ist es schön, Monat-Tag zu haben
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
