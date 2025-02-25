# Anpassen der Achsengrenzen und des Aussehens

Wir werden die Grenzen und das Aussehen jeder Achse mit den Methoden `set_xlim`, `set_ylim` und `tick_params` anpassen.

```python
ax[0].set_xlim(0, 2)
ax[1].set_xlim(0, 1)
ax[0].set_ylim(0, 1)
ax[2].set_ylim(0, 2)
for ax1 in ax:
    ax1.tick_params(labelbottom=False, labelleft=False)
```
