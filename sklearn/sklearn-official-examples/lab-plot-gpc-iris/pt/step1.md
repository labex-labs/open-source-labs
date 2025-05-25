# Importando bibliotecas e conjunto de dados necessários

Primeiro, importamos as bibliotecas necessárias e carregamos o conjunto de dados Iris do scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF

iris = datasets.load_iris()
X = iris.data[:, :2]  # apenas as duas primeiras características são utilizadas.
y = np.array(iris.target, dtype=int)
```
