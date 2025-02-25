# Cargar un glifo

Ahora cargaremos un glifo, la letra 'A', de la fuente y mostraremos su cuadro delimitador utilizando el atributo `glyph.bbox`.

```python
code = coded['A']
glyph = font.load_char(code)
print(glyph.bbox)
```
