# 创建散点图

除了折线图，Matplotlib 还可以创建散点图。以下是一个示例：

```python
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 500 * np.random.rand(50)

plt.scatter(x, y, c=colors, s=sizes)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.show()
```
