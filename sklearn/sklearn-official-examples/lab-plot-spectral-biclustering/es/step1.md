# Generar datos de muestra

Generamos los datos de muestra usando la función `make_checkerboard`. Cada píxel dentro de `shape=(300, 300)` representa con su color un valor de una distribución uniforme. El ruido se agrega a partir de una distribución normal, donde el valor elegido para `noise` es la desviación estándar.

```python
from sklearn.datasets import make_checkerboard
from matplotlib import pyplot as plt

n_clusters = (4, 3)
data, rows, columns = make_checkerboard(
    shape=(300, 300), n_clusters=n_clusters, noise=10, shuffle=False, random_state=42
)

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Original dataset")
_ = plt.show()
```
