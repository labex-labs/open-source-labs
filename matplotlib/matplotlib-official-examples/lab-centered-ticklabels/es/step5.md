# Alinear las etiquetas de las marcas de graduación menores

Finalmente, necesitamos alinear las etiquetas de las marcas de graduación menores al centro entre las marcas de graduación principales. Esto se puede hacer utilizando la función `get_xticklabels()` y estableciendo el parámetro `minor` en `True` para obtener las etiquetas de las marcas de graduación menores. Luego podemos recorrer las etiquetas y establecer la alineación horizontal en `'center'`.

```python
# Alinear la etiqueta de la marca de graduación menor
for label in ax.get_xticklabels(minor=True):
    label.set_horizontalalignment('center')
imid = len(r) // 2
ax.set_xlabel(str(r.date[imid].item().year))
```
