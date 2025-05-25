# 프로그램의 실패 방식

Python 은 함수 인수의 유형이나 값에 대한 검사 또는 유효성 검사를 수행하지 않습니다. 함수는 함수 내의 문과 호환되는 모든 데이터에서 작동합니다.

```python
def add(x, y):
    return x + y

add(3, 4)               # 7
add('Hello', 'World')   # 'HelloWorld'
add('3', '4')           # '34'
```

함수에 오류가 있는 경우, 런타임에 예외 (exception) 로 나타납니다.

```python
def add(x, y):
    return x + y

>>> add(3, '4')
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +:
'int' and 'str'
>>>
```

코드를 검증하기 위해, 테스팅 (testing) 에 대한 강조가 있습니다 (나중에 다룹니다).
