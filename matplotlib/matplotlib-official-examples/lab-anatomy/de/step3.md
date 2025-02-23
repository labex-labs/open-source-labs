# Die Daten plotten

Jetzt werden wir unsere Daten auf den gerade erstellten Achsen plotten. Wir werden die Methode `plot()` verwenden, um die drei Sinuswellen mit unterschiedlichen Farben und Linienbreiten zu plotten.

```python
# Plot data
ax.plot(X, Y1, c='C0', lw=2.5, label="Blue signal", zorder=10)
ax.plot(X, Y2, c='C1', lw=2.5, label="Orange signal")
ax.plot(X[::3], Y3[::3], linewidth=0, markersize=9,
        marker='s', markerfacecolor='none', markeredgecolor='C4',
        markeredgewidth=2.5)
```
