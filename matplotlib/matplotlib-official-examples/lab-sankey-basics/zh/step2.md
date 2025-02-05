# 创建一个简单的桑基图

我们将从创建一个简单的桑基图开始，展示如何使用 `Sankey` 类。

```python
Sankey(flows=[0.25, 0.15, 0.60, -0.20, -0.15, -0.05, -0.50, -0.10],
       labels=['', '', '', 'First', 'Second', 'Third', 'Fourth', 'Fifth'],
       orientations=[-1, 1, 0, 1, 1, 1, 0, -1]).finish()
plt.title("The default settings produce a diagram like this.")
```

这段代码将使用默认设置生成一个桑基图，其中包括流的标签和方向。生成的图表将显示标题 “The default settings produce a diagram like this.”。
