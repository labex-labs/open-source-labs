# 다각형 생성

`Polygon()`을 사용하여 다각형을 생성하고 패치 (patches) 목록에 추가합니다.

```python
for i in range(N):
    polygon = Polygon(np.random.rand(N, 2), closed=True)
    patches.append(polygon)
```
