# Importation des bibliothèques

Dans cette étape, nous importons les bibliothèques nécessaires : `numpy`, `matplotlib`, `make_multilabel_classification` de `sklearn.datasets`, `OneVsRestClassifier` et `SVC` de `sklearn.multiclass`, `PCA` et `CCA` de `sklearn.decomposition`.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_multilabel_classification
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import CCA
```
