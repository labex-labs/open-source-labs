# Création d'un tracé de courbes de niveau remplies avec des niveaux explicites

Maintenant, nous allons créer un tracé de courbes de niveau remplies avec des niveaux explicites. Nous utiliserons la méthode `contourf` avec le paramètre `levels` défini sur une liste de valeurs pour spécifier les niveaux de contour. Nous définirons également la carte de couleurs sur une liste de couleurs et le paramètre `extend` sur `'both'` pour afficher les valeurs en dehors de la plage des niveaux.

```python
# Création d'un tracé de courbes de niveau remplies avec des niveaux explicites
fig, ax = plt.subplots()
levels = [-1.5, -1, -0.5, 0, 0.5, 1]
CS = ax.contourf(X, Y, Z, levels, colors=('r', 'g', 'b'),
                 origin=origin, extend='both')
CS2 = ax.contour(X, Y, Z, levels, colors=('k',),
                 linewidths=(3,), origin=origin)

# Ajout du titre, des étiquettes d'axe et de la barre de couleur
ax.set_title('Tracé de courbes de niveau remplies avec des niveaux explicites')
ax.set_xlabel('Étiquette de X')
ax.set_ylabel('Étiquette de Y')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Étiquette de Z')

# Affichage du tracé
plt.show()
```
