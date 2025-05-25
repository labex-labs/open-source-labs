# 2D 히스토그램으로 데이터 시각화 - 선형 색상 스케일

이 단계에서는 선형 색상 스케일로 데이터를 시각화합니다.

```python
# 동일한 데이터이지만 선형 색상 스케일 사용
pcm = plt.pcolormesh(xedges, yedges, h.T, cmap=cmap,
                         vmax=1.5e2, rasterized=True)
plt.colorbar(pcm, label="# points", pad=0)
plt.title("2D 히스토그램 및 선형 색상 스케일")
plt.show()
```
