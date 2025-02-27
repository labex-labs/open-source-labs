# Swiss Roll-Datensatz generieren

Wir beginnen mit der Generierung des Swiss Roll-Datensatzes mithilfe der Funktion `make_swiss_roll()` aus `sklearn.datasets`. Diese Funktion erzeugt einen 3D-Datensatz mit einer spiralförmigen Gestalt.

```python
import matplotlib.pyplot as plt
from sklearn import manifold, datasets

sr_points, sr_color = datasets.make_swiss_roll(n_samples=1500, random_state=0)
```
