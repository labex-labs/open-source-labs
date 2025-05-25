# Carregar e preparar os dados

Primeiro, carregaremos o conjunto de dados iris usando a biblioteca Scikit-learn. O conjunto de dados iris contém 3 classes de plantas de íris, e binarizarmos o conjunto de dados descartando uma classe para criar um problema de classificação binária. Também adicionaremos recursos ruidosos para tornar o problema mais difícil.

```python
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
target_names = iris.target_names
X, y = iris.data, iris.target
X, y = X[y != 2], y[y != 2]
n_samples, n_features = X.shape

# adicionar recursos ruidosos
random_state = np.random.RandomState(0)
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)
```
