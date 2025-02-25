# 対数正規分布

上部から突き出たスパイク付きの低い盛り上がりを作成します。この盛り上がりとスパイクの両方を見るために、z/色軸を対数スケールにする必要があります。

```python
N = 100
X, Y = np.mgrid[-3:3:complex(0, N), -2:2:complex(0, N)]

Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X * 10)**2 - (Y * 10)**2)
Z = Z1 + 50 * Z2

fig, ax = plt.subplots(2, 1)

pcm = ax[0].pcolor(X, Y, Z,
                   norm=colors.LogNorm(vmin=Z.min(), vmax=Z.max()),
                   cmap='PuBu_r', shading='nearest')
fig.colorbar(pcm, ax=ax[0], extend='max')

pcm = ax[1].pcolor(X, Y, Z, cmap='PuBu_r', shading='nearest')
fig.colorbar(pcm, ax=ax[1], extend='max')
```
