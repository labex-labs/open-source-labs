# Mischen der Daten

Wir mischen die Daten, und das Ziel ist es, sie anschließend mit `SpectralBiclustering` wiederherzustellen.

```python
import numpy as np

# Erstellen von Listen mit gemischten Zeilen- und Spaltenindizes
rng = np.random.RandomState(0)
row_idx_shuffled = rng.permutation(data.shape[0])
col_idx_shuffled = rng.permutation(data.shape[1])

# Neudefinieren der gemischten Daten und Darstellung
data = data[row_idx_shuffled][:, col_idx_shuffled]

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Gemischter Datensatz")
_ = plt.show()
```
