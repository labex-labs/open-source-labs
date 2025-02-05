# 创建次 y 轴

我们将创建第三个示例，展示如何在一种基于数据的临时变换中关联坐标轴，这种变换是通过经验推导得出的。在这种情况下，我们将正向和反向变换函数设置为从一个数据集到另一个数据集的线性插值。

```python
fig, ax = plt.subplots(layout='constrained')
xdata = np.arange(1, 11, 0.4)
ydata = np.random.randn(len(xdata))
ax.plot(xdata, ydata, label='Plotted data')

xold = np.arange(0, 11, 0.2)
# 一个将 x 坐标与另一个由数据导出的坐标相关联的虚拟数据集。
# xnew 必须是单调的，所以我们进行排序...
xnew = np.sort(10 * np.exp(-xold / 4) + np.random.randn(len(xold)) / 3)

ax.plot(xold[3:], xnew[3:], label='Transform data')
ax.set_xlabel('X [m]')
ax.legend()

def forward(x):
    return np.interp(x, xold, xnew)

def inverse(x):
    return np.interp(x, xnew, xold)

secax = ax.secondary_xaxis('top', functions=(forward, inverse))
secax.xaxis.set_minor_locator(AutoMinorLocator())
secax.set_xlabel('$X_{other}$')
```
