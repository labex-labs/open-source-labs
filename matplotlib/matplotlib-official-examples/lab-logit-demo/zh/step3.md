# 创建具有对数几率尺度和生存符号的图表

我们将创建一个具有对数几率尺度和生存符号的图表。这可以通过将y轴尺度设置为对数几率，并使用 `set_yscale("logit", one_half="1/2", use_overline=True)` 将 `one_half` 参数设置为 `"1/2"` 以及将 `use_overline` 参数设置为 `True` 来实现。我们还将使用 `plot()` 绘制正态分布、拉普拉斯分布和柯西分布的累积分布函数，并使用 `legend()` 添加图例。

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.set_yscale("logit", one_half="1/2", use_overline=True)
axs.set_ylim(1e-5, 1 - 1e-5)
axs.legend()
axs.grid()

plt.show()
```
