# Get Character Codes and Glyphs

We will get the character codes and corresponding glyphs in the font and store them in two dictionaries, `coded` and `glyphd`.

```python
codes = font.get_charmap().items()

coded = {}
glyphd = {}
for ccode, glyphind in codes:
    name = font.get_glyph_name(glyphind)
    coded[name] = ccode
    glyphd[name] = glyphind
```
