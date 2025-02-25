# Couleur variable

Dans cette étape, nous allons créer un graphique de champ de flux avec une couleur variable. Le paramètre `color` prend un tableau 2D qui représente l'amplitude du champ vectoriel. Ici, nous utilisons la composante `U` du champ vectoriel comme couleur.

```python
strm = plt.streamplot(X, Y, U, V, color=U, linewidth=2, cmap='autumn')
plt.colorbar(strm.lines)
plt.title('Varying Color')
plt.show()
```
