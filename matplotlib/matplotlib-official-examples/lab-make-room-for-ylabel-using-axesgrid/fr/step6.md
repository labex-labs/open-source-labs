# Créer une figure avec deux axes réglables

Dans cette étape, nous créons une figure avec deux axes réglables. Nous utilisons la méthode `make_axes_locatable` pour créer un diviseur permettant d'ajuster les axes. Nous ajoutons un nouvel axe à droite du premier axe en utilisant la méthode `append_axes`.

```python
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1])
divider = make_axes_locatable(ax1)
ax2 = divider.append_axes("right", "100%", pad=0.3, sharey=ax1)
fig.add_axes(ax2)
```
