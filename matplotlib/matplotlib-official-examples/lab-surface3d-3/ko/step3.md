# 표면 플롯을 위한 색상 생성

이 단계에서는 표면 플롯을 위한 색상을 생성합니다. 메쉬 그리드와 동일한 모양의 문자열 빈 배열을 생성하고, 체커보드 패턴으로 두 가지 색상을 채웁니다.

```python
# Create colors for the surface plot
colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(ylen):
    for x in range(xlen):
        colors[y, x] = colortuple[(x + y) % len(colortuple)]
```
