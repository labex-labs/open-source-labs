# Opções de Variante

A terceira propriedade de fonte que exploraremos é a opção de variante (variant). Essa propriedade permite que você defina a variante de fonte usada em seu gráfico.

```python
# Show variant options
variants = ['normal', 'small-caps']
fig.text(0.5, 0.9, 'variant', fontproperties=heading_font, **alignment)
for k, variant in enumerate(variants):
    font = FontProperties()
    font.set_family('serif')
    font.set_variant(variant)
    fig.text(0.5, yp[k], variant, fontproperties=font, **alignment)
```
