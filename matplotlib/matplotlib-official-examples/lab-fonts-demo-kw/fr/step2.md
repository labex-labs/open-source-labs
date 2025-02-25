# Afficher les familles de polices

Ensuite, nous allons afficher les différentes familles de polices disponibles dans Matplotlib. Nous utiliserons la méthode `fig.text()` pour afficher chaque famille de police, avec le nom de la famille comme texte et la famille de police correspondante comme argument clé.

```python
alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
yp = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]

fig.text(0.1, 0.9, 'family', size='large', **alignment)
families = ['serif','sans-serif', 'cursive', 'fantasy','monospace']
for k, family in enumerate(families):
    fig.text(0.1, yp[k], family, family=family, **alignment)
```
