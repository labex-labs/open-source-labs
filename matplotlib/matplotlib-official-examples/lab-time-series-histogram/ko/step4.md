# 2D 히스토그램으로 데이터 시각화 - 로그 색상 스케일

이 단계에서는 여러 시계열을 히스토그램으로 변환합니다. 숨겨진 신호가 더 잘 보일 뿐만 아니라 훨씬 더 빠른 절차입니다. (x, y) 점을 로그 색상 스케일로 2D 히스토그램에 플롯합니다.

```python
tic = time.time()

# 각 시계열의 점 사이를 선형 보간합니다.
num_fine = 800
x_fine = np.linspace(x.min(), x.max(), num_fine)
y_fine = np.concatenate([np.interp(x_fine, x, y_row) for y_row in Y])
x_fine = np.broadcast_to(x_fine, (num_series, num_fine)).ravel()

# (x, y) 점을 로그 색상 스케일로 2D 히스토그램에 플롯합니다.
# 노이즈 아래에 어떤 종류의 구조가 있다는 것이 분명합니다.
# vmax 를 조정하여 신호를 더 잘 보이게 할 수 있습니다.
cmap = plt.colormaps["plasma"]
cmap = cmap.with_extremes(bad=cmap(0))
h, xedges, yedges = np.histogram2d(x_fine, y_fine, bins=[400, 100])
pcm = plt.pcolormesh(xedges, yedges, h.T, cmap=cmap,
                         norm="log", vmax=1.5e2, rasterized=True)
plt.colorbar(pcm, label="# points", pad=0)
plt.title("2D 히스토그램 및 로그 색상 스케일")
plt.show()

toc = time.time()
print(f"{toc-tic:.3f} sec. elapsed")
```
