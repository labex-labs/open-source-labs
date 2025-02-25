# Definiendo el AutoLocator

El AutoLocator es un localizador que coloca automáticamente las marcas de graduación a intervalos regulares. Podemos definir el AutoLocator utilizando `ticker.AutoLocator()`.

```python
setup(axs[5], title="AutoLocator()")
axs[5].xaxis.set_major_locator(ticker.AutoLocator())
axs[5].xaxis.set_minor_locator(ticker.AutoMinorLocator())
```
