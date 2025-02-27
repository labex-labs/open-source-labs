# Importation des bibliothèques et chargement de l'ensemble de données

Nous allons commencer par importer les bibliothèques nécessaires et charger l'ensemble de données Wine à partir de scikit-learn. L'ensemble de données Wine contient des informations sur différents types de vins, y compris leurs propriétés chimiques.

```python
import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

# Chargement de l'ensemble de données
X1 = load_wine()["data"][:, [1, 2]]  # deux grappes
X2 = load_wine()["data"][:, [6, 9]]  # en forme de "banane"
```
