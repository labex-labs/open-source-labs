# Bild skalieren und spiegeln

In diesem Schritt führen wir eine Skalierung und Spiegelung des Bildes mit der Funktion `scale` durch. Wir übergeben die Skalierungs- und Spiegelungsfaktoren als Eingaben an die Funktion `scale`. Wir verwenden die Funktion `do_plot`, um das skalierte und gespiegelte Bild anzuzeigen.

```python
# prepare image and figure
fig, ax3 = plt.subplots()
Z = get_image()

# scale and reflection
do_plot(ax3, Z, mtransforms.Affine2D().scale(-1,.5))
```
