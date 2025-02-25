# Mostrar tamaños de fuente

Finalmente, mostraremos los diferentes tamaños de fuente disponibles en Matplotlib. Utilizaremos el método `fig.text()` para mostrar cada tamaño de fuente, con el nombre del tamaño como texto y el tamaño de fuente correspondiente como argumento de palabra clave.

```python
fig.text(0.9, 0.9,'size', **alignment)
sizes = [
    'xx-small', 'x-small','small','medium', 'large', 'x-large', 'xx-large']
for k, size in enumerate(sizes):
    fig.text(0.9, yp[k], size, size=size, **alignment)
```
