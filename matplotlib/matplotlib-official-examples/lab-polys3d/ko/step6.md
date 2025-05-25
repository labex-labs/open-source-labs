# 다각형 생성 및 플롯에 추가

Matplotlib 의 `PolyCollection` 함수를 사용하여 다각형을 생성하고 플롯에 추가합니다.

```python
poly = PolyCollection(verts, facecolors=facecolors, alpha=.7)
ax.add_collection3d(poly, zs=lambdas, zdir='y')
```
