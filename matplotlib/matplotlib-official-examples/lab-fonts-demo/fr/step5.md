# Options de poids

La quatrième propriété de police que nous allons explorer est l'option de poids. Cette propriété vous permet de définir le poids de police utilisé dans votre tracé.

```python
# Show weight options
weights = ['light', 'normal','medium','semibold', 'bold', 'heavy', 'black']
fig.text(0.7, 0.9, 'weight', fontproperties=heading_font, **alignment)
for k, weight in enumerate(weights):
    font = FontProperties()
    font.set_weight(weight)
    fig.text(0.7, yp[k], weight, fontproperties=font, **alignment)
```
