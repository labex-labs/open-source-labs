# Gerar dados de amostra

Vamos gerar um conjunto de dados de amostra utilizando a função `make_blobs` do módulo `sklearn.datasets`. A função `make_blobs` gera um conjunto de dados de pontos em um espaço n-dimensional, com cada ponto pertencendo a um dos k clusters. Vamos gerar um conjunto de dados com 300 pontos em um espaço 2-dimensional, com 3 clusters e um desvio padrão de 0,5.

```python
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=300, centers=centers, cluster_std=0.5, random_state=0
)
```
