# Gerar Dados

Geraremos 100.000 pontos de dados usando `numpy.random.standard_normal()` e `numpy.random.standard_normal()`. `standard_normal()` gera números aleatórios de uma distribuição normal padrão com média 0 e desvio padrão 1.

```python
np.random.seed(19680801)

n = 100_000
x = np.random.standard_normal(n)
y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)
xlim = x.min(), x.max()
ylim = y.min(), y.max()
```
