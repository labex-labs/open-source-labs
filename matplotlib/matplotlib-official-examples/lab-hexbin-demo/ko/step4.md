# 로그 색상 스케일 추가

`hexbin()`에서 `bins='log'`를 설정하여 육각형 빈 플롯에 로그 색상 스케일을 추가할 수 있습니다.

```python
fig, ax = plt.subplots(figsize=(9, 4))

hb = ax.hexbin(x, y, gridsize=50, bins='log', cmap='inferno')
ax.set(xlim=xlim, ylim=ylim)
ax.set_title("With a log color scale")

cb = fig.colorbar(hb, ax=ax, label='log10(N)')
```
