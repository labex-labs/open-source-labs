# Autokorrelation plotten

Wir werden nun die Autokorrelation des `x`-Arrays mit der `acorr`-Funktion in Matplotlib plotten.

```python
fig, ax = plt.subplots()
ax.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax.grid(True)
plt.show()
```

Die `acorr`-Funktion nimmt die folgenden Parameter entgegen:

- `x`: das Datenarray, für das die Autokorrelation berechnet werden soll
- `usevlines`: boolesch, ob vertikale Linien von 0 bis zum Korrelationswert gezeichnet werden sollen
- `normed`: boolesch, ob die Korrelationswerte normalisiert werden sollen
- `maxlags`: Ganzzahl, die maximale Anzahl der Lags, für die die Korrelation berechnet werden soll
- `lw`: Ganzzahl, die Linienbreite für das Diagramm
