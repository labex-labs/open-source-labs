# 自定义绘图

既然我们已经创建了一个基本的绘图，现在让我们对其进行自定义，使其在视觉上更具吸引力。我们可以添加标题、轴标签，并更改线条的颜色和样式。

```python
# 添加标题和轴标签
plt.title('Sin Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 更改线条的颜色和样式
plt.plot(x, y, color='red', linestyle='dashed')
plt.show()
```
