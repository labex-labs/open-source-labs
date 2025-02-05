# 绘制样本

我们将使用 `matplotlib.pyplot` 中的 `scatter` 函数来绘制样本。

```python
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, edgecolors="k")
```
