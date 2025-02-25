# Erstellen eines RGBAxes-Plots

In diesem Schritt erstellen wir einen RGBAxes-Plot mit der `RGBAxes`-Klasse. Wir verwenden die `imshow_rgb()`-Methode des `RGBAxes`-Objekts, um das RGB-Bild anzuzeigen.

```python
def demo_rgb1():
    # Erstellen Sie eine Figur und ein RGBAxes-Objekt
    fig = plt.figure()
    ax = RGBAxes(fig, [0.1, 0.1, 0.8, 0.8], pad=0.0)

    # Holen Sie sich die R-, G- und B-Kanäle
    r, g, b = get_rgb()

    # Zeigen Sie das RGB-Bild mit der imshow_rgb()-Methode an
    ax.imshow_rgb(r, g, b)
```
