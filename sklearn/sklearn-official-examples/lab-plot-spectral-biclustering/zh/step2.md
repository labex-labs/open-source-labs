# 打乱数据

我们打乱数据，目的是之后使用“谱双聚类（SpectralBiclustering）”对其进行重构。

```python
import numpy as np

# 创建打乱后的行索引和列索引列表
rng = np.random.RandomState(0)
row_idx_shuffled = rng.permutation(data.shape[0])
col_idx_shuffled = rng.permutation(data.shape[1])

# 重新定义打乱后的数据并绘图。
data = data[row_idx_shuffled][:, col_idx_shuffled]

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Shuffled dataset")
_ = plt.show()
```
