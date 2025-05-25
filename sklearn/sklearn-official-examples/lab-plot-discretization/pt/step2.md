# Criar o Conjunto de Dados

Neste passo, criaremos um conjunto de dados com uma característica de entrada contínua e uma característica de saída contínua. Usaremos o método `numpy.random.RandomState()` para gerar números aleatórios para a característica de entrada e o método `numpy.sin()` para gerar a característica de saída.

```python
rnd = np.random.RandomState(42)
X = rnd.uniform(-3, 3, size=100)
y = np.sin(X) + rnd.normal(size=len(X)) / 3
X = X.reshape(-1, 1)
```
