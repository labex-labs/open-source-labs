# 정점 및 면 색상 계산

Matplotlib 의 `vectorize` 및 `colormaps` 함수를 사용하여 정점 (vertices) 및 면 색상 (facecolors) 을 계산합니다.

```python
# verts[i] 는 다각형 i 를 정의하는 (x, y) 쌍의 목록입니다.
gamma = np.vectorize(math.gamma)
verts = [polygon_under_graph(x, l**x * np.exp(-l) / gamma(x + 1))
         for l in lambdas]
facecolors = plt.colormaps['viridis_r'](np.linspace(0, 1, len(verts)))
```
