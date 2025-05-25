# 원 생성

`make_circle()` 함수를 사용하여 원을 생성합니다. 이 함수는 원의 반지름을 입력으로 받아 원의 x 및 y 좌표를 반환합니다.

```python
def make_circle(r):
    t = np.arange(0, np.pi * 2.0, 0.01)
    t = t.reshape((len(t), 1))
    x = r * np.cos(t)
    y = r * np.sin(t)
    return np.hstack((x, y))
```
