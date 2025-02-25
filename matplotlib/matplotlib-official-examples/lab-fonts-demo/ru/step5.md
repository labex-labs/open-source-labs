# Варианты толщины

Четвёртым параметром шрифта, который мы исследуем, является вариант толщины. Этот параметр позволяет вам выбирать толщину шрифта, используемую в вашем графике.

```python
# Show weight options
weights = ['light', 'normal','medium','semibold', 'bold', 'heavy', 'black']
fig.text(0.7, 0.9, 'weight', fontproperties=heading_font, **alignment)
for k, weight in enumerate(weights):
    font = FontProperties()
    font.set_weight(weight)
    fig.text(0.7, yp[k], weight, fontproperties=font, **alignment)
```
