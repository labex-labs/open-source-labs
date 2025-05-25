# 함수 역 합성 (Reverse Compose Functions)

하나 이상의 함수를 인수로 받아 왼쪽에서 오른쪽으로 함수 합성을 수행하는 새로운 함수를 반환하는 함수 `compose_right`를 작성하십시오. 첫 번째 (가장 왼쪽) 함수는 하나 이상의 인수를 허용할 수 있으며, 나머지 함수는 단항 함수여야 합니다.

구현은 `functools` 모듈의 `reduce` 함수를 사용하여 왼쪽에서 오른쪽으로 함수 합성을 수행해야 합니다.

```python
from functools import reduce

def compose_right(*fns):
  # your code here
```

```python
from functools import reduce

def compose_right(*fns):
  return reduce(lambda f, g: lambda *args: g(f(*args)), fns)
```

```python
add = lambda x, y: x + y
square = lambda x: x * x
add_and_square = compose_right(add, square)
add_and_square(1, 2) # 9
```
