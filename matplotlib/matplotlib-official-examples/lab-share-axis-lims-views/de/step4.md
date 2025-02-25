# Erstellen des zweiten Plots

Als nächstes werden wir das zweite Diagramm erstellen. Wir werden erneut `subplot` verwenden, aber diesmal werden wir das Attribut `sharex` auf das erste Diagramm (`ax1`) setzen. Dadurch wird sichergestellt, dass das zweite Diagramm die gleiche x-Achse wie das erste Diagramm teilt.

```python
ax2 = plt.subplot(212, sharex=ax1)
ax2.plot(t, np.sin(4*np.pi*t))
```
