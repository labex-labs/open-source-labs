# 배열이 뷰인지 복사본인지 확인하기

`ndarray` 객체의 `base` 속성을 사용하여 배열이 뷰인지 복사본인지 확인할 수 있습니다. `base` 속성은 뷰의 경우 원본 배열을 반환하고, 복사본의 경우 `None`을 반환합니다. 예를 들어:

```python
import numpy as np

# 배열 생성
x = np.arange(9)

# 뷰 생성
y = x.reshape(3, 3)

# 복사본 생성
z = y[[2, 1]]

# y 가 뷰인지 확인
print(y.base)  # 출력: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# z 가 복사본인지 확인
print(z.base is None)  # 출력: True
```

위의 예제에서 `y`는 뷰이고 `z`는 복사본입니다.
