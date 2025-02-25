# Plotten

In diesem Schritt werden wir eine Figur erstellen und für jedes Bild, das wir erstellen möchten, Subplots hinzufügen.

```python
def demo():
    fig = plt.figure(figsize=(6, 6))

    # PLOT 1
    # einfaches Bild und Farbskala
    ax = fig.add_subplot(2, 2, 1)
    demo_simple_image(ax)

    # PLOT 2
    # Bild und Farbskala mit Zeichnungszeit-Positionierung -- ein schwieriger Weg
    demo_locatable_axes_hard(fig)

    # PLOT 3
    # Bild und Farbskala mit Zeichnungszeit-Positionierung -- ein einfacher Weg
    ax = fig.add_subplot(2, 2, 3)
    demo_locatable_axes_easy(ax)

    # PLOT 4
    # zwei Bilder nebeneinander mit fester Innenabstand.
    ax = fig.add_subplot(2, 2, 4)
    demo_images_side_by_side(ax)

    plt.show()
```
