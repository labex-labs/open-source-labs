# Définissez la classe MercatorLatitudeScale

Ensuite, nous allons définir la classe `MercatorLatitudeScale` qui implémentera l'échelle personnalisée. Cette classe héritera de `mscale.ScaleBase`.

```python
class MercatorLatitudeScale(mscale.ScaleBase):
    """
    Échelle les données dans la plage -pi/2 à pi/2 (-90 à 90 degrés) en utilisant
    le système utilisé pour échelle les latitudes dans une projection Mercator__.

    La fonction d'échelle :
      ln(tan(y) + sec(y))

    La fonction d'échelle inverse :
      atan(sinh(y))

    Étant donné que l'échelle Mercator tend vers l'infini à +/- 90 degrés,
    il existe un seuil défini par l'utilisateur, au-dessus et en-dessous duquel rien
    ne sera tracé. Cela est par défaut à +/- 85 degrés.

    __ https://en.wikipedia.org/wiki/Mercator_projection
    """
```
