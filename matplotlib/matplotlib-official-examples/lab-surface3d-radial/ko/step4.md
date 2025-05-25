# 표면 플롯

이 단계에서는 Matplotlib 의 `plot_surface()` 함수를 사용하여 표면을 플롯합니다. 표면의 색상을 설정하기 위해 `YlGnBu_r` 컬러맵 (colormap) 을 사용합니다.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
```
