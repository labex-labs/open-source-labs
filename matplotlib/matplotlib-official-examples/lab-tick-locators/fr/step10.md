# Définition du positionneur logarithmique

Le positionneur logarithmique est un positionneur qui place les graduations à des intervalles réguliers sur une échelle logarithmique. Nous pouvons définir le positionneur logarithmique en utilisant `ticker.LogLocator()`.

```python
setup(axs[7], title="LogLocator(base=10, numticks=15)")
axs[7].set_xlim(10**3, 10**10)
axs[7].set_xscale('log')
axs[7].xaxis.set_major_locator(ticker.LogLocator(base=10, numticks=15))
```
