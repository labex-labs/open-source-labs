# 定义索引定位器

索引定位器是一种在索引尺度上以固定间隔放置刻度的定位器。我们可以使用 `ticker.IndexLocator()` 来定义索引定位器。

```python
setup(axs[4], title="IndexLocator(base=0.5, offset=0.25)")
axs[4].plot([0]*5, color='white')
axs[4].xaxis.set_major_locator(ticker.IndexLocator(base=0.5, offset=0.25))
```
