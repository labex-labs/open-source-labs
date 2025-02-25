# Options de variante

La troisième propriété de police que nous allons explorer est l'option de variante. Cette propriété vous permet de définir la variante de police utilisée dans votre tracé.

```python
# Show variant options
variants = ['normal','small-caps']
fig.text(0.5, 0.9, 'variant', fontproperties=heading_font, **alignment)
for k, variant in enumerate(variants):
    font = FontProperties()
    font.set_family('serif')
    font.set_variant(variant)
    fig.text(0.5, yp[k], variant, fontproperties=font, **alignment)
```
