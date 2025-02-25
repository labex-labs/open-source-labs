# Definiendo el MultipleLocator

El MultipleLocator es un localizador que coloca las marcas de graduación a intervalos regulares. Podemos definir el MultipleLocator utilizando `ticker.MultipleLocator()`.

```python
setup(axs[1], title="MultipleLocator(0.5, offset=0.2)")
axs[1].xaxis.set_major_locator(ticker.MultipleLocator(0.5, offset=0.2))
axs[1].xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
```
