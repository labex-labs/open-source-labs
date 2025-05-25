# Importar bibliotecas e carregar o conjunto de dados

Começaremos importando as bibliotecas necessárias e carregando o conjunto de dados Wine do scikit-learn. O conjunto de dados Wine contém informações sobre diferentes tipos de vinho, incluindo suas propriedades químicas.

```python
import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

# Carregar o conjunto de dados
X1 = load_wine()["data"][:, [1, 2]]  # dois clusters
X2 = load_wine()["data"][:, [6, 9]]  # em forma de "banana"
```
