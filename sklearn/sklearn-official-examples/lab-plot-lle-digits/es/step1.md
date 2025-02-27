# Cargar el conjunto de datos de dígitos

Cargaremos el conjunto de datos de dígitos y solo usaremos seis de las diez clases disponibles. También graficaremos los primeros cien dígitos de este conjunto de datos.

```python
# Cargar el conjunto de datos de dígitos
from sklearn.datasets import load_digits

digits = load_digits(n_class=6)
X, y = digits.data, digits.target
n_samples, n_features = X.shape
n_neighbors = 30

# Graficar los primeros cien dígitos
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=10, ncols=10, figsize=(6, 6))
for idx, ax in enumerate(axs.ravel()):
    ax.imshow(X[idx].reshape((8, 8)), cmap=plt.cm.binary)
    ax.axis("off")
_ = fig.suptitle("Una selección del conjunto de datos de dígitos de 64 dimensiones", fontsize=16)
```
