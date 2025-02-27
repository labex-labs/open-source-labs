# Crear un conjunto de datos separable en dos clases

Para crear un conjunto de datos separable en dos clases, usaremos la función `make_blobs()` de scikit-learn. Esta función genera manchas gaussianas isotrópicas para agrupamiento y clasificación. Crearemos 40 muestras con dos centros y una semilla aleatoria de 6. También graficaremos los puntos de datos usando `matplotlib`.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# create a two-class separable dataset
X, y = make_blobs(n_samples=40, centers=2, random_state=6)

# plot the data points
plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
plt.show()
```
