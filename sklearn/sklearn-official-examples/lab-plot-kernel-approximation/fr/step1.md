# Importation du package Python et du jeu de données, Chargement du jeu de données

```python
# Importations scientifiques standard de Python
import matplotlib.pyplot as plt
import numpy as np
from time import time

# Importation de jeux de données, de classifieurs et de mesures de performance
from sklearn import datasets, svm, pipeline
from sklearn.kernel_approximation import RBFSampler, Nystroem
from sklearn.decomposition import PCA

# Le jeu de données des chiffres
digits = datasets.load_digits(n_class=9)
```
