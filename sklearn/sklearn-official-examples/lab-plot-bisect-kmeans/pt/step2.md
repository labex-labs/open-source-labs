# Gerar Dados de Amostra

Neste passo, geraremos dados de amostra utilizando a função `make_blobs()` do scikit-learn. Geraremos 10000 amostras com 2 centros.

```python
n_samples = 10000
random_state = 0
X, _ = make_blobs(n_samples=n_samples, centers=2, random_state=random_state)
```
