# 수평 컬러바가 있는 플롯 생성

이제 수평 컬러바가 있는 플롯을 생성합니다. 2 단계와 동일한 단계를 따르지만, 이번에는 `afmhot` 컬러맵을 사용하고 컬러바의 방향을 수평으로 설정합니다.

```python
# Make plot with horizontal colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.afmhot)
ax.set_title('Gaussian noise with horizontal colorbar')

cbar = fig.colorbar(cax, ticks=[-1, 0, 1], orientation='horizontal')
cbar.ax.set_xticklabels(['Low', 'Medium', 'High'])  # horizontal colorbar
```
