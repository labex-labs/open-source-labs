# Criar os Dados

Criaremos um conjunto de dados simulado que consiste em 500 amostras, 25 recursos e uma classificação de 5. Também adicionaremos ruído homocedástico e heterocedástico ao conjunto de dados.

```python
import numpy as np
from scipy import linalg

n_samples, n_features, rank = 500, 25, 5
sigma = 1.0
rng = np.random.RandomState(42)
U, _, _ = linalg.svd(rng.randn(n_features, n_features))
X = np.dot(rng.randn(n_samples, rank), U[:, :rank].T)

# Adicionando ruído homocedástico
X_homo = X + sigma * rng.randn(n_samples, n_features)

# Adicionando ruído heterocedástico
sigmas = sigma * rng.rand(n_features) + sigma / 2.0
X_hetero = X + rng.randn(n_samples, n_features) * sigmas
```
