# Importieren der erforderlichen Bibliotheken

In diesem Lab werden die folgenden Bibliotheken verwendet: `pandas`, `numpy`, `matplotlib`, `sklearn.datasets`, `RandomForestClassifier`, `randint` und `HalvingRandomSearchCV`. Importiere sie mit dem folgenden Code:

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
