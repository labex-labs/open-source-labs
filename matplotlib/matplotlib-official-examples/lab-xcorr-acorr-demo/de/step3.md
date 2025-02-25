# Kreuzkorrelation plotten

Wir werden nun die Kreuzkorrelation zwischen den beiden Arrays mit der `xcorr`-Funktion in Matplotlib plotten.

```python
fig, ax = plt.subplots()
ax.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
ax.grid(True)
plt.show()
```

Die `xcorr`-Funktion nimmt die folgenden Parameter entgegen:

- `x`: das erste Datenarray
- `y`: das zweite Datenarray
- `usevlines`: boolesch, ob vertikale Linien von 0 bis zum Korrelationswert gezeichnet werden sollen
- `maxlags`: Ganzzahl, die maximale Anzahl der Lags, für die die Korrelation berechnet werden soll
- `normed`: boolesch, ob die Korrelationswerte normalisiert werden sollen
- `lw`: Ganzzahl, die Linienbreite für das Diagramm
