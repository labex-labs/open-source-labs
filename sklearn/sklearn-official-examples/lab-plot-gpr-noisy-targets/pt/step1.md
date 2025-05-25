# Geração de Dados

Vamos gerar um conjunto de dados sintético. O verdadeiro processo gerador é definido como f(x) = x sen(x).

```python
import numpy as np

X = np.linspace(start=0, stop=10, num=1_000).reshape(-1, 1)
y = np.squeeze(X * np.sin(X))

import matplotlib.pyplot as plt

plt.plot(X, y, label=r"$f(x) = x \sin(x)$", linestyle="dotted")
plt.legend()
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
_ = plt.title("Verdadeiro processo gerador")
```
