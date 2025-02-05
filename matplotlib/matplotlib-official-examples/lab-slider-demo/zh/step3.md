# 创建初始图表

现在，我们将创建正弦波的初始图表。我们将定义幅度和频率的初始参数，并使用这些参数绘制正弦波。

```python
t = np.linspace(0, 1, 1000)
init_amplitude = 5
init_frequency = 3

fig, ax = plt.subplots()
line, = ax.plot(t, f(t, init_amplitude, init_frequency), lw=2)
ax.set_xlabel('Time [s]')
```
