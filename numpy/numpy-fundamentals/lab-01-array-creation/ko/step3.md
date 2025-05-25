# 기존 배열 복제, 결합 또는 변형하기

배열을 생성한 후에는 이를 복제, 결합 또는 변형하여 새로운 배열을 생성할 수 있습니다. 배열 또는 해당 요소를 새 변수에 할당할 때는 원본 배열의 뷰 (view) 대신 새 배열을 생성하기 위해 `np.copy` 함수를 사용하십시오. 다음은 예시입니다.

```python
import numpy as np

# 배열 생성
a = np.array([1, 2, 3, 4])

# 배열의 처음 두 요소의 뷰 생성
b = a[:2]

# 뷰 수정
b += 1

# 원본 배열과 수정된 뷰 출력
print('a =', a, '; b =', b)
```

배열을 결합하려면 `np.vstack`, `np.hstack`, `np.block`과 같은 함수를 사용할 수 있습니다. 다음은 `np.block`을 사용하여 네 개의 2x2 배열을 4x4 배열로 결합하는 예시입니다.

```python
import numpy as np

A = np.ones((2, 2))
B = np.eye(2)
C = np.zeros((2, 2))
D = np.diag((-3, -4))

result = np.block([[A, B], [C, D]])
```
