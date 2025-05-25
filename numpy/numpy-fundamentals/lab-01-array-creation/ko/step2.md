# 내장 NumPy 배열 생성 함수 사용하기

NumPy 는 배열을 생성하기 위한 내장 함수를 제공합니다. 다음은 몇 가지 예입니다.

```python
import numpy as np

# 규칙적으로 증가하는 값으로 1D 배열 생성
arr1D = np.arange(10)

# 특정 데이터 유형으로 1D 배열 생성
arr1D_float = np.arange(2, 10, dtype=float)

# 지정된 수의 요소로 1D 배열 생성
arr1D_linspace = np.linspace(1., 4., 6)

# 2D 단위 행렬 생성
identity_matrix = np.eye(3)

# 대각선을 따라 주어진 값으로 2D 배열 생성
diag_matrix = np.diag([1, 2, 3])

# Vandermonde 행렬 생성
vander_matrix = np.vander([1, 2, 3, 4], 2)

# 0 으로 채워진 배열 생성
zeros_array = np.zeros((2, 3))

# 1 로 채워진 배열 생성
ones_array = np.ones((2, 3))

# 임의의 값으로 채워진 배열 생성
random_array = np.random.default_rng(42).random((2, 3))
```
