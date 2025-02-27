# Importation des bibliothèques

Nous commencerons par importer les bibliothèques nécessaires pour ce laboratoire. Nous utiliserons la bibliothèque scikit-learn pour récupérer l'ensemble de données, entraîner le modèle et évaluer les performances du modèle.

```python
import time
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import check_random_state
```
