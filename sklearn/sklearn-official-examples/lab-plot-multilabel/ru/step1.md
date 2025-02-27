# Импорт библиотек

В этом шаге мы импортируем необходимые библиотеки: `numpy`, `matplotlib`, `make_multilabel_classification` из `sklearn.datasets`, `OneVsRestClassifier` и `SVC` из `sklearn.multiclass`, `PCA` и `CCA` из `sklearn.decomposition`.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_multilabel_classification
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import CCA
```
