# Importation des bibliothèques

Tout d'abord, nous allons importer les bibliothèques nécessaires pour créer une projection personnalisée.

```python
import numpy as np
import matplotlib
from matplotlib.axes import Axes
import matplotlib.axis as maxis
from matplotlib.patches import Circle
from matplotlib.path import Path
from matplotlib.projections import register_projection
import matplotlib.spines as mspines
from matplotlib.ticker import FixedLocator, Formatter, NullLocator
from matplotlib.transforms import Affine2D, BboxTransformTo, Transform
```
