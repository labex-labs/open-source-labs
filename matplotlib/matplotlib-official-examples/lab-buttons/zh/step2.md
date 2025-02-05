# 设置初始绘图

接下来，我们将设置初始绘图。我们将使用 `numpy` 的 `arange` 函数创建一个频率为 2 Hz 的正弦波，并使用 `matplotlib.pyplot` 的 `plot` 函数进行绘制。

```python
freqs = np.arange(2, 20, 3)
fig, ax = plt.subplots()
t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2*np.pi*freqs[0]*t)
l, = ax.plot(t, s, lw=2)
```
