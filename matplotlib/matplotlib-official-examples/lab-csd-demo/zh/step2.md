# 生成信号

我们需要生成两个信号。这些信号包含一个相干部分和一个随机部分。两个信号的相干部分频率均为 10 赫兹。信号的随机部分是通过白噪声生成的，该白噪声经过低通滤波器以创建有色噪声。

```python
dt = 0.01
t = np.arange(0, 30, dt)

# 固定随机状态以确保可重复性
np.random.seed(19680801)

nse1 = np.random.randn(len(t))                 # 白噪声 1
nse2 = np.random.randn(len(t))                 # 白噪声 2
r = np.exp(-t / 0.05)

cnse1 = np.convolve(nse1, r, mode='same') * dt   # 有色噪声 1
cnse2 = np.convolve(nse2, r, mode='same') * dt   # 有色噪声 2

# 两个具有相干部分和随机部分的信号
s1 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse1
s2 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse2
```
