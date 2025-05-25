# Importando Bibliotecas Necessárias

As seguintes bibliotecas serão utilizadas neste laboratório: `pandas`, `numpy`, `matplotlib`, `sklearn.datasets`, `RandomForestClassifier`, `randint` e `HalvingRandomSearchCV`. Importe-as utilizando o código seguinte:

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
