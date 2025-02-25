# Anpassen des Plots

Wir können den Plot anpassen, indem wir Beschriftungen, Titel hinzufügen und die Farbpalette ändern:

```python
fig, ax = plt.subplots()
cs = ax.contourf(X, Y, z, locator=ticker.LogLocator(), cmap=cm.coolwarm)

ax.set_title('Contourf Plot mit logarithmischer Farbskala')
ax.set_xlabel('X-Achse')
ax.set_ylabel('Y-Achse')

cbar = fig.colorbar(cs)

plt.show()
```
