# Definiendo el FixedLocator

El FixedLocator es un localizador que coloca las marcas de graduación en ubicaciones fijas. Podemos definir el FixedLocator utilizando `ticker.FixedLocator()`.

```python
setup(axs[2], title="FixedLocator([0, 1, 5])")
axs[2].xaxis.set_major_locator(ticker.FixedLocator([0, 1, 5]))
axs[2].xaxis.set_minor_locator(ticker.FixedLocator(np.linspace(0.2, 0.8, 4)))
```
