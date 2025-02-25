# Definiendo el IndexLocator

El IndexLocator es un localizador que coloca las marcas de graduación a intervalos regulares en una escala de índice. Podemos definir el IndexLocator utilizando `ticker.IndexLocator()`.

```python
setup(axs[4], title="IndexLocator(base=0.5, offset=0.25)")
axs[4].plot([0]*5, color='white')
axs[4].xaxis.set_major_locator(ticker.IndexLocator(base=0.5, offset=0.25))
```
