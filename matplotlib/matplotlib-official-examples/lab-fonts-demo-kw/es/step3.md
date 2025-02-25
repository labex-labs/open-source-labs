# Mostrar estilos de fuente

Ahora, mostraremos los diferentes estilos de fuente disponibles en Matplotlib. Utilizaremos el método `fig.text()` para mostrar cada estilo de fuente, con el nombre del estilo como texto y el estilo de fuente correspondiente como argumento de palabra clave.

```python
fig.text(0.3, 0.9,'style', **alignment)
styles = ['normal', 'italic', 'oblique']
for k, style in enumerate(styles):
    fig.text(0.3, yp[k], style, family='sans-serif', style=style, **alignment)
```
