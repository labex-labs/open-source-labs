# 데이터 생성

이 단계에서는 플롯할 데이터를 생성합니다. `squiggle_xy` 함수를 사용하여 서로 다른 주파수를 가진 사인파와 코사인파를 생성합니다.

```python
def squiggle_xy(a, b, c, d):
    i = np.arange(0.0, 2*np.pi, 0.05)
    return np.sin(i*a)*np.cos(i*b), np.sin(i*c)*np.cos(i*d)
```
