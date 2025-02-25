# Erzeuge den RangeSlider

Wir werden nun das RangeSlider-Widget erstellen, mit dem wir den Schwellwert des Bildes anpassen können. Wir werden eine neue Achse für den Slider erstellen und sie zur Figur hinzufügen.

```python
slider_ax = fig.add_axes([0.20, 0.1, 0.60, 0.03])
slider = RangeSlider(slider_ax, "Threshold", img.min(), img.max())
```
