# Definir uma função para obter as médias iniciais

Em seguida, definiremos uma função `get_initial_means` que recebe os dados de amostra, o método de inicialização e o estado aleatório como entradas e retorna as médias de inicialização.

```python
def get_initial_means(X, init_params, r):
    # Executar um GaussianMixture com max_iter=0 para produzir as médias de inicialização
    gmm = GaussianMixture(
        n_components=4, init_params=init_params, tol=1e-9, max_iter=0, random_state=r
    ).fit(X)
    return gmm.means_
```
