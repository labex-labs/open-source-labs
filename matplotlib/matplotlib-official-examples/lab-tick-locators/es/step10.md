# Definiendo el LogLocator

El LogLocator es un localizador que coloca las marcas de graduación a intervalos regulares en una escala logarítmica. Podemos definir el LogLocator utilizando `ticker.LogLocator()`.

```python
setup(axs[7], title="LogLocator(base=10, numticks=15)")
axs[7].set_xlim(10**3, 10**10)
axs[7].set_xscale('log')
axs[7].xaxis.set_major_locator(ticker.LogLocator(base=10, numticks=15))
```
