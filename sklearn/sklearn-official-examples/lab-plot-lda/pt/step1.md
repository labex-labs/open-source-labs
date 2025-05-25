# Gerar Dados Aleatórios

Primeiro, precisamos gerar dados aleatórios com um recurso discriminativo e recursos ruidosos. Usaremos a função `make_blobs` do scikit-learn para gerar dois clusters de dados com um recurso discriminativo. Em seguida, adicionaremos ruído aleatório aos outros recursos.

```python
import numpy as np
from sklearn.datasets import make_blobs

def generate_data(n_samples, n_features):
    """Gerar dados aleatórios em forma de blob com recursos ruidosos.

    Isto retorna uma matriz de dados de entrada com forma `(n_samples, n_features)`
    e uma matriz de rótulos de destino `n_samples`.

    Apenas um recurso contém informações discriminativas, os outros recursos
    contêm apenas ruído.
    """
    X, y = make_blobs(n_samples=n_samples, n_features=1, centers=[[-2], [2]])

    # adicionar recursos não discriminativos
    if n_features > 1:
        X = np.hstack([X, np.random.randn(n_samples, n_features - 1)])
    return X, y
```
