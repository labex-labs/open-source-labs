# Options de taille

La cinquième propriété de police que nous allons explorer est l'option de taille. Cette propriété vous permet de définir la taille de police utilisée dans votre tracé.

```python
# Show size options
sizes = [
    'xx-small', 'x-small','small','medium', 'large', 'x-large', 'xx-large']
fig.text(0.9, 0.9,'size', fontproperties=heading_font, **alignment)
for k, size in enumerate(sizes):
    font = FontProperties()
    font.set_size(size)
    fig.text(0.9, yp[k], size, fontproperties=font, **alignment)
```
