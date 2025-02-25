# Opciones de variante

La tercera propiedad de fuente que exploraremos es la opción de variante. Esta propiedad le permite establecer la variante de fuente utilizada en su gráfica.

```python
# Muestra las opciones de variante
variants = ['normal','small-caps']
fig.text(0.5, 0.9, 'variant', fontproperties=heading_font, **alignment)
for k, variant in enumerate(variants):
    font = FontProperties()
    font.set_family('serif')
    font.set_variant(variant)
    fig.text(0.5, yp[k], variant, fontproperties=font, **alignment)
```
