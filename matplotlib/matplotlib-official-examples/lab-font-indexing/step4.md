# Load a Glyph

Now we will load a glyph, the letter 'A', from the font and print its bounding box using the `glyph.bbox` attribute.

```python
code = coded['A']
glyph = font.load_char(code)
print(glyph.bbox)
```
