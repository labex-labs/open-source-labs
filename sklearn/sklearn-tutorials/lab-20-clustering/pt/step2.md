# Gerar Dados de Amostra

Em seguida, vamos gerar alguns dados de amostra para trabalhar. Usaremos a função `make_blobs` do módulo `sklearn.datasets` para criar um conjunto de dados sintético com clusters.

```python
# Gerar dados de amostra
X, y = make_blobs(n_samples=100, centers=4, random_state=0, cluster_std=1.0)
```
