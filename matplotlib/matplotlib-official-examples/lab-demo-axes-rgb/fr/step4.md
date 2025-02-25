# Créez un tracé RGBAxes

Dans cette étape, nous allons créer un tracé RGBAxes en utilisant la classe `RGBAxes`. Nous utiliserons la méthode `imshow_rgb()` de l'objet `RGBAxes` pour afficher l'image RGB.

```python
def demo_rgb1():
    # Créez une figure et un objet RGBAxes
    fig = plt.figure()
    ax = RGBAxes(fig, [0.1, 0.1, 0.8, 0.8], pad=0.0)

    # Obtenez les canaux R, G et B
    r, g, b = get_rgb()

    # Affichez l'image RGB à l'aide de la méthode imshow_rgb()
    ax.imshow_rgb(r, g, b)
```
