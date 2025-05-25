# Carregar o Conjunto de Dados de Dígitos

Carregaremos o conjunto de dados de dígitos e usaremos apenas seis das dez classes disponíveis. Também plotaremos os cem primeiros dígitos deste conjunto de dados.

```python
# Carregar o conjunto de dados de dígitos
from sklearn.datasets import load_digits

digits = load_digits(n_class=6)
X, y = digits.data, digits.target
n_samples, n_features = X.shape
n_neighbors = 30

# Plotar os cem primeiros dígitos
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=10, ncols=10, figsize=(6, 6))
for idx, ax in enumerate(axs.ravel()):
    ax.imshow(X[idx].reshape((8, 8)), cmap=plt.cm.binary)
    ax.axis("off")
_ = fig.suptitle("Uma seleção do conjunto de dados de dígitos 64-dimensionais", fontsize=16)
```
