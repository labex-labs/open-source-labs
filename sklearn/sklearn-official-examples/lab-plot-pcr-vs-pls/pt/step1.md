# Criar um Conjunto de Dados

Começamos criando um conjunto de dados simples com duas características. Usamos a biblioteca numpy para criar o conjunto de dados e a biblioteca matplotlib para o representar graficamente.

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.RandomState(0)
n_samples = 500
cov = [[3, 3], [3, 4]]
X = rng.multivariate_normal(mean=[0, 0], cov=cov, size=n_samples)
plt.scatter(X[:, 0], X[:, 1], alpha=0.3, label="amostras")
plt.gca().set(
    aspect="equal",
    title="Conjunto de dados bidimensional com componentes principais",
    xlabel="primeira característica",
    ylabel="segunda característica",
)
plt.legend()
plt.show()
```
