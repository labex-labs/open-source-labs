# 添加标签和标题

最后，我们可以为箱线图添加标签和标题，使其更具信息性。我们可以为 x 轴和 y 轴添加标签，以及为图表添加标题。我们还可以更改标签和标题的字体大小和样式。以下是添加标签和标题的示例：

```python
plt.boxplot([data1, data2, data3])
plt.xlabel('Group')
plt.ylabel('Value')
plt.title('Comparison of Three Groups')
plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.show()
```
