# 添加标签和标题

在这一步中，我们将为图表添加一个标题，并为 x 轴和 y 轴添加标签。

```python
plt.plot(t, t, 'r--', label='linear')
plt.plot(t, t**2, 'bs', label='quadratic')
plt.plot(t, t**3, 'g^', label='cubic')
plt.legend()
plt.title("多个数据集")
plt.xlabel("时间 (秒)")
plt.ylabel("值")
plt.show()
```
