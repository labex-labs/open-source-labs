# 구조화 배열 생성

구조화 배열을 생성하려면 `np.array` 함수를 사용하고 `dtype` 매개변수를 사용하여 데이터 유형을 지정할 수 있습니다. 데이터 유형은 튜플 목록이어야 하며, 각 튜플은 구조화 배열의 필드를 나타냅니다. 각 튜플에는 필드 이름과 필드의 데이터 유형이 포함되어야 합니다.

```python
import numpy as np

# Create a structured array
x = np.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
```
