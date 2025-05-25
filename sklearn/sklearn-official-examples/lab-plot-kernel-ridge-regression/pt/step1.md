# Gerar Dados de Amostra

Vamos gerar um conjunto de dados composto por uma função-alvo sinusoidal e ruído forte adicionado a cada quinto ponto de dados.

```python
import numpy as np

# Gerar dados de amostra
rng = np.random.RandomState(42)
X = 5 * rng.rand(10000, 1)
y = np.sin(X).ravel()

# Adicionar ruído aos alvos
y[::5] += 3 * (0.5 - rng.rand(X.shape[0] // 5))

X_plot = np.linspace(0, 5, 100000)[:, None]
```
