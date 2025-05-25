# Definindo o Multiple Locator

O _multiple locator_ (localizador múltiplo) é um localizador que coloca _ticks_ (marcas) em intervalos regulares. Podemos definir o _multiple locator_ usando `ticker.MultipleLocator()`.

```python
setup(axs[1], title="MultipleLocator(0.5, offset=0.2)")
axs[1].xaxis.set_major_locator(ticker.MultipleLocator(0.5, offset=0.2))
axs[1].xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
```
