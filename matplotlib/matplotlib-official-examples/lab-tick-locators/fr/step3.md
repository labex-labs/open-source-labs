# Définition du positionneur nul

Le positionneur nul est un positionneur qui ne place pas de graduation sur l'axe. Nous pouvons définir le positionneur nul en utilisant `ticker.NullLocator()`.

```python
setup(axs[0], title="NullLocator()")
axs[0].xaxis.set_major_locator(ticker.NullLocator())
axs[0].xaxis.set_minor_locator(ticker.NullLocator())
```
