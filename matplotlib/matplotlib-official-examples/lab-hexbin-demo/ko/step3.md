# 육각형 빈 플롯 생성

`matplotlib.pyplot.hexbin()`을 사용하여 육각형 빈 플롯을 생성합니다.

```python
fig, ax = plt.subplots(figsize=(9, 4))

hb = ax.hexbin(x, y, gridsize=50, cmap='inferno')
ax.set(xlim=xlim, ylim=ylim)
ax.set_title("Hexagon binning")

cb = fig.colorbar(hb, ax=ax, label='counts')
```

여기서 그리드 크기를 50 으로 설정하고 컬러 맵을 'inferno'로 설정합니다. 또한 각 육각형 내의 데이터 포인트 수를 표시하기 위해 컬러 바를 추가합니다.
