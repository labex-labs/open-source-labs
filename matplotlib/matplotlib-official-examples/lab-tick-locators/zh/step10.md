# 定义对数定位器

对数定位器是一种在对数尺度上以固定间隔放置刻度的定位器。我们可以使用 `ticker.LogLocator()` 来定义对数定位器。

```python
setup(axs[7], title="LogLocator(base=10, numticks=15)")
axs[7].set_xlim(10**3, 10**10)
axs[7].set_xscale('log')
axs[7].xaxis.set_major_locator(ticker.LogLocator(base=10, numticks=15))
```
