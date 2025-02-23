# Funktion zum Zeichnen des Bildes erstellen

In diesem Schritt definieren wir eine Funktion, die das Bild, die Zeichnungsachse und die Transformation als Eingaben nimmt. Die Funktion zeigt das Bild auf der Zeichnungsachse mit der angegebenen Transformation an. Die Funktion zeigt auch ein gelbes Rechteck um das Bild an, um den beabsichtigten Bereich des Bildes anzuzeigen.

```python
def do_plot(ax, Z, transform):
    im = ax.imshow(Z, interpolation='none',
                   origin='lower',
                   extent=[-2, 4, -3, 2], clip_on=True)

    trans_data = transform + ax.transData
    im.set_transform(trans_data)

    # display intended extent of the image
    x1, x2, y1, y2 = im.get_extent()
    ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], "y--",
            transform=trans_data)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 4)
```
