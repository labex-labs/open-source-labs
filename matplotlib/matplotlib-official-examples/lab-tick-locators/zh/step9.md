# 定义最大刻度数定位器

最大刻度数定位器是一种在轴上放置最大数量刻度的定位器。我们可以使用 `ticker.MaxNLocator()` 来定义最大刻度数定位器。

```python
setup(axs[6], title="MaxNLocator(n=4)")
axs[6].xaxis.set_major_locator(ticker.MaxNLocator(4))
axs[6].xaxis.set_minor_locator(ticker.MaxNLocator(40))
```
