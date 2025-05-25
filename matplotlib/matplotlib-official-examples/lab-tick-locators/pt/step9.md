# Definindo o MaxN Locator

O _MaxN locator_ (localizador MaxN) é um localizador que coloca um número máximo de _ticks_ (marcas) no eixo. Podemos definir o _MaxN locator_ usando `ticker.MaxNLocator()`.

```python
setup(axs[6], title="MaxNLocator(n=4)")
axs[6].xaxis.set_major_locator(ticker.MaxNLocator(4))
axs[6].xaxis.set_minor_locator(ticker.MaxNLocator(40))
```
