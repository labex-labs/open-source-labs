# Setze die Haupt- und Nebenmarkierer und -formatter

Um die Beschriftungen zwischen den Strichen zu zentrieren, müssen wir die Haupt- und Nebenmarkierer und -formatter für die x-Achse festlegen. Wir werden die `dates.MonthLocator()`-Funktion verwenden, um die Haupt- und Nebenmarkierer auf den Monat festzulegen, und die `dates.DateFormatter()`-Funktion, um die Nebenstrichbeschriftungen in die Monatskürzel zu formatieren.

```python
import matplotlib.dates as dates
import matplotlib.ticker as ticker

ax.xaxis.set_major_locator(dates.MonthLocator())
# 16 ist eine leichte Näherung, da die Monate in der Anzahl der Tage unterschiedlich sind.
ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=16))

ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
```
