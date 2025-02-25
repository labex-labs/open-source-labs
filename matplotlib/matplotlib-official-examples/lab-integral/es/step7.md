# Agregar etiquetas de eje y etiquetas de marcas de graduación

Agrega las etiquetas de los ejes x e y utilizando `figtext`. Oculta las espinas superior e inferior utilizando `spines`. Establece la colocación personalizada de las marcas de graduación y las etiquetas utilizando `set_xticks` y `set_yticks`.

```python
fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')

ax.spines[['top', 'right']].set_visible(False)
ax.set_xticks([a, b], labels=['$a$', '$b$'])
ax.set_yticks([])
```
