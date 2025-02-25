# Ajouter du texte au tracé

Nous pouvons ajouter du texte au tracé à l'aide de la fonction `text`. Nous pouvons spécifier la position, la rotation, l'alignement horizontal et vertical, et l'alignement multiple du texte.

```python
ax0.text(2, 7, 'this is\nyet another test',
         rotation=45,
         horizontalalignment='center',
         verticalalignment='top',
         multialignment='center')
```
