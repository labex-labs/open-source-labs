# Gras et italique

La dernière propriété de police que nous allons explorer est une combinaison des options de style et de poids. Cette propriété vous permet de définir le style et le poids de police utilisés dans votre tracé.

```python
# Show bold italic
font = FontProperties(style='italic', weight='bold', size='x-small')
fig.text(0.3, 0.1, 'bold italic', fontproperties=font, **alignment)
font = FontProperties(style='italic', weight='bold', size='medium')
fig.text(0.3, 0.2, 'bold italic', fontproperties=font, **alignment)
font = FontProperties(style='italic', weight='bold', size='x-large')
fig.text(0.3, 0.3, 'bold italic', fontproperties=font, **alignment)
```
