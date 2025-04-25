# 计算互谱密度（CSD）

为了计算两个信号的互谱密度，我们需要使用 Matplotlib 的 csd 函数。该函数将两个信号、快速傅里叶变换（FFT）的点数以及采样频率作为输入。

```python
fig, ax = plt.subplots()
cxy, f = ax.csd(s1, s2, 256, 1. / dt)
ax.set_ylabel('CSD (dB)')
plt.show()
```
