# データをシャッフルして分割する

次に、データセットをシャッフルして、ラベル付きと非ラベル付きの部分に分割します。最初は10個のラベル付きポイントだけで始めます。

```python
import numpy as np

rng = np.random.RandomState(0)
indices = np.arange(len(digits.data))
rng.shuffle(indices)

X = digits.data[indices[:330]]
y = digits.target[indices[:330]]
images = digits.images[indices[:330]]

n_total_samples = len(y)
n_labeled_points = 10
unlabeled_indices = np.arange(n_total_samples)[n_labeled_points:]
```
