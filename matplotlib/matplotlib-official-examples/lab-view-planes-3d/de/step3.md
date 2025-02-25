# Definieren der primären 3D-Ansichtsebenen und ihrer Winkel

Wir definieren die primären 3D-Ansichtsebenen und ihre entsprechenden Höhen-, Azimut- und Rollwinkel.

```python
views = [('XY',   (90, -90, 0)),
         ('XZ',    (0, -90, 0)),
         ('YZ',    (0,   0, 0)),
         ('-XY', (-90,  90, 0)),
         ('-XZ',   (0,  90, 0)),
         ('-YZ',   (0, 180, 0))]
```
