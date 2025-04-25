# 打乱并分割数据

接下来，我们将打乱数据集并将其分割为有标签和无标签的部分。我们将从仅 10 个有标签的点开始。

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
