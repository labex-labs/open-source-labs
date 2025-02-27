# Importation des bibliothèques requises

Les bibliothèques suivantes seront utilisées dans ce laboratoire : `pandas`, `numpy`, `matplotlib`, `sklearn.datasets`, `RandomForestClassifier`, `randint` et `HalvingRandomSearchCV`. Importez-les à l'aide du code suivant :

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
