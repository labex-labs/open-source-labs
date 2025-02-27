# Importar bibliotecas

En este paso, importaremos las bibliotecas necesarias para nuestro análisis. Importaremos la biblioteca scikit-learn para el aprendizaje automático, numpy para el cálculo numérico y matplotlib para la visualización.

```python
from time import time

import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils import Bunch
from sklearn.datasets import fetch_species_distributions
from sklearn import svm, metrics
```
