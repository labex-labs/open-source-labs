# 指定光源和颜色映射表

我们通过设置光源的方位角和高度来指定LightSource对象。我们还设置了绘图中要使用的颜色映射表。

```python
ls = LightSource(azdeg=315, altdeg=45)
cmap = plt.cm.gist_earth
```
