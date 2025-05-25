# 타입 캐스팅 규칙 (Type Casting Rules)

타입 캐스팅은 제공된 입력 타입에 대한 핵심 루프 구현이 없을 때 ufunc 의 입력에 대해 수행됩니다. 캐스팅 규칙은 데이터 타입이 다른 데이터 타입으로 안전하게 캐스팅될 수 있는 시점을 결정합니다. 예시를 살펴보겠습니다.

```python
import numpy as np

# int 가 float 로 안전하게 캐스팅될 수 있는지 확인
result = np.can_cast(np.int, np.float)

# 결과 출력
print(result)
```

Output:

```
True
```
