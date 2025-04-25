# 创建图表

现在，我们可以使用自定义刻度来创建图表了。我们将使用示例数据创建一个柱状图，并将 y 轴刻度设置为使用我们的自定义刻度函数。

```python
# Create a bar chart with sample data
fig, ax = plt.subplots()
money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]
ax.bar(['Bill', 'Fred', 'Mary', 'Sue'], money)

# Set the y-axis ticker to use the custom ticker function
ax.yaxis.set_major_formatter(ticker.FuncFormatter(millions))

# Display the plot
plt.show()
```
