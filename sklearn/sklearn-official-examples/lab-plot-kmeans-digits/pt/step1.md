# Carregar o Conjunto de Dados

Começaremos carregando o conjunto de dados de dígitos usando a função `load_digits()` do scikit-learn. Esta função retorna as características e as etiquetas do conjunto de dados.

```python
import numpy as np
from sklearn.datasets import load_digits

data, labels = load_digits(return_X_y=True)
(n_samples, n_features), n_digits = data.shape, np.unique(labels).size
```
