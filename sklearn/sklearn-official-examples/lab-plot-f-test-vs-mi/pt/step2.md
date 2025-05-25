# Criar conjunto de dados

Criaremos um conjunto de dados com 3 características, onde a primeira característica tem uma relação linear com a variável alvo, a segunda característica tem uma relação não linear com a variável alvo e a terceira característica é completamente irrelevante. Criaremos 1000 amostras para este conjunto de dados.

```python
np.random.seed(0)
X = np.random.rand(1000, 3)
y = X[:, 0] + np.sin(6 * np.pi * X[:, 1]) + 0.1 * np.random.randn(1000)
```
