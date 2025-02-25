# Créer le RangeSlider

Nous allons maintenant créer le widget RangeSlider, qui nous permettra de régler le seuil de l'image. Nous allons créer un nouvel axe pour le curseur et l'ajouter à la figure.

```python
slider_ax = fig.add_axes([0.20, 0.1, 0.60, 0.03])
slider = RangeSlider(slider_ax, "Threshold", img.min(), img.max())
```
