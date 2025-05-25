# Gerar Dados Sintéticos

Em seguida, vamos gerar alguns dados sintéticos para trabalhar. Criaremos uma função-alvo sinusoidal e adicionaremos algum ruído aleatório a ela.

```python
# Gerar dados de entrada
np.random.seed(0)
X = np.sort(5 * np.random.rand(100, 1), axis=0)
y = np.sin(X).ravel()
y += 0.5 * (0.5 - np.random.rand(y.size))
```
