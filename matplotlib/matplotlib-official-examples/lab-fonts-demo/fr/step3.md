# Options de style

La deuxième propriété de police que nous allons explorer est l'option de style. Cette propriété vous permet de définir le style de police utilisé dans votre tracé.

```python
# Show style options
styles = ['normal', 'italic', 'oblique']
fig.text(0.3, 0.9,'style', fontproperties=heading_font, **alignment)
for k, style in enumerate(styles):
    font = FontProperties()
    font.set_family('sans-serif')
    font.set_style(style)
    fig.text(0.3, yp[k], style, fontproperties=font, **alignment)
```
