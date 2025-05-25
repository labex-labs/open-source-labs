# Criando o Conjunto de Dados XOR

Neste passo, criaremos um conjunto de dados XOR usando o numpy. Usaremos a função `logical_xor` para criar rótulos com base nas características de entrada.

```python
xx, yy = np.meshgrid(np.linspace(-3, 3, 50), np.linspace(-3, 3, 50))
rng = np.random.RandomState(0)
X = rng.randn(200, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
```
