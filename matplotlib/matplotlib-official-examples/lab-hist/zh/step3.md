# 绘制二维直方图

要绘制二维直方图，只需要两个长度相同的向量，分别对应直方图的每个轴。

```python
fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(dist1, dist2)

plt.show()
```
