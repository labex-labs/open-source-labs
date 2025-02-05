# 设置变量

接下来，我们将为信号设置变量。我们将使用 0.01 的采样间隔，这将为我们提供 100 Hz 的采样频率。我们将创建一个从 0 到 10 秒、步长为 0.01 秒的时间数组。我们还将使用 NumPy 的 `randn` 函数生成噪声，并将其与指数衰减函数进行卷积以创建一个有噪声的信号。

```python
np.random.seed(0)

dt = 0.01  # 采样间隔
Fs = 1 / dt  # 采样频率
t = np.arange(0, 10, dt)

# 生成噪声：
nse = np.random.randn(len(t))
r = np.exp(-t / 0.05)
cnse = np.convolve(nse, r) * dt
cnse = cnse[:len(t)]

s = 0.1 * np.sin(4 * np.pi * t) + cnse  # 信号
```
