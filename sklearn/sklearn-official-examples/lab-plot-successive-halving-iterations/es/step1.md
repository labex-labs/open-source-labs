# Importando las bibliotecas necesarias

En este laboratorio se usarán las siguientes bibliotecas: `pandas`, `numpy`, `matplotlib`, `sklearn.datasets`, `RandomForestClassifier`, `randint` y `HalvingRandomSearchCV`. Importelas con el siguiente código:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import HalvingRandomSearchCV
```
