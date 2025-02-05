# 绘制数据点

我们使用 Matplotlib 的 scatter 函数来绘制输入数据点。

```python
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor="k", s=20)
```
