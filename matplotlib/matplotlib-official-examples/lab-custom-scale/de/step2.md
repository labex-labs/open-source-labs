# Definieren der MercatorLatitudeScale-Klasse

Als nächstes definieren wir die Klasse `MercatorLatitudeScale`, die die benutzerdefinierte Skala implementieren wird. Diese Klasse erbt von `mscale.ScaleBase`.

```python
class MercatorLatitudeScale(mscale.ScaleBase):
    """
    Skaliert Daten im Bereich von -pi/2 bis pi/2 (-90 bis 90 Grad) unter Verwendung
    des Systems, das zur Skalierung von Breitengraden bei einer Mercator__-Projektion verwendet wird.

    Die Skalenfunktion lautet:
      ln(tan(y) + sec(y))

    Die inverse Skalenfunktion lautet:
      atan(sinh(y))

    Da die Mercator-Skala bei +/- 90 Grad gegen unendlich strebt,
    gibt es einen benutzerdefinierten Schwellenwert, oberhalb und unterhalb dessen
    nichts geplottet wird. Dies ist standardmäßig auf +/- 85 Grad eingestellt.

    __ https://en.wikipedia.org/wiki/Mercator_projection
    """
```
