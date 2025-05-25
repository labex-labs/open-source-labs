# Embaralhar os dados

Embaralhamos os dados e o objetivo é reconstruí-los posteriormente usando `SpectralBiclustering`.

```python
import numpy as np

# Criando listas de índices de linha e coluna embaralhados
rng = np.random.RandomState(0)
row_idx_shuffled = rng.permutation(data.shape[0])
col_idx_shuffled = rng.permutation(data.shape[1])

# Redefinindo os dados embaralhados e plotando-os.
data = data[row_idx_shuffled][:, col_idx_shuffled]

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Conjunto de dados embaralhado")
_ = plt.show()
```
