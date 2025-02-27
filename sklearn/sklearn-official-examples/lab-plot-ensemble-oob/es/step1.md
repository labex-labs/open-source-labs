# Importar las bibliotecas necesarias

Comenzaremos importando las bibliotecas necesarias, incluyendo scikit-learn, NumPy y Matplotlib. También estableceremos un valor de estado aleatorio para garantizar la reproducibilidad.

```python
import matplotlib.pyplot as plt
from collections import OrderedDict
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

RANDOM_STATE = 123
```
