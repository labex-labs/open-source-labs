# Zeichne die Daten und setze die Markierungen auf der x-Achse

Schließlich kannst du die Daten mit der `plot`-Funktion zeichnen und die Markierungen auf der x-Achse mit den zuvor gesetzten Funktionen für den Markierungsgeber und den Formatierer festlegen.

```python
fig, ax = plt.subplots()
plt.plot(dates, s, 'o')
ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30, labelsize=10)
plt.show()
```
