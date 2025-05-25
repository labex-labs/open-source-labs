# Opções de Família

A primeira propriedade de fonte que exploraremos é a opção de família (family). Essa propriedade permite que você defina a família de fontes usada em seu gráfico.

```python
# Show family options
fig.text(0.1, 0.9, 'family', fontproperties=heading_font, **alignment)
families = ['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']
for k, family in enumerate(families):
    font = FontProperties()
    font.set_family(family)
    fig.text(0.1, yp[k], family, fontproperties=font, **alignment)
```
