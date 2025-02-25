# Lädt eine Glyphe

Jetzt werden wir eine Glyphe, den Buchstaben 'A', aus der Schriftart laden und seine Begrenzungskarte (Bounding Box) mit der Eigenschaft `glyph.bbox` ausgeben.

```python
code = coded['A']
glyph = font.load_char(code)
print(glyph.bbox)
```
