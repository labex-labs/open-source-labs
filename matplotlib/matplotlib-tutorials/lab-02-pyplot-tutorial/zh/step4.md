# 使用分类变量绘图

Matplotlib 允许你使用分类变量创建图表。让我们使用分类变量创建一个条形图、散点图和折线图：

```python
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)

plt.suptitle('Categorical Plotting')
plt.show()
```

解释：

- 我们创建了一个包含三个分类值的列表 `names` 和一个表示其对应值的列表 `values`。
- 调用 `figure` 函数创建一个指定大小的新图形。
- 我们使用 `subplot` 函数创建一个子图网格。在这个例子中，我们创建了三个子图，每个子图都有不同类型的图：条形图、散点图和折线图。
- `suptitle` 函数用于设置图形的总标题。
