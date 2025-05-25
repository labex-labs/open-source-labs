# Carregar os Dados

Começaremos carregando o conjunto de dados Iris e selecionando apenas as duas primeiras características para fins de visualização.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y != 0, :2]
y = y[y != 0]
```
