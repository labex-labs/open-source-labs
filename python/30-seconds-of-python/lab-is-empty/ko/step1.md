# 컬렉션이 비어 있는지 확인

`is_empty(val)`이라는 Python 함수를 작성하세요. 이 함수는 값을 매개변수로 받아, 값이 빈 시퀀스 또는 컬렉션인 경우 `True`를 반환하고, 그렇지 않은 경우 `False`를 반환합니다.

시퀀스 또는 컬렉션이 비어 있는지 확인하려면 `not` 연산자를 사용하여 제공된 시퀀스 또는 컬렉션의 진리값을 테스트할 수 있습니다. 시퀀스 또는 컬렉션이 비어 있으면 `not` 연산자는 `True`를 반환합니다.

작성하는 함수는 다음 유형의 시퀀스 및 컬렉션을 처리할 수 있어야 합니다.

- 리스트 (Lists)
- 튜플 (Tuples)
- 세트 (Sets)
- 딕셔너리 (Dictionaries)
- 문자열 (Strings)
- 범위 (Ranges)

```python
def is_empty(val):
  return not val
```

```python
is_empty([]) # True
is_empty({}) # True
is_empty('') # True
is_empty(set()) # True
is_empty(range(0)) # True
is_empty([1, 2]) # False
is_empty({ 'a': 1, 'b': 2 }) # False
is_empty('text') # False
is_empty(set([1, 2])) # False
is_empty(range(2)) # False
```
