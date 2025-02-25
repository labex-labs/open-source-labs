# Afficher en gras et en italique

En prime, nous pouvons également afficher du texte avec les styles gras et italique à la fois. Nous utiliserons la méthode `fig.text()` pour afficher le texte avec le style, la graisse et la taille appropriés.

```python
fig.text(0.3, 0.1, 'bold italic',
         style='italic', weight='bold', size='x-small', **alignment)
fig.text(0.3, 0.2, 'bold italic',
         style='italic', weight='bold', size='medium', **alignment)
fig.text(0.3, 0.3, 'bold italic',
         style='italic', weight='bold', size='x-large', **alignment)
```
