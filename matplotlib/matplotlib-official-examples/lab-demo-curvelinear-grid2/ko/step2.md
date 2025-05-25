# 변환 함수 정의

두 번째 단계는 변환 함수를 정의하는 것입니다. 이 예제에서는 x 축 값을 변환하고 y 축 값은 변경하지 않기 위해 `tr` 함수를 사용합니다. `inv_tr` 함수는 변환을 반전시키는 데 사용됩니다.

```python
def tr(x, y):
    return np.sign(x)*abs(x)**.5, y

def inv_tr(x, y):
    return np.sign(x)*x**2, y
```
