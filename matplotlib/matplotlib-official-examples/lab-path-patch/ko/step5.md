# 제어점 및 연결선 플롯

이 단계에서는 axes 객체의 `plot` 메서드를 사용하여 경로의 제어점 (control points) 과 연결선을 플롯합니다.

```python
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')
```
