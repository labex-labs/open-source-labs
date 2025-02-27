# Importation des bibliothèques

Tout d'abord, nous devons importer les bibliothèques nécessaires. Nous utiliserons `matplotlib` pour la visualisation, `datasets` et `metrics` de `sklearn` pour charger et évaluer le jeu de données, et `svm` pour entraîner la machine à vecteurs de support.

```python
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
```
