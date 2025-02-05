# 创建柱状图

另一种常见的图表类型是柱状图。柱状图对于比较不同类别的值很有用。

```python
# 创建数据
x = ['A', 'B', 'C', 'D', 'E']
y = [3, 7, 1, 9, 4]

# 创建柱状图
plt.bar(x, y)

# 添加标题和轴标签
plt.title('柱状图')
plt.xlabel('类别')
plt.ylabel('值')

plt.show()
```
