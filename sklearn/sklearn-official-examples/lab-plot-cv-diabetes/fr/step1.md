# Charger et préparer l'ensemble de données

Tout d'abord, nous allons charger et préparer l'ensemble de données sur le diabète. Nous n'utiliserons que les 150 premières échantillons pour cet exercice.

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

X, y = datasets.load_diabetes(return_X_y=True)
X = X[:150]
y = y[:150]
```
