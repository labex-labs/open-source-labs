# 定义 GridHelperCurveLinear

第三步是定义 `GridHelperCurveLinear` 实例。我们将使用第二步中定义的变换函数来变换网格。我们还将把 `grid_locator1` 和 `grid_locator2` 设置为 `MaxNLocator(nbins=6)` 以增加刻度密度。

```python
grid_helper = GridHelperCurveLinear(
    (tr, inv_tr),
    extreme_finder=ExtremeFinderSimple(20, 20),
    grid_locator1=MaxNLocator(nbins=6), grid_locator2=MaxNLocator(nbins=6))
```
