# SymLogNorm

Мы создадим два горба, один отрицательный и один положительный, при этом амплитуда положительного горба в 5 раз больше. Линейно мы не сможем увидеть детали в отрицательном горбе. Мы отдельно применим логарифмический масштаб к положительным и отрицательным данным с использованием `SymLogNorm`.

```python
X, Y = np.mgrid[-3:3:complex(0, N), -2:2:complex(0, N)]
Z = 5 * np.exp(-X**2 - Y**2)

fig, ax = plt.subplots(2, 1)

pcm = ax[0].pcolormesh(X, Y, Z,
                       norm=colors.SymLogNorm(linthresh=0.03, linscale=0.03,
                                              vmin=-1.0, vmax=1.0, base=10),
                       cmap='RdBu_r', shading='nearest')
fig.colorbar(pcm, ax=ax[0], extend='both')

pcm = ax[1].pcolormesh(X, Y, Z, cmap='RdBu_r', vmin=-np.max(Z),
                       shading='nearest')
fig.colorbar(pcm, ax=ax[1], extend='both')
```
