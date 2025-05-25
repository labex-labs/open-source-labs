# 함수 합성 (Compose Functions)

`compose(*fns)`라는 함수를 작성하십시오. 이 함수는 하나 이상의 함수를 인수로 받아들이고, 입력 함수들을 오른쪽에서 왼쪽으로 합성한 결과인 새로운 함수를 반환합니다. 마지막 (가장 오른쪽에 있는) 함수는 하나 이상의 인수를 받아들일 수 있으며, 나머지 함수들은 단항 함수여야 합니다.

```python
from functools import reduce

def compose(*fns):
  return reduce(lambda f, g: lambda *args: f(g(*args)), fns)
```

```python
add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)
multiply_and_add_5(5, 2) # 15
```
