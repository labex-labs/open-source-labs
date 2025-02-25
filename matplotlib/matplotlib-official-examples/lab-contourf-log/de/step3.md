# Erstellen des Plots

Wir werden die `contourf`-Funktion verwenden, um einen gefüllten Konturplot mit einer logarithmischen Farbskala zu erstellen:

```python
fig, ax = plt.subplots()
cs = ax.contourf(X, Y, z, locator=ticker.LogLocator(), cmap=cm.PuBu_r)

cbar = fig.colorbar(cs)

plt.show()
```
