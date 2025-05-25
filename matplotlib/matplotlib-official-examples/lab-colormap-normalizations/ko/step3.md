# SymLogNorm

우리는 두 개의 험프 (hump) 를 생성할 것입니다. 하나는 음수이고 다른 하나는 양수이며, 양수 험프는 5 배의 진폭을 갖습니다. 선형적으로는 음수 험프의 세부 사항을 볼 수 없습니다. `SymLogNorm`을 사용하여 양수 및 음수 데이터를 개별적으로 로그 스케일링 (logarithmically scale) 합니다.

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
