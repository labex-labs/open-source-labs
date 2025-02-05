# 定义空刻度定位器

空刻度定位器是一种不在轴上放置任何刻度的定位器。我们可以使用 `ticker.NullLocator()` 来定义空刻度定位器。

```python
setup(axs[0], title="NullLocator()")
axs[0].xaxis.set_major_locator(ticker.NullLocator())
axs[0].xaxis.set_minor_locator(ticker.NullLocator())
```
