# Imprimir Estilos de Fonte

Nesta etapa, imprimiremos os estilos da fonte.

```python
for style in ('Italic',
              'Bold',
              'Scalable',
              'Fixed sizes',
              'Fixed width',
              'SFNT',
              'Horizontal',
              'Vertical',
              'Kerning',
              'Fast glyphs',
              'Multiple masters',
              'Glyph names',
              'External stream'):
    bitpos = getattr(ft, style.replace(' ', '_').upper()) - 1
    print(f"{style+':':17}", bool(font.style_flags & (1 << bitpos)))
```
