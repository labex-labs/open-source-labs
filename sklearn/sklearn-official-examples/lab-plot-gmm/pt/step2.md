# Gerar Dados

Neste passo, geraremos um conjunto de dados de amostra que consiste em duas distribuições gaussianas com médias e covariâncias diferentes.

```python
n_samples = 500

np.random.seed(0)
C = np.array([[0.0, -0.1], [1.7, 0.4]])
X = np.r_[
    np.dot(np.random.randn(n_samples, 2), C),
    0.7 * np.random.randn(n_samples, 2) + np.array([-6, 3]),
]
```
