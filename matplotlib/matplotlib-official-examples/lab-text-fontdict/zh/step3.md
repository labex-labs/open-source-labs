# 创建绘图

现在，我们可以创建我们的绘图了。我们将使用NumPy生成一些数据，并绘制一条阻尼指数衰减曲线。

```python
x = np.linspace(0.0, 5.0, 100)
y = np.cos(2*np.pi*x) * np.exp(-x)

plt.plot(x, y, 'k')
```
