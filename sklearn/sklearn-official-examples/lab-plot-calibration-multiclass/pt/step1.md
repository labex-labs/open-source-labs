# Dados

Geramos um conjunto de dados de classificação com 2000 amostras, 2 características e 3 classes de destino. Em seguida, dividimos os dados da seguinte forma:

- treino: 600 amostras (para treinar o classificador)
- validação: 400 amostras (para calibrar as probabilidades previstas)
- teste: 1000 amostras

```python
import numpy as np
from sklearn.datasets import make_blobs

np.random.seed(0)

X, y = make_blobs(
    n_samples=2000, n_features=2, centers=3, random_state=42, cluster_std=5.0
)
X_train, y_train = X[:600], y[:600]
X_valid, y_valid = X[600:1000], y[600:1000]
X_train_valid, y_train_valid = X[:1000], y[:1000]
X_test, y_test = X[1000:], y[1000:]
```
