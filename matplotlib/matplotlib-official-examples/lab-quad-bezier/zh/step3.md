# 创建 PathPatch 对象

既然我们已经有了 `Path` 对象，就可以创建 `PathPatch` 对象了，它将用于在绘图上绘制贝塞尔曲线。我们将把 `facecolor` 设置为 `'none'`，这样就只会绘制曲线而不会填充。

```python
bezier_patch = mpatches.PathPatch(bezier_path, fc="none")
```
