# Geração de Dados

Usaremos a função `make_blobs` do scikit-learn para gerar diferentes conjuntos de dados com distribuições variadas. No bloco de código a seguir, geramos quatro conjuntos de dados:

- Uma mistura de blobs gaussianos
- Blobs distribuídos anisotrópica
- Blobs com variância desigual
- Blobs com tamanhos desiguais

```python
import numpy as np
from sklearn.datasets import make_blobs

n_samples = 1500
random_state = 170
transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]

X, y = make_blobs(n_samples=n_samples, random_state=random_state)
X_aniso = np.dot(X, transformation)  # Blobs anisotrópicos
X_varied, y_varied = make_blobs(
    n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=random_state
)  # Variância desigual
X_filtered = np.vstack(
    (X[y == 0][:500], X[y == 1][:100], X[y == 2][:10])
)  # Blobs com tamanhos desiguais
y_filtered = [0] * 500 + [1] * 100 + [2] * 10
```
