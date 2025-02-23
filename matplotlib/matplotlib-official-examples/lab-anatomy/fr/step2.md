# Création de la figure et configuration des axes

Ensuite, nous allons créer une figure et configurer les axes. Nous utiliserons la méthode `add_axes()` pour créer un nouvel ensemble d'axes à l'intérieur de la figure. Nous définirons également les limites des axes x et y et ajouterons des lignes de grille.

```python
# Création de la figure et des axes
fig = plt.figure(figsize=(7.5, 7.5))
ax = fig.add_axes([0.2, 0.17, 0.68, 0.7], aspect=1)

# Définition des limites et des lignes de grille
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
```
