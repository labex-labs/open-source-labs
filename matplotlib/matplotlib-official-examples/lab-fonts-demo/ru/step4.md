# Варианты варианта

Третьим параметром шрифта, который мы исследуем, является вариант варианта. Этот параметр позволяет вам выбирать вариант шрифта, используемый в вашем графике.

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
