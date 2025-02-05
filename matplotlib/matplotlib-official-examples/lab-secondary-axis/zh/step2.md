# 绘制数据

我们将创建一个简单的正弦波来演示次坐标轴的使用。我们将使用度数作为 x 轴来绘制正弦波。

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0, 360, 1)
y = np.sin(2 * x * np.pi / 180)
ax.plot(x, y)
ax.set_xlabel('angle [degrees]')
ax.set_ylabel('signal')
ax.set_title('Sine wave')
```
