# Geração de Dados de Amostra

Em seguida, geraremos dados de amostra usando a função `make_blobs` do módulo `sklearn.datasets`. Criaremos um conjunto de dados com 10.000 amostras e três clusters com centros em `[[1, 1], [-1, -1], [1, -1]]` e um desvio padrão de 0,6.

```python
centers = [[1, 1], [-1, -1], [1, -1]]
X, _ = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6)
```
