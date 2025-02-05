# 数据可视化

我们将使用 Matplotlib 来可视化生成的数据集。在以下代码块中，我们创建了一个 2x2 的图表，展示了每个数据集的真实聚类情况。

```python
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 12))

axs[0, 0].scatter(X[:, 0], X[:, 1], c=y)
axs[0, 0].set_title("高斯混合聚类")

axs[0, 1].scatter(X_aniso[:, 0], X_aniso[:, 1], c=y)
axs[0, 1].set_title("各向异性分布的聚类")

axs[1, 0].scatter(X_varied[:, 0], X_varied[:, 1], c=y_varied)
axs[1, 0].set_title("方差不等")

axs[1, 1].scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_filtered)
axs[1, 1].set_title("大小不均的聚类")

plt.suptitle("真实聚类情况").set_y(0.95)
plt.show()
```
