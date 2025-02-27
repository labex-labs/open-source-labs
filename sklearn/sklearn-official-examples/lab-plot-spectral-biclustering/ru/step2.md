# Перемешивание данных

Мы перемешиваем данные, и цель - потом реконструировать их с использованием `SpectralBiclustering`.

```python
import numpy as np

# Создание списков перемешанных индексов строк и столбцов
rng = np.random.RandomState(0)
row_idx_shuffled = rng.permutation(data.shape[0])
col_idx_shuffled = rng.permutation(data.shape[1])

# Переопределение перемешанных данных и их отображение.
data = data[row_idx_shuffled][:, col_idx_shuffled]

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Shuffled dataset")
_ = plt.show()
```
