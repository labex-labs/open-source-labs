# Opciones de estilo

La segunda propiedad de fuente que exploraremos es la opción de estilo. Esta propiedad le permite establecer el estilo de fuente utilizado en su gráfica.

```python
# Muestra las opciones de estilo
styles = ['normal', 'italic', 'oblique']
fig.text(0.3, 0.9,'style', fontproperties=heading_font, **alignment)
for k, style in enumerate(styles):
    font = FontProperties()
    font.set_family('sans-serif')
    font.set_style(style)
    fig.text(0.3, yp[k], style, fontproperties=font, **alignment)
```
