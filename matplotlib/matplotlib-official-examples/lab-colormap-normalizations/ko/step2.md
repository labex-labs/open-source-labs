# PowerNorm

X 에서 멱법칙 (power-law) 추세를 생성하여 Y 에서 정류된 사인파 (sine wave) 의 일부를 가립니다. 그런 다음 `PowerNorm`을 사용하여 멱법칙을 제거합니다.

```python
X, Y = np.mgrid[0:3:complex(0, N), 0:2:complex(0, N)]
Z1 = (1 + np.sin(Y * 10.)) * X**2

fig, ax = plt.subplots(2, 1)

pcm = ax[0].pcolormesh(X, Y, Z1, norm=colors.PowerNorm(gamma=1. / 2.),
                       cmap='PuBu_r', shading='nearest')
fig.colorbar(pcm, ax=ax[0], extend='max')

pcm = ax[1].pcolormesh(X, Y, Z1, cmap='PuBu_r', shading='nearest')
fig.colorbar(pcm, ax=ax[1], extend='max')
```
