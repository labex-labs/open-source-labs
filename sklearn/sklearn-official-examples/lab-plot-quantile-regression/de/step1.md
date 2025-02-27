# Datensatzgenerierung

Wir werden zwei synthetische Datensätze mit dem gleichen erwarteten Wert unter Verwendung einer linearen Beziehung mit einem einzelnen Merkmal `x` generieren. Wir werden heteroskedastischen Normalrauschen und asymmetrisches Pareto-Rauschen zu den Datensätzen hinzufügen.

```python
import numpy as np

rng = np.random.RandomState(42)
x = np.linspace(start=0, stop=10, num=100)
X = x[:, np.newaxis]
y_true_mean = 10 + 0.5 * x

# Heteroskedastisches Normalrauschen
y_normal = y_true_mean + rng.normal(loc=0, scale=0.5 + 0.5 * x, size=x.shape[0])

# Asymmetrisches Pareto-Rauschen
a = 5
y_pareto = y_true_mean + 10 * (rng.pareto(a, size=x.shape[0]) - 1 / (a - 1))
```
