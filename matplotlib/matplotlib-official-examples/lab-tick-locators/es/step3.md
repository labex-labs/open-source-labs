# Definiendo el NullLocator

El NullLocator es un localizador que no coloca ninguna marca de graduación en el eje. Podemos definir el NullLocator utilizando `ticker.NullLocator()`.

```python
setup(axs[0], title="NullLocator()")
axs[0].xaxis.set_major_locator(ticker.NullLocator())
axs[0].xaxis.set_minor_locator(ticker.NullLocator())
```
