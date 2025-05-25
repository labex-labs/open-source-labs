# NaN 으로 설정

y > 0.7 인 경우 NaN 으로 설정합니다. NaN 값을 가진 새로운 y 배열을 생성합니다.

```python
y4 = y.copy()
y4[y3 > 0.7] = np.nan
```
