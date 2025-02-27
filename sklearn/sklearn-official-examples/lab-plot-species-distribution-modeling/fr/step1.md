# Importation des bibliothèques

Dans cette étape, nous allons importer les bibliothèques nécessaires à notre analyse. Nous importerons la bibliothèque scikit-learn pour l'apprentissage automatique, numpy pour les calculs numériques et matplotlib pour la visualisation.

```python
from time import time

import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils import Bunch
from sklearn.datasets import fetch_species_distributions
from sklearn import svm, metrics
```
