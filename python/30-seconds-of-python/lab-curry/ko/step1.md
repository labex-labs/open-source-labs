# 커리 함수 (Curry Function)

주어진 함수 `fn`을 커리하는 함수 `curry(fn, *args)`를 작성하십시오. 이 함수는 주어진 인수 `args`가 부분적으로 적용된 `fn`처럼 동작하는 새로운 함수를 반환해야 합니다.

```python
from functools import partial

def curry(fn, *args):
  return partial(fn, *args)
```

```python
add = lambda x, y: x + y
add10 = curry(add, 10)
add10(20) # 30
```
