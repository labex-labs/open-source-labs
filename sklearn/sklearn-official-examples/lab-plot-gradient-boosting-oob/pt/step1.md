# Gerar Dados

O primeiro passo é gerar alguns dados de exemplo que podemos usar para treinar e testar nosso modelo. Usaremos a função `make_classification` do módulo `sklearn.datasets` para gerar um problema de classificação binária aleatória com 3 recursos informativos.

```python
import numpy as np
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=3, n_informative=3,
                           n_redundant=0, n_classes=2, random_state=1)
```
