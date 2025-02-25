# Définition du positionneur linéaire

Le positionneur linéaire est un positionneur qui place les graduations à des intervalles réguliers sur une échelle linéaire. Nous pouvons définir le positionneur linéaire en utilisant `ticker.LinearLocator()`.

```python
setup(axs[3], title="LinearLocator(numticks=3)")
axs[3].xaxis.set_major_locator(ticker.LinearLocator(3))
axs[3].xaxis.set_minor_locator(ticker.LinearLocator(31))
```
