# 创建数据

接下来，我们将创建一些数据用于绘图。在本教程中，我们将创建一个简单的折线图。

```python
# 创建数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 绘制数据
plt.plot(x, y)
plt.show()
```
