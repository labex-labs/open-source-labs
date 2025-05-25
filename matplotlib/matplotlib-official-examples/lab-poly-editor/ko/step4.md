# 다각형 생성

`Polygon` 클래스를 사용하여 편집할 다각형을 생성해야 합니다.

```python
theta = np.arange(0, 2*np.pi, 0.1)
r = 1.5

xs = r * np.cos(theta)
ys = r * np.sin(theta)

poly = Polygon(np.column_stack([xs, ys]), animated=True)
```
