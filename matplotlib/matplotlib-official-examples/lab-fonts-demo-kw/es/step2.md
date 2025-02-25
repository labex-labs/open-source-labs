# Mostrar familias de fuentes

A continuación, mostraremos las diferentes familias de fuentes disponibles en Matplotlib. Utilizaremos el método `fig.text()` para mostrar cada familia de fuentes, con el nombre de la familia como texto y la familia de fuentes correspondiente como argumento de palabra clave.

```python
alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
yp = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]

fig.text(0.1, 0.9, 'family', size='large', **alignment)
families = ['serif','sans-serif', 'cursive', 'fantasy','monospace']
for k, family in enumerate(families):
    fig.text(0.1, yp[k], family, family=family, **alignment)
```
