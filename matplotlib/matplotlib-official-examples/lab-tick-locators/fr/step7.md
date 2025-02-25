# Définition du positionneur d'index

Le positionneur d'index est un positionneur qui place les graduations à des intervalles réguliers sur une échelle d'index. Nous pouvons définir le positionneur d'index en utilisant `ticker.IndexLocator()`.

```python
setup(axs[4], title="IndexLocator(base=0.5, offset=0.25)")
axs[4].plot([0]*5, color='white')
axs[4].xaxis.set_major_locator(ticker.IndexLocator(base=0.5, offset=0.25))
```
