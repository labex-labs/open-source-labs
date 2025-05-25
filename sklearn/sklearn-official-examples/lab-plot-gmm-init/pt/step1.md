# Importar bibliotecas e gerar dados de amostra

Começaremos importando as bibliotecas necessárias e gerando alguns dados de amostra usando a função `make_blobs` do scikit-learn.

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.utils.extmath import row_norms
from sklearn.datasets._samples_generator import make_blobs
from timeit import default_timer as timer

# Gerar alguns dados
X, y_true = make_blobs(n_samples=4000, centers=4, cluster_std=0.60, random_state=0)
X = X[:, ::-1]

n_samples = 4000
n_components = 4
x_squared_norms = row_norms(X, squared=True)
```
