# Bildrotation durchführen

In diesem Schritt führen wir eine Rotation des Bildes mit der Funktion `rotate_deg` durch. Wir übergeben den Rotationswinkel als Eingabe an die Funktion `rotate_deg`. Wir verwenden die Funktion `do_plot`, um das rotierte Bild anzuzeigen.

```python
# prepare image and figure
fig, ax1 = plt.subplots()
Z = get_image()

# image rotation
do_plot(ax1, Z, mtransforms.Affine2D().rotate_deg(30))
```
