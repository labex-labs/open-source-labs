# 定义自动定位器

自动定位器是一种能自动以固定间隔放置刻度的定位器。我们可以使用 `ticker.AutoLocator()` 来定义自动定位器。

```python
setup(axs[5], title="AutoLocator()")
axs[5].xaxis.set_major_locator(ticker.AutoLocator())
axs[5].xaxis.set_minor_locator(ticker.AutoMinorLocator())
```
