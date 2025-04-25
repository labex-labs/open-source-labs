# 创建图形和子图

接下来，我们创建一个图形，并添加一个使用 `AxesZero` 的子图。这将创建一条带有 x 轴和 y 轴标签的轴线，但没有刻度线或网格。

```python
fig = plt.figure()
fig.subplots_adjust(right=0.85)
ax = fig.add_subplot(axes_class=AxesZero)
```
