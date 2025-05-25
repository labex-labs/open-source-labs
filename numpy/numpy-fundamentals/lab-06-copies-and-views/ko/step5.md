# 기타 연산

NumPy 에는 뷰 또는 복사본을 생성할 수 있는 다른 연산들이 있습니다.

- `reshape()` 함수는 가능한 경우 뷰를 생성하고, 그렇지 않으면 복사본을 생성합니다. 예를 들어:

```python
import numpy as np

# 배열 생성
x = np.ones((2, 3))

# 배열 전치
y = x.T

# 배열 모양 변경 시도
try:
    y.shape = 6
except AttributeError:
    print("In-place 수정에 호환되지 않는 모양입니다. 원하는 모양의 복사본을 만들려면 `.reshape()` 를 사용하십시오.")
```

위의 예제에서 배열 `y`는 전치 후 비연속적이 되므로, 모양을 변경하려면 복사본이 필요합니다.

- `ravel()` 함수는 가능한 경우 배열의 연속적인 평탄화된 뷰를 반환합니다. 반면에, `flatten()` 메서드는 항상 배열의 평탄화된 복사본을 반환합니다. 예를 들어:

```python
import numpy as np

# 배열 생성
x = np.arange(9).reshape(3, 3)

# 평탄화된 뷰 생성
y = x.ravel()

# 평탄화된 복사본 생성
z = x.flatten()

# 원본 배열 출력
print(x)  # 출력: [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```

위의 예제에서 `y`는 뷰이고, `z`는 복사본입니다.
