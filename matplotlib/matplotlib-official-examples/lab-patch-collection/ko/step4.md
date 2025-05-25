# 원 생성

`Circle()`을 사용하여 원을 생성하고 패치 (patches) 목록에 추가합니다.

```python
x = np.random.rand(N)
y = np.random.rand(N)
radii = 0.1*np.random.rand(N)
patches = []
for x1, y1, r in zip(x, y, radii):
    circle = Circle((x1, y1), r)
    patches.append(circle)
```
