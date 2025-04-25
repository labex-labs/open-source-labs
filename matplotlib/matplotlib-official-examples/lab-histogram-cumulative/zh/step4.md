# 绘制累积分布

在这一步中，我们将绘制累积分布。我们将使用`.ecdf`方法来绘制经验累积分布函数（ECDF）和互补经验累积分布函数。我们还将使用均值为 200、标准差为 25 的正态分布来绘制理论累积分布函数。

```python
# 累积分布
axs[0].ecdf(data, label="CDF")
n, bins, patches = axs[0].hist(data, 25, density=True, histtype="step",
                               cumulative=True, label="累积直方图")
x = np.linspace(data.min(), data.max())
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (x - mu))**2))
y = y.cumsum()
y /= y[-1]
axs[0].plot(x, y, "k--", linewidth=1.5, label="理论")

# 互补累积分布
axs[1].ecdf(data, complementary=True, label="CCDF")
axs[1].hist(data, bins=bins, density=True, histtype="step", cumulative=-1,
            label="反向累积直方图")
axs[1].plot(x, 1 - y, "k--", linewidth=1.5, label="理论")
```
