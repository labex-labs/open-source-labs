# Cargar el conjunto de datos Iris y graficar la covarianza de las características

Comenzaremos cargando el conjunto de datos Iris y graficando la covarianza de las características para ver cómo están correlacionadas.

```python
import matplotlib.pyplot as plt
import numpy as np

from sklearn.decomposition import FactorAnalysis, PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# Cargar datos de Iris
data = load_iris()
X = StandardScaler().fit_transform(data["data"])
nombres_caracteristicas = data["feature_names"]

# Graficar la covarianza de las características de Iris
ax = plt.axes()

im = ax.imshow(np.corrcoef(X.T), cmap="RdBu_r", vmin=-1, vmax=1)

ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(list(nombres_caracteristicas), rotation=90)
ax.set_yticks([0, 1, 2, 3])
ax.set_yticklabels(list(nombres_caracteristicas))

plt.colorbar(im).ax.set_ylabel("$r$", rotation=0)
ax.set_title("Matriz de correlación de las características de Iris")
plt.tight_layout()
```
