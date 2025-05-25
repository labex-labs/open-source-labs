# Gerar Dados

Vamos gerar 30 amostras de uma função cosseno, com algum ruído aleatório adicionado às amostras.

```python
def true_fun(X):
    return np.cos(1.5 * np.pi * X)

np.random.seed(0)

n_samples = 30

X = np.sort(np.random.rand(n_samples))
y = true_fun(X) + np.random.randn(n_samples) * 0.1
```
