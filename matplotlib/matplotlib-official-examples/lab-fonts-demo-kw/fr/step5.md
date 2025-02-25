# Afficher les graisses de police

Maintenant, nous allons afficher les différentes graisses de police disponibles dans Matplotlib. Nous utiliserons la méthode `fig.text()` pour afficher chaque graisse de police, avec le nom de la graisse comme texte et la graisse de police correspondante comme argument clé.

```python
fig.text(0.7, 0.9, 'weight', **alignment)
weights = ['light', 'normal','medium','semibold', 'bold', 'heavy', 'black']
for k, weight in enumerate(weights):
    fig.text(0.7, yp[k], weight, weight=weight, **alignment)
```
