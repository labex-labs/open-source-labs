# Gerar alguns dados de amostra

Em seguida, geraremos alguns dados de amostra para realizar a estimação de densidade. Para os propósitos deste laboratório, vamos gerar um conjunto de dados unidimensional com 100 pontos. Usaremos uma distribuição normal para gerar os dados.

```python
np.random.seed(0)
X = np.random.normal(0, 1, 100).reshape(-1, 1)
```
