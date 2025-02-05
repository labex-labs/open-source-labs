# 创建绘图

我们将创建绘图并将 `路径补丁(PathPatch)` 添加到绘图中。我们将把绘图的标题设置为 `'一个复合路径'`。

```python
fig, ax = plt.subplots()
ax.add_patch(pathpatch)
ax.set_title('A Compound Path')

ax.autoscale_view()

plt.show()
```
