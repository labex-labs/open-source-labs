# Preparar Dados

Em seguida, prepararemos os dados para nosso box plot. Criaremos alguns dados fictícios para os valores de x e y, bem como os valores de erro.

```python
# Número de pontos de dados
n = 5

# Dados fictícios
np.random.seed(19680801)
x = np.arange(0, n, 1)
y = np.random.rand(n) * 5.

# Erros fictícios (acima e abaixo)
xerr = np.random.rand(2, n) + 0.1
yerr = np.random.rand(2, n) + 0.2
```
