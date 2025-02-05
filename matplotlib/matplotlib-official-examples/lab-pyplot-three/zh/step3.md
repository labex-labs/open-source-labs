# 绘制数据

在这一步中，我们将使用 Matplotlib 中的 `plot` 函数在一次调用中绘制所有三个数据集。对于第一个数据集，我们将使用红色虚线；对于第二个数据集，我们将使用蓝色方块；对于第三个数据集，我们将使用绿色三角形。

```python
plt.plot(t, t, 'r--', label='linear')
plt.plot(t, t**2, 'bs', label='quadratic')
plt.plot(t, t**3, 'g^', label='cubic')
plt.legend()
plt.show()
```
