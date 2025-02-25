# Obtener códigos de caracteres y glifos

Obtendremos los códigos de caracteres y los glifos correspondientes en la fuente y los almacenaremos en dos diccionarios, `coded` y `glyphd`.

```python
codes = font.get_charmap().items()

coded = {}
glyphd = {}
for ccode, glyphind in codes:
    name = font.get_glyph_name(glyphind)
    coded[name] = ccode
    glyphd[name] = glyphind
```
