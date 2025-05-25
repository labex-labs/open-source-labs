# 경계 정규화 (Boundary Norm) 사용

선분들의 색상을 지정하기 위해 경계 정규화 (boundary norm) 를 사용합니다. 빨간색, 녹색, 파란색의 세 가지 색상을 포함하는 `ListedColormap`을 생성합니다. 그런 다음 경계 -1, -0.5, 0.5, 1 과 `ListedColormap`을 사용하여 `BoundaryNorm`을 생성합니다. `set_array` 함수를 사용하여 colormapping 에 사용되는 값을 설정합니다.

```python
cmap = ListedColormap(['r', 'g', 'b'])
norm = BoundaryNorm([-1, -0.5, 0.5, 1], cmap.N)
lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```
