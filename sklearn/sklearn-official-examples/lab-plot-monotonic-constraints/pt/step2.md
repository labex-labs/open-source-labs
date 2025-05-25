# Gerar Dados

Vamos gerar um conjunto de dados artificial onde o valor-alvo tem correlação positiva com a primeira característica e correlação negativa com a segunda característica. Também adicionaremos algum ruído aleatório para tornar os dados mais realistas.

```python
rng = np.random.RandomState(0)

n_samples = 1000
f_0 = rng.rand(n_samples)
f_1 = rng.rand(n_samples)
X = np.c_[f_0, f_1]
noise = rng.normal(loc=0.0, scale=0.01, size=n_samples)

y = 5 * f_0 + np.sin(10 * np.pi * f_0) - 5 * f_1 - np.cos(10 * np.pi * f_1) + noise
```
