# 구멍이 있는 채워진 등고선 생성

`Path` 클래스에 설명된 대로, 여러 개의 채워진 등고선은 다각형 정점의 단일 목록과 정점 종류 (코드 유형) 의 목록과 함께 지정할 수 있습니다. 이는 특히 구멍이 있는 다각형에 유용합니다.

```python
fig, ax = plt.subplots()
filled01 = [[[0, 0], [3, 0], [3, 3], [0, 3], [1, 1], [1, 2], [2, 2], [2, 1]]]
M = Path.MOVETO
L = Path.LINETO
kinds01 = [[M, L, L, L, M, L, L, L]]
cs = ContourSet(ax, [0, 1], [filled01], [kinds01], filled=True)
cbar = fig.colorbar(cs)

ax.set(xlim=(-0.5, 3.5), ylim=(-0.5, 3.5),
       title='User specified filled contours with holes')
```
