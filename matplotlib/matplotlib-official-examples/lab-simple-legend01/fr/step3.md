# Ajoutez une légende au tracé

Nous allons maintenant ajouter une légende au tracé. Il existe deux manières d'ajouter une légende dans Matplotlib. Nous utiliserons les deux méthodes dans cet exemple.

```python
# Méthode 1 : Placer une légende au-dessus du sous-graphique
ax.legend(bbox_to_anchor=(0., 1.02, 1.,.102), loc='lower left',
           ncols=2, mode="expand", borderaxespad=0.)

# Méthode 2 : Placer une légende à droite du sous-graphique
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
```
