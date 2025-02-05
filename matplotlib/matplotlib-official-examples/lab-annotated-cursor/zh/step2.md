# 创建一个绘图

我们使用NumPy的`linspace`函数创建一个简单的抛物线图，为x生成-5到5之间的1000个值，然后将y计算为x的平方。

```python
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Cursor Tracking x Position")

x = np.linspace(-5, 5, 1000)
y = x**2

line, = ax.plot(x, y)
ax.set_xlim(-5, 5)
ax.set_ylim(0, 25)
```
