# Mélanger les données

Nous mélangeons les données et le but est de les reconstruire ensuite à l'aide de `SpectralBiclustering`.

```python
import numpy as np

# Création de listes d'indices de lignes et de colonnes mélangés
rng = np.random.RandomState(0)
row_idx_shuffled = rng.permutation(data.shape[0])
col_idx_shuffled = rng.permutation(data.shape[1])

# Redéfinition des données mélangées et affichage.
data = data[row_idx_shuffled][:, col_idx_shuffled]

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Shuffled dataset")
_ = plt.show()
```
