# Créer une fonction pour tracer l'image

Dans cette étape, nous définissons une fonction qui prend l'image, l'axe de tracé et la transformation en entrées. La fonction affiche l'image sur l'axe de tracé avec la transformation spécifiée. La fonction affiche également un rectangle jaune autour de l'image pour montrer l'étendue souhaitée de l'image.

```python
def do_plot(ax, Z, transform):
    im = ax.imshow(Z, interpolation='none',
                   origin='lower',
                   extent=[-2, 4, -3, 2], clip_on=True)

    trans_data = transform + ax.transData
    im.set_transform(trans_data)

    # affiche l'étendue souhaitée de l'image
    x1, x2, y1, y2 = im.get_extent()
    ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], "y--",
            transform=trans_data)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 4)
```
