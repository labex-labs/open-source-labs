# Préparer la représentation graphique

Nous allons maintenant préparer la représentation graphique de notre simulation. Nous allons créer une figure avec des limites x et y égales à la longueur maximale du pendule, définir le rapport d'aspect pour être égal et ajouter une grille.

```python
fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(autoscale_on=False, xlim=(-L, L), ylim=(-L, 1.))
ax.set_aspect('equal')
ax.grid()
```
