# Mostrar variantes de fuente

A continuación, mostraremos las diferentes variantes de fuente disponibles en Matplotlib. Utilizaremos el método `fig.text()` para mostrar cada variante de fuente, con el nombre de la variante como texto y la variante de fuente correspondiente como argumento de palabra clave.

```python
fig.text(0.5, 0.9, 'variant', **alignment)
variants = ['normal','small-caps']
for k, variant in enumerate(variants):
    fig.text(0.5, yp[k], variant, family='serif', variant=variant, **alignment)
```
