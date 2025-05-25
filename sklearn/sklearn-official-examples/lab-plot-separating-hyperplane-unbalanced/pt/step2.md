# Criar Dados

Criaremos dois grupos de pontos aleatórios usando a função `make_blobs`. Criaremos um grupo com 1000 pontos e outro com 100 pontos. Os centros dos grupos serão `[0.0, 0.0]` e `[2.0, 2.0]`, respetivamente. O parâmetro `clusters_std` controla o desvio padrão dos grupos.

```python
n_samples_1 = 1000
n_samples_2 = 100
centers = [[0.0, 0.0], [2.0, 2.0]]
clusters_std = [1.5, 0.5]
X, y = make_blobs(
    n_samples=[n_samples_1, n_samples_2],
    centers=centers,
    cluster_std=clusters_std,
    random_state=0,
    shuffle=False,
)
```
