# Importez les bibliothèques nécessaires et générez des données

Tout d'abord, nous devons importer les bibliothèques nécessaires et générer un ensemble de données approprié pour la classification. Dans cet exemple, nous allons générer 50 points séparables en utilisant la fonction `make_blobs` de Scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_blobs

# nous créons 50 points séparables
X, Y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.60)
```
