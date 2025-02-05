# 创建具有自定义 bin 宽度的直方图

我们可以通过提供一个 bin 边缘列表来创建具有自定义且不等宽 bin 的直方图。在这个例子中，我们将创建一个 bin 间距不均匀的直方图。

```python
bins = [100, 150, 180, 195, 205, 220, 250, 300]
plt.hist(x, bins=bins, density=True, histtype='bar', rwidth=0.8)
plt.show()
```
