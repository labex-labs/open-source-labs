# 使用 `alpha` 淡化颜色

`alpha` 参数还可用于淡化颜色，以创建更具视觉吸引力的图表。在以下示例中，我们将计算两组随机游走者，它们的步长取自具有不同均值和标准差的正态分布。我们使用填充区域来绘制总体平均位置的正负一个标准差。

```python
# 固定随机状态以确保可重复性
np.random.seed(19680801)

Nsteps, Nwalkers = 100, 250
t = np.arange(Nsteps)

# 一个 (Nsteps x Nwalkers) 的随机游走步长数组
S1 = 0.004 + 0.02*np.random.randn(Nsteps, Nwalkers)
S2 = 0.002 + 0.01*np.random.randn(Nsteps, Nwalkers)

# 一个 (Nsteps x Nwalkers) 的随机游走者位置数组
X1 = S1.cumsum(axis=0)
X2 = S2.cumsum(axis=0)

# 长度为 Nsteps 的数组，分别表示两个总体随时间的经验均值和标准差
mu1 = X1.mean(axis=1)
sigma1 = X1.std(axis=1)
mu2 = X2.mean(axis=1)
sigma2 = X2.std(axis=1)

# 绘制图表！
fig, ax = plt.subplots(1)
ax.plot(t, mu1, lw=2, label='mean population 1')
ax.plot(t, mu2, lw=2, label='mean population 2')
ax.fill_between(t, mu1+sigma1, mu1-sigma1, facecolor='C0', alpha=0.4)
ax.fill_between(t, mu2+sigma2, mu2-sigma2, facecolor='C1', alpha=0.4)
ax.set_title(r'random walkers empirical $\mu$ and $\pm \sigma$ interval')
ax.legend(loc='upper left')
ax.set_xlabel('num steps')
ax.set_ylabel('position')
ax.grid()
```
