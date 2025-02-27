# Laden des Digits-Datensatzes

Wir werden den Digits-Datensatz laden und nur sechs der zehn verfügbaren Klassen verwenden. Wir werden auch die ersten hundert Ziffern aus diesem Datensatz plotten.

```python
# Load digits dataset
from sklearn.datasets import load_digits

digits = load_digits(n_class=6)
X, y = digits.data, digits.target
n_samples, n_features = X.shape
n_neighbors = 30

# Plot first hundred digits
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=10, ncols=10, figsize=(6, 6))
for idx, ax in enumerate(axs.ravel()):
    ax.imshow(X[idx].reshape((8, 8)), cmap=plt.cm.binary)
    ax.axis("off")
_ = fig.suptitle("A selection from the 64-dimensional digits dataset", fontsize=16)
```
