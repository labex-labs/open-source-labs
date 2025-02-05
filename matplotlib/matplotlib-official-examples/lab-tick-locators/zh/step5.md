# 定义固定定位器

固定定位器是一种在固定位置放置刻度的定位器。我们可以使用 `ticker.FixedLocator()` 来定义固定定位器。

```python
setup(axs[2], title="FixedLocator([0, 1, 5])")
axs[2].xaxis.set_major_locator(ticker.FixedLocator([0, 1, 5]))
axs[2].xaxis.set_minor_locator(ticker.FixedLocator(np.linspace(0.2, 0.8, 4)))
```
