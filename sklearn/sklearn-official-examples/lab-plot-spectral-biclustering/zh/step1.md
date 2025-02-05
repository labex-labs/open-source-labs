# 生成样本数据

我们使用 `make_checkerboard` 函数生成样本数据。`shape=(300, 300)` 内的每个像素都以其颜色表示来自均匀分布的值。噪声是从正态分布中添加的，其中为 `noise` 选择的值是标准差。

```python
from sklearn.datasets import make_checkerboard
from matplotlib import pyplot as plt

n_clusters = (4, 3)
data, rows, columns = make_checkerboard(
    shape=(300, 300), n_clusters=n_clusters, noise=10, shuffle=False, random_state=42
)

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Original dataset")
_ = plt.show()
```
