# Variantenoptionen

Die dritte Schriftart-Eigenschaft, die wir untersuchen werden, ist die Varianten-Option. Mit dieser Eigenschaft kannst du die Schriftvariante festlegen, die in deinem Diagramm verwendet wird.

```python
# Zeige Variantenoptionen
variants = ['normal','small-caps']
fig.text(0.5, 0.9, 'variant', fontproperties=heading_font, **alignment)
for k, variant in enumerate(variants):
    font = FontProperties()
    font.set_family('serif')
    font.set_variant(variant)
    fig.text(0.5, yp[k], variant, fontproperties=font, **alignment)
```
