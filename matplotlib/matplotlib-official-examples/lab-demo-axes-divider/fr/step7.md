# Traçage

Dans cette étape, nous allons créer une figure et ajouter des sous-graphiques pour chaque image que nous souhaitons créer.

```python
def demo():
    fig = plt.figure(figsize=(6, 6))

    # TRACÉ 1
    # image simple et barre de couleur
    ax = fig.add_subplot(2, 2, 1)
    demo_simple_image(ax)

    # TRACÉ 2
    # image et barre de couleur avec positionnement au moment du tracé -- une manière difficile
    demo_locatable_axes_hard(fig)

    # TRACÉ 3
    # image et barre de couleur avec positionnement au moment du tracé -- une manière facile
    ax = fig.add_subplot(2, 2, 3)
    demo_locatable_axes_easy(ax)

    # TRACÉ 4
    # deux images côte à côte avec une marge fixe.
    ax = fig.add_subplot(2, 2, 4)
    demo_images_side_by_side(ax)

    plt.show()
```
