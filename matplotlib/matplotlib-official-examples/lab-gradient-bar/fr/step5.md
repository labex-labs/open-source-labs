# Créez le tracé

Maintenant, nous pouvons créer le tracé. Nous allons tout d'abord créer une figure et un objet d'axes. Nous définirons ensuite les limites x et y des axes. Nous créerons un fond à gradient à l'aide de la fonction `gradient_image()`. Enfin, nous créerons un ensemble de données aléatoires et utiliserons la fonction `gradient_bar()` pour créer le graphique en barres.

```python
fig, ax = plt.subplots()
ax.set(xlim=(0, 10), ylim=(0, 1))

# image de fond
gradient_image(ax, direction=1, extent=(0, 1, 0, 1), transform=ax.transAxes,
               cmap=plt.cm.RdYlGn, cmap_range=(0.2, 0.8), alpha=0.5)

N = 10
x = np.arange(N) + 0.15
y = np.random.rand(N)
gradient_bar(ax, x, y, width=0.7)
plt.show()
```
