# Importation des bibliothèques nécessaires

Tout d'abord, nous devons importer les bibliothèques nécessaires. Nous utiliserons Matplotlib, NumPy et certains modules de `mpl_toolkits.axisartist` et `mpl_toolkits.axisartist.grid_finder`.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D
import mpl_toolkits.axisartist.angle_helper as angle_helper
import mpl_toolkits.axisartist.floating_axes as floating_axes
from mpl_toolkits.axisartist.grid_finder import (DictFormatter, FixedLocator,
                                                 MaxNLocator)
```
