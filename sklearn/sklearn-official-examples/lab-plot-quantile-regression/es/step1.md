# Generación del conjunto de datos

Generaremos dos conjuntos de datos sintéticos con el mismo valor esperado utilizando una relación lineal con una sola característica `x`. Agregaremos ruido normal heterocedástico y ruido de Pareto asimétrico a los conjuntos de datos.

```python
import numpy as np

rng = np.random.RandomState(42)
x = np.linspace(start=0, stop=10, num=100)
X = x[:, np.newaxis]
y_true_mean = 10 + 0.5 * x

# Ruido normal heterocedástico
y_normal = y_true_mean + rng.normal(loc=0, scale=0.5 + 0.5 * x, size=x.shape[0])

# Ruido de Pareto asimétrico
a = 5
y_pareto = y_true_mean + 10 * (rng.pareto(a, size=x.shape[0]) - 1 / (a - 1))
```
