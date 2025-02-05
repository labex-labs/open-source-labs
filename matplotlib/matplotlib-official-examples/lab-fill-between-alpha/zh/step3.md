# 使用 `where` 突出显示特定区域

`where` 关键字参数对于突出显示图表的特定区域非常方便。`where` 接受一个与 x、ymin 和 ymax 参数长度相同的布尔掩码，并且只填充布尔掩码为 `True` 的区域。在下面的示例中，我们模拟了一个随机游走者，并计算了总体位置的解析均值和标准差。总体均值显示为虚线，均值的正负一个标准差偏差显示为填充区域。我们使用 `where` 掩码 `X > upper_bound` 来找到游走者超出一个标准差边界的区域，并将该区域涂成红色。

```python
# 固定随机状态以确保可重复性
np.random.seed(1)

Nsteps = 500
t = np.arange(Nsteps)

mu = 0.002
sigma = 0.01

# 步长和位置
S = mu + sigma*np.random.randn(Nsteps)
X = S.cumsum()

# 解析的总体一个标准差上下界
lower_bound = mu*t - sigma*np.sqrt(t)
upper_bound = mu*t + sigma*np.sqrt(t)

fig, ax = plt.subplots(1)
ax.plot(t, X, lw=2, label='walker position')
ax.plot(t, mu*t, lw=1, label='population mean', color='C0', ls='--')
ax.fill_between(t, lower_bound, upper_bound, facecolor='C0', alpha=0.4,
                label='1 sigma range')
ax.legend(loc='upper left')

# 在这里，我们使用 where 参数只填充游走者高于总体一个标准差边界的区域
ax.fill_between(t, upper_bound, X, where=X > upper_bound, fc='red', alpha=0.4)
ax.fill_between(t, lower_bound, X, where=X < lower_bound, fc='red', alpha=0.4)
ax.set_xlabel('num steps')
ax.set_ylabel('position')
ax.grid()
```
