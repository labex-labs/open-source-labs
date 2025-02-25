# Obtenir les codes de caractères et les glyphes

Nous allons obtenir les codes de caractères et les glyphes correspondants dans la police et les stocker dans deux dictionnaires, `coded` et `glyphd`.

```python
codes = font.get_charmap().items()

coded = {}
glyphd = {}
for ccode, glyphind in codes:
    name = font.get_glyph_name(glyphind)
    coded[name] = ccode
    glyphd[name] = glyphind
```
