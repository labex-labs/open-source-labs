# 对图形 1 进行更改

现在，我们将切换回第一个图形并进行一些更改。我们将使用方形标记在顶部子图中绘制第二个正弦波，并从顶部子图中移除 x 轴刻度标签。

```python
plt.figure(1)

# 顶部子图
plt.subplot(211)
plt.plot(t, s2, 's')
ax = plt.gca()
ax.set_xticklabels([])
```
