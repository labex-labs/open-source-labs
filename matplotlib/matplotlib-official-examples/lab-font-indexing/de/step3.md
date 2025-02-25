# Holt Zeichencodes und Glyphen

Wir werden die Zeichencodes und die zugehörigen Glyphen in der Schriftart abrufen und sie in zwei Wörterbüchern, `coded` und `glyphd`, speichern.

```python
codes = font.get_charmap().items()

coded = {}
glyphd = {}
for ccode, glyphind in codes:
    name = font.get_glyph_name(glyphind)
    coded[name] = ccode
    glyphd[name] = glyphind
```
