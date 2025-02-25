# Charger un glyphe

Maintenant, nous allons charger un glyphe, la lettre 'A', à partir de la police et afficher sa boîte englobante en utilisant l'attribut `glyph.bbox`.

```python
code = coded['A']
glyph = font.load_char(code)
print(glyph.bbox)
```
