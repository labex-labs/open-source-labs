# 좌표 및 색상 정의

다음으로, 플롯에 대한 좌표와 색상을 정의해야 합니다. 이 예제에서는 `np.indices` 함수를 사용하여 RGB 색상에 대한 17x17x17 값 그리드를 생성합니다.

```python
r, g, b = np.indices((17, 17, 17)) / 16.0
```

또한 그리드의 값 사이의 중간점을 찾기 위해 `midpoints` 함수를 정의합니다. 이 함수는 나중에 구를 생성하는 데 사용됩니다.

```python
def midpoints(x):
    sl = ()
    for _ in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```
