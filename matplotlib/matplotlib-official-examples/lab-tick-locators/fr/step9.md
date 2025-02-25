# Définition du positionneur MaxN

Le positionneur MaxN est un positionneur qui place un nombre maximum de graduations sur l'axe. Nous pouvons définir le positionneur MaxN en utilisant `ticker.MaxNLocator()`.

```python
setup(axs[6], title="MaxNLocator(n=4)")
axs[6].xaxis.set_major_locator(ticker.MaxNLocator(4))
axs[6].xaxis.set_minor_locator(ticker.MaxNLocator(40))
```
