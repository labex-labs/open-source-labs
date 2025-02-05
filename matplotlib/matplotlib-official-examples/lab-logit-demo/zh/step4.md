# 创建具有线性尺度的图表

我们将创建一个具有线性尺度的图表。这可以通过使用 `plot()` 简单地绘制正态分布、拉普拉斯分布和柯西分布的累积分布函数，并使用 `legend()` 添加图例来实现。

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.legend()
axs.grid()

plt.show()
```
