# Erstellen eines RGBAxes-Plots mit separaten Kanälen

In diesem Schritt erstellen wir einen RGBAxes-Plot mit separaten Kanälen mit der `make_rgb_axes()`-Funktion. Wir verwenden die `imshow()`-Methode der `Axes`-Objekte, um die R-, G- und B-Kanäle anzuzeigen.

```python
def demo_rgb2():
    # Erstellen Sie eine Figur und ein Axes-Objekt
    fig, ax = plt.subplots()

    # Erstellen Sie die R-, G- und B Axes-Objekte mit der make_rgb_axes()-Funktion
    ax_r, ax_g, ax_b = make_rgb_axes(ax, pad=0.02)

    # Holen Sie sich die R-, G- und B-Kanäle und erstellen Sie den RGB-Würfel
    r, g, b = get_rgb()
    im_r, im_g, im_b, im_rgb = make_cube(r, g, b)

    # Zeigen Sie das RGB-Bild und die R-, G- und B-Kanäle an
    ax.imshow(im_rgb)
    ax_r.imshow(im_r)
    ax_g.imshow(im_g)
    ax_b.imshow(im_b)

    # Legen Sie die Tick-Parameter und die Spine-Farben für alle Axes-Objekte fest
    for ax in fig.axes:
        ax.tick_params(direction='in', color='w')
        ax.spines[:].set_color("w")
```
