# Importar Bibliotecas

Neste passo, importamos as bibliotecas necessárias: `numpy`, `matplotlib`, `make_multilabel_classification` de `sklearn.datasets`, `OneVsRestClassifier` e `SVC` de `sklearn.multiclass`, `PCA` e `CCA` de `sklearn.decomposition`.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_multilabel_classification
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import CCA
```
