# Gerar Dados de Brinquedo

Agora, geraremos um conjunto de dados de brinquedo usando a função `make_regression` do scikit-learn. Geraremos um conjunto de dados com 20 amostras, uma característica e uma semente aleatória de 0. Também adicionaremos algum ruído ao conjunto de dados.

```python
rng = np.random.RandomState(0)
X, y = make_regression(
    n_samples=20, n_features=1, random_state=0, noise=4.0, bias=100.0
)
```
