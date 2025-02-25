# Options de famille

La première propriété de police que nous allons explorer est l'option de famille. Cette propriété vous permet de définir la famille de polices utilisée dans votre tracé.

```python
# Show family options
fig.text(0.1, 0.9, 'family', fontproperties=heading_font, **alignment)
families = ['serif','sans-serif', 'cursive', 'fantasy','monospace']
for k, family in enumerate(families):
    font = FontProperties()
    font.set_family(family)
    fig.text(0.1, yp[k], family, fontproperties=font, **alignment)
```
