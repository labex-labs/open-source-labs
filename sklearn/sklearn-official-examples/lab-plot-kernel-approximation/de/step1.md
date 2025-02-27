# Python-Paket und Datensatzimporte, Datensatz laden

```python
# Standardwissenschaftliche Python-Importe
import matplotlib.pyplot as plt
import numpy as np
from time import time

# Importe von Datensätzen, Klassifizierern und Leistungsmessgrößen
from sklearn import datasets, svm, pipeline
from sklearn.kernel_approximation import RBFSampler, Nystroem
from sklearn.decomposition import PCA

# Der Digits-Datensatz
digits = datasets.load_digits(n_class=9)
```
