# Opciones de grosor

La cuarta propiedad de fuente que exploraremos es la opción de grosor. Esta propiedad le permite establecer el grosor de fuente utilizado en su gráfica.

```python
# Muestra las opciones de grosor
weights = ['light', 'normal','medium','semibold', 'bold', 'heavy', 'black']
fig.text(0.7, 0.9, 'weight', fontproperties=heading_font, **alignment)
for k, weight in enumerate(weights):
    font = FontProperties()
    font.set_weight(weight)
    fig.text(0.7, yp[k], weight, fontproperties=font, **alignment)
```
