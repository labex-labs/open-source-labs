# Criar Dados

Criaremos um conjunto de dados com 20 pontos, onde os primeiros 10 pontos pertencem à classe 1 e os últimos 10 pontos pertencem à classe -1.

```python
np.random.seed(0)
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
y = [1] * 10 + [-1] * 10
```
