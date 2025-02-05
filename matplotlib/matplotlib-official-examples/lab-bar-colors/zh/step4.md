# 自定义图表

我们可以通过添加轴标签和标题来进一步自定义图表。我们还可以更改轴标签和图例标题的颜色。以下代码演示了如何自定义图表：

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply', color='blue')
ax.set_xlabel('fruit names', color='blue')
ax.set_title('Fruit supply by kind and color', color='purple')
ax.legend(title='Fruit color', title_color='red', labelcolor='green')
plt.show()
```
