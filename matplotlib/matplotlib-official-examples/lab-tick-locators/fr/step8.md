# Définition du positionneur automatique

Le positionneur automatique est un positionneur qui place automatiquement les graduations à des intervalles réguliers. Nous pouvons définir le positionneur automatique en utilisant `ticker.AutoLocator()`.

```python
setup(axs[5], title="AutoLocator()")
axs[5].xaxis.set_major_locator(ticker.AutoLocator())
axs[5].xaxis.set_minor_locator(ticker.AutoMinorLocator())
```
