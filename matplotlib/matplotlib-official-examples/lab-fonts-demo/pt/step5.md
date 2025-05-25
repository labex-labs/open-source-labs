# Opções de Peso

A quarta propriedade de fonte que exploraremos é a opção de peso (weight). Essa propriedade permite que você defina o peso da fonte usado em seu gráfico.

```python
# Show weight options
weights = ['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']
fig.text(0.7, 0.9, 'weight', fontproperties=heading_font, **alignment)
for k, weight in enumerate(weights):
    font = FontProperties()
    font.set_weight(weight)
    fig.text(0.7, yp[k], weight, fontproperties=font, **alignment)
```
