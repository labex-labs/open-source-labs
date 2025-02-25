# Ajouter des lignes verticales à l'histogramme

Pour faciliter la visualisation de l'effet du seuillage, nous allons ajouter des lignes verticales à l'histogramme pour indiquer les valeurs de seuil actuelles. Nous allons créer deux lignes pour les valeurs de seuil inférieur et supérieur respectivement.

```python
lower_limit_line = axs[1].axvline(slider.val[0], color='k')
upper_limit_line = axs[1].axvline(slider.val[1], color='k')
```
