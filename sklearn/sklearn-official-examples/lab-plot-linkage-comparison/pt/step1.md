# Importar Bibliotecas e Carregar Dados

Começaremos importando as bibliotecas necessárias e carregando os conjuntos de dados de exemplo que usaremos nos nossos exemplos de agrupamento hierárquico.

```python
import time
import warnings

import numpy as np
import matplotlib.pyplot as plt

from sklearn import cluster, datasets
from sklearn.preprocessing import StandardScaler
from itertools import cycle, islice

np.random.seed(0)

# %%
# Gerar conjuntos de dados. Escolhemos um tamanho suficientemente grande para ver a escalabilidade dos algoritmos, mas não muito grande para evitar tempos de execução demasiado longos

n_samples = 1500
noisy_circles = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.05)
noisy_moons = datasets.make_moons(n_samples=n_samples, noise=0.05)
blobs = datasets.make_blobs(n_samples=n_samples, random_state=8)
no_structure = np.random.rand(n_samples, 2), None

# Dados distribuídos anisotrópica
random_state = 170
X, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
transformation = [[0.6, -0.6], [-0.4, 0.8]]
X_aniso = np.dot(X, transformation)
aniso = (X_aniso, y)

# Blobs com variâncias variadas
varied = datasets.make_blobs(
    n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=random_state
)
```
