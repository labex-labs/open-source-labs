# Validação Empírica

O próximo passo é validar os limites de Johnson-Lindenstrauss empiricamente no conjunto de dados de documentos de texto 20 newsgroups ou no conjunto de dados de dígitos. Usaremos o conjunto de dados 20 newsgroups e projetamos 300 documentos com 100k recursos no total usando uma matriz aleatória esparsa para espaços euclidianos menores com vários valores para o número alvo de dimensões `n_components`.

```python
import sys
from time import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_20newsgroups_vectorized
from sklearn.random_projection import SparseRandomProjection
from sklearn.metrics.pairwise import euclidean_distances

data = fetch_20newsgroups_vectorized().data[:300]

n_samples, n_features = data.shape
print(f"Embedding {n_samples} samples with dim {n_features} using various random projections")

n_components_range = np.array([300, 1_000, 10_000])
dists = euclidean_distances(data, squared=True).ravel()

# seleciona apenas pares de amostras não idênticas
nonzero = dists != 0
dists = dists[nonzero]

for n_components in n_components_range:
    t0 = time()
    rp = SparseRandomProjection(n_components=n_components)
    projected_data = rp.fit_transform(data)
    print(f"Projected {n_samples} samples from {n_features} to {n_components} in {time() - t0:0.3f}s")
    if hasattr(rp, "components_"):
        n_bytes = rp.components_.data.nbytes
        n_bytes += rp.components_.indices.nbytes
        print(f"Matriz aleatória com tamanho: {n_bytes / 1e6:0.3f} MB")

    projected_dists = euclidean_distances(projected_data, squared=True).ravel()[nonzero]

    plt.figure()
    min_dist = min(projected_dists.min(), dists.min())
    max_dist = max(projected_dists.max(), dists.max())
    plt.hexbin(
        dists,
        projected_dists,
        gridsize=100,
        cmap=plt.cm.PuBu,
        extent=[min_dist, max_dist, min_dist, max_dist],
    )
    plt.xlabel("Distâncias quadradas em pares no espaço original")
    plt.ylabel("Distâncias quadradas em pares no espaço projetado")
    plt.title("Distribuição de distâncias em pares para n_components=%d" % n_components)
    cb = plt.colorbar()
    cb.set_label("Contagem de pares de amostras")

    rates = projected_dists / dists
    print(f"Taxa média de distâncias: {np.mean(rates):.2f} ({np.std(rates):.2f})")

    plt.figure()
    plt.hist(rates, bins=50, range=(0.0, 2.0), edgecolor="k", density=True)
    plt.xlabel("Taxa de distâncias quadradas: projetada / original")
    plt.ylabel("Distribuição de pares de amostras")
    plt.title("Histograma de taxas de distância em pares para n_components=%d" % n_components)
```
