# Picking simple, lignes, rectangles et texte

Nous commencerons par activer le picking simple en configurant la propriété "picker" d'un artiste. Cela permettra à l'artiste de déclencher un événement de sélection si l'événement souris se produit au-dessus de l'artiste. Nous allons créer un tracé simple contenant une ligne, un rectangle et du texte, et activer le picking sur chacun de ces artistes.

```python
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.set_title('cliquez sur les points, les rectangles ou le texte', picker=True)
ax1.set_ylabel('ylabel', picker=True, bbox=dict(facecolor='red'))
line, = ax1.plot(rand(100), 'o', picker=True, pickradius=5)

# Sélectionnez le rectangle.
ax2.bar(range(10), rand(10), picker=True)
for label in ax2.get_xticklabels():  # Rendre les étiquettes d'échelle x sélectionnables.
    label.set_picker(True)
```
