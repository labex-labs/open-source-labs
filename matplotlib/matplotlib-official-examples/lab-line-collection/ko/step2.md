# 데이터 생성

다음으로, 선을 플롯하는 데 사용할 데이터를 생성해야 합니다. `numpy`를 사용하여 `x` 및 `y` 값의 2D 배열을 생성합니다.

```python
x = np.arange(100)
ys = x[:50, np.newaxis] + x[np.newaxis, :]
```
