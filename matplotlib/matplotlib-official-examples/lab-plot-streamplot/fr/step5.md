# Largeur de ligne variable

Dans cette étape, nous allons créer un graphique de champ de flux avec une largeur de ligne variable. Le paramètre `linewidth` contrôle la largeur des lignes de courant. Ici, nous utilisons le tableau `speed` que nous avons calculé précédemment pour varier la largeur de ligne.

```python
lw = 5*speed / speed.max()
plt.streamplot(X, Y, U, V, density=0.6, color='k', linewidth=lw)
plt.title('Varying Line Width')
plt.show()
```
