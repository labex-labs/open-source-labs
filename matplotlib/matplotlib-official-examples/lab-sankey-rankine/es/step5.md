# Agregar etiquetas y formato

Agregaremos etiquetas a los parches en el diagrama de Sankey utilizando el atributo `text` de cada parche. También formatearemos el texto para que sea en negrita y aumentaremos el tamaño de la fuente.

```python
diagrams = sankey.finish()
for diagram in diagrams:
    diagram.text.set_fontweight('bold')
    diagram.text.set_fontsize('10')
    for text in diagram.texts:
        text.set_fontsize('10')
```
