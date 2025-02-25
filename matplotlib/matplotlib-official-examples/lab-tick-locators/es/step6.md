# Definiendo el LinearLocator

El LinearLocator es un localizador que coloca las marcas de graduación a intervalos regulares en una escala lineal. Podemos definir el LinearLocator utilizando `ticker.LinearLocator()`.

```python
setup(axs[3], title="LinearLocator(numticks=3)")
axs[3].xaxis.set_major_locator(ticker.LinearLocator(3))
axs[3].xaxis.set_minor_locator(ticker.LinearLocator(31))
```
