# Importation des bibliothèques

Nous commencerons par importer les bibliothèques nécessaires pour ce laboratoire. Nous utiliserons la bibliothèque scikit-learn pour générer l'ensemble de données et entraîner les modèles de régression logistique, et la bibliothèque matplotlib pour tracer la frontière de décision.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import DecisionBoundaryDisplay
```
