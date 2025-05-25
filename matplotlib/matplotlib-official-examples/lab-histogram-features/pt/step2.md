# Gerar dados de amostra

Nesta etapa, geraremos dados de amostra usando numpy. Geraremos dados aleatórios de uma distribuição normal com média 100 e desvio padrão 15.

```python
np.random.seed(19680801)
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(437)
```
