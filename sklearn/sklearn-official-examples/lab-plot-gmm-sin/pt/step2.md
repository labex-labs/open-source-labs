# Gerar Conjunto de Dados

Em seguida, geraremos um conjunto de dados que segue uma curva senoidal com ruído.

```python
# Parâmetros
n_samples = 100

# Gerar amostra aleatória seguindo uma curva senoidal
np.random.seed(0)
X = np.zeros((n_samples, 2))
step = 4.0 * np.pi / n_samples

for i in range(X.shape[0]):
    x = i * step - 6.0
    X[i, 0] = x + np.random.normal(0, 0.1)
    X[i, 1] = 3.0 * (np.sin(x) + np.random.normal(0, 0.2))
```
