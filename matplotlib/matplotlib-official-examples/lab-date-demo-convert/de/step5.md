# Setzen der x-Achse und Formatieren der Daten

Um den Graphen lesbarer zu machen, setzen wir die Grenzen der x-Achse auf das erste und das letzte Datum im Bereich. Wir setzen auch die Haupt- und Neben-Locatoren auf DayLocator und HourLocator respective. Schließlich formatieren wir die Daten mit der DateFormatter-Funktion. Kopieren und einfügen Sie den folgenden Code:

```python
ax.set_xlim(dates[0], dates[-1])
ax.xaxis.set_major_locator(DayLocator())
ax.xaxis.set_minor_locator(HourLocator(range(0, 25, 6)))
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
```
