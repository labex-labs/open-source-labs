# 定义线性定位器

线性定位器是一种在线性尺度上以固定间隔放置刻度的定位器。我们可以使用 `ticker.LinearLocator()` 来定义线性定位器。

```python
setup(axs[3], title="LinearLocator(numticks=3)")
axs[3].xaxis.set_major_locator(ticker.LinearLocator(3))
axs[3].xaxis.set_minor_locator(ticker.LinearLocator(31))
```
