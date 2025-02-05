# 将初始化种子与样本数据一起绘制

我们将使用 matplotlib 库把初始化种子与样本数据一起绘制出来。初始化种子将显示为蓝色点，样本数据将显示为彩色点。

```python
# 将初始化种子与样本数据一起绘制
plt.figure(1)
colors = ["#4EACC5", "#FF9C34", "#4E9A06", "m"]

for k, col in enumerate(colors):
    cluster_data = y_true == k
    plt.scatter(X[cluster_data, 0], X[cluster_data, 1], c=col, marker=".", s=10)

plt.scatter(centers_init[:, 0], centers_init[:, 1], c="b", s=50)
plt.title("K-Means++ Initialization")
plt.xticks([])
plt.yticks([])
plt.show()
```
