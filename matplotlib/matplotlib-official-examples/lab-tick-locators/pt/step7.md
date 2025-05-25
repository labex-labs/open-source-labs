# Definindo o Index Locator

O _index locator_ (localizador de índice) é um localizador que coloca _ticks_ (marcas) em intervalos regulares em uma escala de índice. Podemos definir o _index locator_ usando `ticker.IndexLocator()`.

```python
setup(axs[4], title="IndexLocator(base=0.5, offset=0.25)")
axs[4].plot([0]*5, color='white')
axs[4].xaxis.set_major_locator(ticker.IndexLocator(base=0.5, offset=0.25))
```
