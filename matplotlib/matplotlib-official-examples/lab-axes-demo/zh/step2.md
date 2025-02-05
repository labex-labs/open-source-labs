# 生成数据

在这一步中，我们生成一些用于绘图的数据。我们将使用 NumPy 的 `convolve` 函数创建高斯色噪声，并使用 Matplotlib 进行绘制。

```python
np.random.seed(19680801)
dt = 0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000] / 0.05)
x = np.random.randn(len(t))
s = np.convolve(x, r)[:len(x)] * dt

fig, main_ax = plt.subplots()
main_ax.plot(t, s)
```
