# Definindo o Fixed Locator

O _fixed locator_ (localizador fixo) é um localizador que coloca _ticks_ (marcas) em localizações fixas. Podemos definir o _fixed locator_ usando `ticker.FixedLocator()`.

```python
setup(axs[2], title="FixedLocator([0, 1, 5])")
axs[2].xaxis.set_major_locator(ticker.FixedLocator([0, 1, 5]))
axs[2].xaxis.set_minor_locator(ticker.FixedLocator(np.linspace(0.2, 0.8, 4)))
```
