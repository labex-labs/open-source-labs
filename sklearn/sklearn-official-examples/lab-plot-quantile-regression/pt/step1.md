# Geração de Conjuntos de Dados

Vamos gerar dois conjuntos de dados sintéticos com o mesmo valor esperado usando uma relação linear com um único recurso `x`. Adicionaremos ruído normal heterocedástico e ruído de Pareto assimétrico aos conjuntos de dados.

```python
import numpy as np

rng = np.random.RandomState(42)
x = np.linspace(start=0, stop=10, num=100)
X = x[:, np.newaxis]
y_true_mean = 10 + 0.5 * x

# Ruído Normal Heterocedástico
y_normal = y_true_mean + rng.normal(loc=0, scale=0.5 + 0.5 * x, size=x.shape[0])

# Ruído de Pareto Assimétrico
a = 5
y_pareto = y_true_mean + 10 * (rng.pareto(a, size=x.shape[0]) - 1 / (a - 1))
```
