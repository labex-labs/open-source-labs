# 添加带阴影线的多边形补丁

你还可以添加带阴影线的多边形补丁。在这种情况下，我们将使用`add_patch`函数向图表中添加一个多边形补丁。

```python
plt.gca().add_patch(Polygon([(10, 20), (30, 50), (50, 10)], hatch='\\/...', facecolor='g'))
```
