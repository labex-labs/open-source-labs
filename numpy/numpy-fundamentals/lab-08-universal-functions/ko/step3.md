# 출력 타입 결정

ufunc 의 출력은 모든 입력 인수가 ndarray 가 아닌 경우 반드시 ndarray 일 필요는 없습니다. 출력 타입은 입력 타입과 타입 캐스팅 규칙에 따라 결정될 수 있습니다. 예시를 살펴보겠습니다.

```python
import numpy as np

# 배열 생성
arr = np.arange(9).reshape(3, 3)

# 곱셈을 수행하고 출력 타입을 지정
result = np.multiply.reduce(arr, dtype=float)

# 결과 출력
print(result)
```

Output:

```
array([ 0., 28., 80.])
```
