# 제너레이터 (Generators)

제너레이터는 반복을 정의하는 함수입니다.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

예를 들어:

```python
>>> for x in countdown(10):
...   print(x, end=' ')
...
10 9 8 7 6 5 4 3 2 1
>>>
```

제너레이터는 `yield` 문을 사용하는 모든 함수입니다.

제너레이터의 동작은 일반 함수와 다릅니다. 제너레이터 함수를 호출하면 제너레이터 객체가 생성됩니다. 함수를 즉시 실행하지 않습니다.

```python
def countdown(n):
    # Added a print statement
    print('Counting down from', n)
    while n > 0:
        yield n
        n -= 1
```

```python
>>> x = countdown(10)
# There is NO PRINT STATEMENT
>>> x
# x is a generator object
<generator object at 0x58490>
>>>
```

함수는 `__next__()` 호출 시에만 실행됩니다.

```python
>>> x = countdown(10)
>>> x
<generator object at 0x58490>
>>> x.__next__()
Counting down from 10
10
>>>
```

`yield`는 값을 생성하지만 함수 실행을 일시 중단합니다. 함수는 `__next__()`에 대한 다음 호출에서 재개됩니다.

```python
>>> x.__next__()
9
>>> x.__next__()
8
```

제너레이터가 최종적으로 반환되면 반복은 오류를 발생시킵니다.

```python
>>> x.__next__()
1
>>> x.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in ? StopIteration
>>>
```

_관찰: 제너레이터 함수는 for 문이 리스트, 튜플, 딕셔너리, 파일 등에서 사용하는 것과 동일한 하위 수준 프로토콜을 구현합니다._
