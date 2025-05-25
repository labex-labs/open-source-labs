# 브로드캐스팅 (Broadcasting)

브로드캐스팅은 ufunc 의 강력한 기능으로, 서로 다른 형태의 배열에 대한 연산을 수행할 수 있게 해줍니다. 브로드캐스팅 규칙은 서로 다른 형태의 배열이 연산 중에 어떻게 처리되는지를 결정합니다. 예시를 살펴보겠습니다.

```python
import numpy as np

# 두 개의 배열 생성
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1], [2], [3]])

# 배열 곱셈
result = arr1 * arr2

# 결과 출력
print(result)
```

Output:

```
array([[1, 2, 3],
       [2, 4, 6],
       [3, 6, 9]])
```
