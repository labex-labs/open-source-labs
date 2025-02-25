# Créer un graphique en 3D

Nous créons un graphique en 3D à l'aide de `matplotlib`. Nous ajoutons une ligne vide pour chaque mouvement aléatoire au graphique. Nous définissons les limites des axes x, y et z entre 0 et 1.

```python
# Attacher l'axe 3D à la figure
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Créer des lignes initialement sans données
lines = [ax.plot([], [], [])[0] for _ in walks]

# Définir les propriétés des axes
ax.set(xlim3d=(0, 1), xlabel='X')
ax.set(ylim3d=(0, 1), ylabel='Y')
ax.set(zlim3d=(0, 1), zlabel='Z')
```
