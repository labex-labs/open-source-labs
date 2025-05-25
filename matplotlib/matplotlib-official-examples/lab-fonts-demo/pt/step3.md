# Opções de Estilo

A segunda propriedade de fonte que exploraremos é a opção de estilo (style). Essa propriedade permite que você defina o estilo de fonte usado em seu gráfico.

```python
# Show style options
styles = ['normal', 'italic', 'oblique']
fig.text(0.3, 0.9, 'style', fontproperties=heading_font, **alignment)
for k, style in enumerate(styles):
    font = FontProperties()
    font.set_family('sans-serif')
    font.set_style(style)
    fig.text(0.3, yp[k], style, fontproperties=font, **alignment)
```
