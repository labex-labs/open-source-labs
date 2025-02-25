# Definiendo el MaxNLocator

El MaxNLocator es un localizador que coloca un número máximo de marcas de graduación en el eje. Podemos definir el MaxNLocator utilizando `ticker.MaxNLocator()`.

```python
setup(axs[6], title="MaxNLocator(n=4)")
axs[6].xaxis.set_major_locator(ticker.MaxNLocator(4))
axs[6].xaxis.set_minor_locator(ticker.MaxNLocator(40))
```
