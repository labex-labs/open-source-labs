# 기본 산술 연산

기본 ufuncs 는 스칼라에 대해 작동하며, 가장 간단한 예는 덧셈 연산자입니다. 덧셈 연산자를 사용하여 두 배열을 요소별로 더하는 방법을 살펴보겠습니다.

```python
import numpy as np

# 두 배열 생성
arr1 = np.array([0, 2, 3, 4])
arr2 = np.array([1, 1, -1, 2])

# 배열을 요소별로 더하기
result = arr1 + arr2

# 결과 출력
print(result)
```

Output:

```
array([1, 3, 2, 6])
```
