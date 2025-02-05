# 添加第一个图表

我们使用 `sankey.add()` 并传入 `flows=[1, -1]` 和 `orientations=[0, 1]` 来添加第一个图表。

```python
sankey.add(flows=[1, -1], orientations=[0, 1],
           patchlabel="0", facecolor='k',
           rotation=45)
```
