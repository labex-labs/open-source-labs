# Obter Códigos de Caracteres e Glifos

Obteremos os códigos de caracteres e os glifos correspondentes na fonte e os armazenaremos em dois dicionários, `coded` e `glyphd`.

```python
codes = font.get_charmap().items()

coded = {}
glyphd = {}
for ccode, glyphind in codes:
    name = font.get_glyph_name(glyphind)
    coded[name] = ccode
    glyphd[name] = glyphind
```
