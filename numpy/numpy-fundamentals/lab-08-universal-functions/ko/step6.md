# Ufunc 동작 재정의 (Overriding Ufunc Behavior)

ndarray 서브클래스를 포함한 클래스는 특정 특수 메서드를 정의하여 ufunc 이 해당 클래스에 대해 어떻게 작동하는지를 재정의할 수 있습니다. 이를 통해 ufunc 동작을 사용자 정의할 수 있습니다. 예시를 살펴보겠습니다.

```python
import numpy as np

# 사용자 정의 클래스 정의
class MyArray(np.ndarray):
    def __add__(self, other):
        print("Custom add method called")
        return super().__add__(other)

# 사용자 정의 클래스의 인스턴스 생성
arr = MyArray([1, 2, 3])

# 덧셈 수행
result = arr + 1

# 결과 출력
print(result)
```

Output:

```
Custom add method called
[2 3 4]
```
