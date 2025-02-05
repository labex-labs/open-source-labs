# 定义多重定位器

多重定位器是一种以固定间隔放置刻度的定位器。我们可以使用 `ticker.MultipleLocator()` 来定义多重定位器。

```python
setup(axs[1], title="MultipleLocator(0.5, offset=0.2)")
axs[1].xaxis.set_major_locator(ticker.MultipleLocator(0.5, offset=0.2))
axs[1].xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
```
