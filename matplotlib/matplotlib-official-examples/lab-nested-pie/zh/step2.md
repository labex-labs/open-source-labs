# 使用`ax.pie`创建嵌套饼图

我们可以使用`ax.pie`方法创建一个嵌套饼图。我们将首先生成一些虚假数据，对应于三个组。在内圈中，我们将把每个数字视为属于其自己的组。在外圈中，我们将把它们绘制为其原始三个组的成员。

```python
fig, ax = plt.subplots()

size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

cmap = plt.colormaps["tab20c"]
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])

ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.set(aspect="equal", title='Pie plot with `ax.pie`')
plt.show()
```
