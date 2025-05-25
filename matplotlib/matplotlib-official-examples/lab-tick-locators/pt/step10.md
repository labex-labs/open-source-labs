# Definindo o Log Locator

O _log locator_ (localizador logarítmico) é um localizador que coloca _ticks_ (marcas) em intervalos regulares em uma escala logarítmica. Podemos definir o _log locator_ usando `ticker.LogLocator()`.

```python
setup(axs[7], title="LogLocator(base=10, numticks=15)")
axs[7].set_xlim(10**3, 10**10)
axs[7].set_xscale('log')
axs[7].xaxis.set_major_locator(ticker.LogLocator(base=10, numticks=15))
```
