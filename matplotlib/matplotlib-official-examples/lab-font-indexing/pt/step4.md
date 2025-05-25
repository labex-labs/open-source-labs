# Carregar um Glifo

Agora, carregaremos um glifo, a letra 'A', da fonte e imprimiremos sua caixa delimitadora (bounding box) usando o atributo `glyph.bbox`.

```python
code = coded['A']
glyph = font.load_char(code)
print(glyph.bbox)
```
