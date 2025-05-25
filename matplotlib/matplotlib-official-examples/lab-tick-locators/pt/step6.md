# Definindo o Linear Locator

O _linear locator_ (localizador linear) é um localizador que coloca _ticks_ (marcas) em intervalos regulares em uma escala linear. Podemos definir o _linear locator_ usando `ticker.LinearLocator()`.

```python
setup(axs[3], title="LinearLocator(numticks=3)")
axs[3].xaxis.set_major_locator(ticker.LinearLocator(3))
axs[3].xaxis.set_minor_locator(ticker.LinearLocator(31))
```
