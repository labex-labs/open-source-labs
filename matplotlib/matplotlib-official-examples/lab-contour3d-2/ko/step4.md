# 등고선 플롯 생성

이제 `contour()` 함수를 사용하여 등고선 플롯을 생성합니다. `X`, `Y`, `Z` 데이터를 전달하고, 곡선을 수직으로 '리본' 형태로 확장하기 위해 `extend3d=True`를 설정합니다. 또한 멋진 색상 구성을 위해 색상 맵 (colormap) 을 `cm.coolwarm`으로 설정합니다.

```python
ax.contour(X, Y, Z, extend3d=True, cmap=cm.coolwarm)
```
