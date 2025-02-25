# Personnalisez les limites et l'apparence des axes

Nous allons personnaliser les limites et l'apparence de chaque axe à l'aide des méthodes `set_xlim`, `set_ylim` et `tick_params`.

```python
ax[0].set_xlim(0, 2)
ax[1].set_xlim(0, 1)
ax[0].set_ylim(0, 1)
ax[2].set_ylim(0, 2)
for ax1 in ax:
    ax1.tick_params(labelbottom=False, labelleft=False)
```
