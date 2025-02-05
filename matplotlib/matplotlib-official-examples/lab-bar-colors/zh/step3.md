# 创建柱状图

现在，我们可以使用在步骤 2 中定义的数据来创建柱状图。我们将使用 Matplotlib 的 `pyplot` 模块的 `bar()` 方法来创建图表。我们还将分别传入 `label` 和 `color` 参数来控制图例条目和条形颜色。以下代码演示了如何创建柱状图：

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')
plt.show()
```
