# Opciones de familia

La primera propiedad de fuente que exploraremos es la opción de familia. Esta propiedad le permite establecer la familia de fuentes utilizada en su gráfica.

```python
# Muestra las opciones de familia
fig.text(0.1, 0.9, 'family', fontproperties=heading_font, **alignment)
families = ['serif','sans-serif', 'cursive', 'fantasy','monospace']
for k, family in enumerate(families):
    font = FontProperties()
    font.set_family(family)
    fig.text(0.1, yp[k], family, fontproperties=font, **alignment)
```
