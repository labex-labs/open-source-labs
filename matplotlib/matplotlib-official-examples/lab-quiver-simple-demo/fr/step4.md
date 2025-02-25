# Création de la clé de flèches

Nous pouvons ajouter une clé de flèches au graphique pour montrer l'échelle des flèches. Nous utilisons la fonction `ax.quiverkey()` pour ajouter la clé. Nous passons l'objet `q`, la position `X` et `Y` de la clé, la longueur de la flèche, l'étiquette pour la clé et la position de l'étiquette.

```python
ax.quiverkey(q, X=0.3, Y=1.1, U=10,
             label='Quiver key, length = 10', labelpos='E')
```
