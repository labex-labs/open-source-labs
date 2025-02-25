# Créer une figure avec deux axes

Dans cette étape, nous créons une figure avec deux axes. Nous utilisons la méthode `add_axes` pour ajouter deux axes à la figure. Nous définissons également l'étiquette de graduation de l'axe des y pour le premier axe et le titre pour le second axe.

```python
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 0.5])
ax2 = fig.add_axes([0, 0.5, 1, 0.5])

ax1.set_yticks([0.5], labels=["very long label"])
ax1.set_ylabel("Y label")

ax2.set_title("Title")
```
