# 함수란 무엇인가?

함수는 이름이 지정된 일련의 구문 (statement) 입니다.

```python
def funcname(args):
  statement
  statement
  ...
  return result
```

_어떤_ Python 구문이든 내부에 사용할 수 있습니다.

```python
def foo():
    import math
    print(math.sqrt(2))
    help(math)
```

Python 에는 _특별한_ 구문이 없습니다 (그래서 기억하기 쉽습니다).
