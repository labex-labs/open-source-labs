# Ajuster les limites et ajouter des étiquettes

Enfin, nous allons ajuster les limites du tracé et ajouter des étiquettes d'axe à l'aide des fonctions `set_zlim()`, `set_xlabel()`, `set_ylabel()` et `set_zlabel()` de Matplotlib. Nous utiliserons également le mode mathématique LaTeX pour écrire les étiquettes d'axe.

```python
ax.set_zlim(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{réel}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')
```
