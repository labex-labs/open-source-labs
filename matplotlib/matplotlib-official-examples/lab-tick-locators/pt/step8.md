# Definindo o Auto Locator

O _auto locator_ (localizador automático) é um localizador que coloca automaticamente _ticks_ (marcas) em intervalos regulares. Podemos definir o _auto locator_ usando `ticker.AutoLocator()`.

```python
setup(axs[5], title="AutoLocator()")
axs[5].xaxis.set_major_locator(ticker.AutoLocator())
axs[5].xaxis.set_minor_locator(ticker.AutoMinorLocator())
```
