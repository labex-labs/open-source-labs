# 创建PathPatch对象

在这一步中，我们使用上一步创建的路径对象创建一个 `PathPatch` 对象。这个对象用于填充路径所包围的区域。我们还可以设置补丁的颜色和透明度。

```python
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
```
