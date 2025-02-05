# 创建散点图

除了折线图，Matplotlib还允许我们创建散点图。散点图对于可视化两个变量之间的关系很有用。

```python
# 创建数据
x = np.random.rand(50)
y = np.random.rand(50)

# 创建散点图
plt.scatter(x, y)

# 添加标题和轴标签
plt.title('Scatter Plot')
plt.xlabel('X轴')
plt.ylabel('Y轴')

plt.show()
```
