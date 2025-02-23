# Bildverzerrung durchführen

In diesem Schritt führen wir eine Verzerrung des Bildes mit der Funktion `skew_deg` durch. Wir übergeben die Verzerrungswinkel als Eingaben an die Funktion `skew_deg`. Wir verwenden die Funktion `do_plot`, um das verzerrte Bild anzuzeigen.

```python
# prepare image and figure
fig, ax2 = plt.subplots()
Z = get_image()

# image skew
do_plot(ax2, Z, mtransforms.Affine2D().skew_deg(30, 15))
```
