# Ufunc 메서드

Ufuncs 는 reduce, accumulate, reduceat, outer 의 네 가지 메서드를 가지고 있습니다. 이러한 메서드는 배열에 대한 연산을 수행하는 데 유용합니다. reduce 메서드를 살펴보겠습니다.

```python
import numpy as np

# 배열 생성
arr = np.arange(9).reshape(3, 3)

# 첫 번째 축을 따라 배열을 reduce
result = np.add.reduce(arr, 1)

# 결과 출력
print(result)
```

Output:

```
array([ 3, 12, 21])
```
