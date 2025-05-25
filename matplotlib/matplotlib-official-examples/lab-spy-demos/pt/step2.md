# Criando um Array Aleatório

Em seguida, criaremos um array aleatório com dimensões (20, 20) usando a função `numpy.random.randn`. Também definiremos alguns elementos como zero para criar uma matriz esparsa (sparse matrix).

```python
np.random.seed(19680801)
x = np.random.randn(20, 20)
x[5, :] = 0.
x[:, 12] = 0.
```
