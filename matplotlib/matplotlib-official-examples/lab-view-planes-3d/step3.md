# Define the primary 3D view planes and their angles

We define the primary 3D view planes and their corresponding elevation, azimuth, and roll angles.

```python
views = [('XY',   (90, -90, 0)),
         ('XZ',    (0, -90, 0)),
         ('YZ',    (0,   0, 0)),
         ('-XY', (-90,  90, 0)),
         ('-XZ',   (0,  90, 0)),
         ('-YZ',   (0, 180, 0))]
```
