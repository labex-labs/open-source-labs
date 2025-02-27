# Импорт пакетов Python и датасета, загрузка датасета

```python
# Стандартные научные импорты Python
import matplotlib.pyplot as plt
import numpy as np
from time import time

# Импорт датасетов, классификаторов и метрик производительности
from sklearn import datasets, svm, pipeline
from sklearn.kernel_approximation import RBFSampler, Nystroem
from sklearn.decomposition import PCA

# Датасет digits
digits = datasets.load_digits(n_class=9)
```
