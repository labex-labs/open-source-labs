# Erstellen eines Diagramms und Festlegen der x-Achse auf logarithmische Skala

Wir erstellen ein Figure- und Axes-Objekt mit der `subplots()`-Methode. Anschließend plotten wir die exponentielle Abnahme-Funktion mit der `semilogx()`-Methode und setzen die x-Achse auf eine logarithmische Skala mit der `set_xscale()`-Methode. Wir fügen auch ein Gitter zum Diagramm hinzu mit der `grid()`-Methode.

```python
fig, ax = plt.subplots()

ax.semilogx(t, np.exp(-t / 5.0))
ax.set_xscale('log')
ax.grid()
```
