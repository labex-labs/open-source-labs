# Definir a semente aleatória e gerar os dados

Nesta etapa, definiremos a semente aleatória e geraremos os dados. Geraremos 100 pontos de dados de uma distribuição normal com média 200 e desvio padrão 25.

```python
np.random.seed(19680801)
mu = 200
sigma = 25
data = np.random.normal(mu, sigma, size=100)
```
