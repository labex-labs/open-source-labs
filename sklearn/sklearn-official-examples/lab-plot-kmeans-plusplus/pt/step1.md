# Gerar dados de amostra

Usaremos a função `make_blobs` da biblioteca scikit-learn para gerar dados de amostra. Esta função gera blobs gaussianos isotrópicos para agrupamento. Geraremos 4000 amostras com 4 centros.

```python
# Gerar dados de amostra
n_samples = 4000
n_components = 4

X, y_true = make_blobs(
    n_samples=n_samples, centers=n_components, cluster_std=0.60, random_state=0
)
X = X[:, ::-1]
```
