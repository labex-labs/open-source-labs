# Définition du positionneur multiple

Le positionneur multiple est un positionneur qui place les graduations à des intervalles réguliers. Nous pouvons définir le positionneur multiple en utilisant `ticker.MultipleLocator()`.

```python
setup(axs[1], title="MultipleLocator(0.5, offset=0.2)")
axs[1].xaxis.set_major_locator(ticker.MultipleLocator(0.5, offset=0.2))
axs[1].xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
```
