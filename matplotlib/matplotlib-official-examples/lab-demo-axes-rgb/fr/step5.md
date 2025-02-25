# Créez un tracé RGBAxes avec des canaux séparés

Dans cette étape, nous allons créer un tracé RGBAxes avec des canaux séparés en utilisant la fonction `make_rgb_axes()`. Nous utiliserons la méthode `imshow()` des objets `Axes` pour afficher les canaux R, G et B.

```python
def demo_rgb2():
    # Créez une figure et un objet Axes
    fig, ax = plt.subplots()

    # Créez les objets Axes R, G et B à l'aide de la fonction make_rgb_axes()
    ax_r, ax_g, ax_b = make_rgb_axes(ax, pad=0.02)

    # Obtenez les canaux R, G et B et créez le cube RGB
    r, g, b = get_rgb()
    im_r, im_g, im_b, im_rgb = make_cube(r, g, b)

    # Affichez l'image RGB et les canaux R, G et B
    ax.imshow(im_rgb)
    ax_r.imshow(im_r)
    ax_g.imshow(im_g)
    ax_b.imshow(im_b)

    # Réglez les paramètres d'échelle et les couleurs des bords pour tous les objets Axes
    for ax in fig.axes:
        ax.tick_params(direction='in', color='w')
        ax.spines[:].set_color("w")
```
