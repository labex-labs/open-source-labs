# 更改直方图样式

我们可以通过在 `hist` 函数中指定 `histtype` 参数来更改直方图的样式。在这个例子中，我们将创建一个带有颜色填充的阶梯曲线直方图。

```python
plt.hist(x, bins=20, density=True, histtype='stepfilled', facecolor='g', alpha=0.75)
plt.show()
```
