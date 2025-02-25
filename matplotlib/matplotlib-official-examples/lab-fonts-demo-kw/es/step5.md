# Mostrar pesos de fuente

Ahora, mostraremos los diferentes pesos de fuente disponibles en Matplotlib. Utilizaremos el método `fig.text()` para mostrar cada peso de fuente, con el nombre del peso como texto y el peso de fuente correspondiente como argumento de palabra clave.

```python
fig.text(0.7, 0.9, 'weight', **alignment)
weights = ['light', 'normal','medium','semibold', 'bold', 'heavy', 'black']
for k, weight in enumerate(weights):
    fig.text(0.7, yp[k], weight, weight=weight, **alignment)
```
