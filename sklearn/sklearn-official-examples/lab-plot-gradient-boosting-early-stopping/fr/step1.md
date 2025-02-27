# Charger les bibliothèques et les données requises

Tout d'abord, nous devons charger les bibliothèques et les données requises. Nous utiliserons la bibliothèque scikit - learn pour la mise en œuvre du gradient boosting.

```python
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn import ensemble
from sklearn import datasets
from sklearn.model_selection import train_test_split

data_list = [
    datasets.load_iris(return_X_y=True),
    datasets.make_classification(n_samples=800, random_state=0),
    datasets.make_hastie_10_2(n_samples=2000, random_state=0),
]
names = ["Données Iris", "Données de classification", "Données Hastie"]
n_estimators = 200
```
