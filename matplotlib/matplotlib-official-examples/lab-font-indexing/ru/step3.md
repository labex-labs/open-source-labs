# Получение кодов символов и глифов

Мы получим коды символов и соответствующие глифы в шрифте и сохраним их в двух словарях `coded` и `glyphd`.

```python
codes = font.get_charmap().items()

coded = {}
glyphd = {}
for ccode, glyphind in codes:
    name = font.get_glyph_name(glyphind)
    coded[name] = ccode
    glyphd[name] = glyphind
```
