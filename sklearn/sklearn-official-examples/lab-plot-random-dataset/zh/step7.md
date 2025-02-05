# 三个高斯分布数据集

我们创建一个包含三个高斯分布数据集的数据集，并将其绘制出来。

```python
plt.subplot(325)
plt.title("Three blobs", fontsize="small")
X1, Y1 = make_blobs(n_features=2, centers=3)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")
```
