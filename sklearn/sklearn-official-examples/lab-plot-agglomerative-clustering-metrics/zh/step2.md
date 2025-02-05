# 绘制真实标签

我们绘制波形数据的真实标签。

```python
n_clusters = 3

labels = ("波形 1", "波形 2", "波形 3")

colors = ["#f7bd01", "#377eb8", "#f781bf"]

# 绘制真实标签
plt.figure()
plt.axes([0, 0, 1, 1])
for l, color, n in zip(range(n_clusters), colors, labels):
    lines = plt.plot(X[y == l].T, c=color, alpha=0.5)
    lines[0].set_label(n)

plt.legend(loc="best")

plt.axis("tight")
plt.axis("off")
plt.suptitle("真实情况", size=20, y=1)
```
