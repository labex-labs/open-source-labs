# 带对数刻度的 pcolor

第三步是创建一个带对数刻度的 pcolor 绘图。当你有取值范围很广的数据时，这很有用。

```python
N = 100
X, Y = np.meshgrid(np.linspace(-3, 3, N), np.linspace(-2, 2, N))

# 一个有尖峰突出的低隆起。
# 需要在对数刻度上设置 z/颜色轴，这样我们就能同时看到隆起和尖峰。
# 线性刻度只会显示尖峰。
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X * 10)**2 - (Y * 10)**2)
Z = Z1 + 50 * Z2

fig, (ax0, ax1) = plt.subplots(2, 1)

c = ax0.pcolor(X, Y, Z, shading='auto',
               norm=LogNorm(vmin=Z.min(), vmax=Z.max()), cmap='PuBu_r')
fig.colorbar(c, ax=ax0)

c = ax1.pcolor(X, Y, Z, cmap='PuBu_r', shading='auto')
fig.colorbar(c, ax=ax1)

plt.show()
```
