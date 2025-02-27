# Crear un conjunto de datos

Comenzamos creando un conjunto de datos simple con dos características. Utilizamos la librería numpy para crear el conjunto de datos y la librería matplotlib para graficarlo.

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.RandomState(0)
n_samples = 500
cov = [[3, 3], [3, 4]]
X = rng.multivariate_normal(mean=[0, 0], cov=cov, size=n_samples)
plt.scatter(X[:, 0], X[:, 1], alpha=0.3, label="muestras")
plt.gca().set(
    aspecto="igual",
    título="Conjunto de datos bidimensional con componentes principales",
    xlabel="primera característica",
    ylabel="segunda característica",
)
plt.legend()
plt.show()
```
