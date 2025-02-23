# Mehrere Transformationen durchführen

In diesem Schritt führen wir mehrere Transformationen des Bildes mit den Funktionen `rotate_deg`, `skew_deg`, `scale` und `translate` durch. Wir übergeben die Transformationsparameter als Eingaben an die jeweiligen Funktionen. Wir verwenden die Funktion `do_plot`, um das transformierte Bild anzuzeigen.

```python
# prepare image and figure
fig, ax4 = plt.subplots()
Z = get_image()

# everything and a translation
do_plot(ax4, Z, mtransforms.Affine2D().
        rotate_deg(30).skew_deg(30, 15).scale(-1,.5).translate(.5, -1))
```
