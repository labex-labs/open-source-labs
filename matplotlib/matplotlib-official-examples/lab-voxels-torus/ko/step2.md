# 중간점 함수 정의

다음으로, 좌표 배열의 중간점을 계산하는 `midpoints` 함수를 정의합니다. 이 함수는 나중에 `r`, `theta`, 그리고 `z`의 중간점을 계산하는 데 사용됩니다.

```python
def midpoints(x):
    sl = ()
    for i in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```
