# Criar Conjuntos de Dados

Criaremos três conjuntos de dados para fins de visualização. O primeiro conjunto de dados será um conjunto aleatório de 200 amostras de uma distribuição uniforme entre -3 e 3 em ambas as dimensões. O segundo conjunto de dados será um conjunto de 200 amostras geradas usando a função `make_blobs` de `sklearn.datasets`. O terceiro conjunto de dados também será gerado usando a função `make_blobs`.

```python
n_samples = 200
centers_0 = np.array([[0, 0], [0, 5], [2, 4], [8, 8]])
centers_1 = np.array([[0, 0], [3, 1]])

X_list = [
    np.random.RandomState(42).uniform(-3, 3, size=(n_samples, 2)),
    make_blobs(
        n_samples=[n_samples // 10, n_samples * 4 // 10, n_samples // 10, n_samples * 4 // 10],
        cluster_std=0.5,
        centers=centers_0,
        random_state=42,
    )[0],
    make_blobs(
        n_samples=[n_samples // 5, n_samples * 4 // 5],
        cluster_std=0.5,
        centers=centers_1,
        random_state=42,
    )[0],
]
```
