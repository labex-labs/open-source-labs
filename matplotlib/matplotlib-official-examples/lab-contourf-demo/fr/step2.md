# Création d'un tracé de courbes de niveau remplies avec des niveaux automatiques

Ensuite, nous allons créer un tracé de courbes de niveau remplies avec des niveaux automatiques. Nous utiliserons la méthode `contourf` avec le paramètre `cmap` défini sur `plt.cm.bone` pour spécifier la carte de couleurs. Nous ajouterons également des lignes de niveau avec la méthode `contour` et passerons un sous-ensemble des niveaux de contour utilisés pour les courbes de niveau remplies.

```python
# Création d'un tracé de courbes de niveau remplies avec des niveaux automatiques
fig, ax = plt.subplots()
CS = ax.contourf(X, Y, Z, 10, cmap=plt.cm.bone, origin=origin)
CS2 = ax.contour(CS, levels=CS.levels[::2], colors='r', origin=origin)

# Ajout du titre, des étiquettes d'axe et de la barre de couleur
ax.set_title('Tracé de courbes de niveau remplies avec des niveaux automatiques')
ax.set_xlabel('Étiquette de X')
ax.set_ylabel('Étiquette de Y')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Étiquette de Z')
cbar.add_lines(CS2)

# Affichage du tracé
plt.show()
```
