# Plot mit logarithmischer Skala und Fehlerbalken

Schließlich werden wir unsere Daten mit einer logarithmischen Skala und Fehlerbalken plotten. Die Funktion `ax.set_yscale()` wird verwendet, um die y-Achse auf eine logarithmische Skala einzustellen.

```python
# plot log scale with error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=error, fmt='o')
ax.set_title('Log Scale with Error Bars')
ax.set_yscale('log')
plt.show()
```
