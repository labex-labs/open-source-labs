# Importation des bibliothèques

Nous commencerons par importer les bibliothèques nécessaires pour ce laboratoire. Nous utiliserons scikit-learn pour créer des jeux de données synthétiques, MLPClassifier pour construire le modèle MLP, StandardScaler pour standardiser les données et make_pipeline pour créer un pipeline de transformations et de classifieur.

```python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
```
