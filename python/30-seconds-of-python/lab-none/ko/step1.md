# 모든 리스트 요소가 falsy 인지 테스트

`lst` 리스트와 선택적 함수 `fn`을 인수로 사용하는 Python 함수 `none(lst, fn = lambda x: x)`를 작성하십시오. 이 함수는 리스트의 모든 요소가 falsy 이면 `True`를 반환하고, 그렇지 않으면 `False`를 반환해야 합니다. 선택적 함수 `fn`이 제공되면 리스트의 각 요소의 truthiness 를 결정하는 데 사용해야 합니다.

요소가 falsy 인지 확인하려면 Python 의 `bool()` 함수와 동일한 규칙을 사용할 수 있습니다. 일반적으로 다음 값은 falsy 로 간주됩니다.

- `False`
- `None`
- `0` (정수)
- `0.0` (부동 소수점)
- `''` (빈 문자열)
- `[]` (빈 리스트)
- `{}` (빈 딕셔너리)
- `()` (빈 튜플)
- `set()` (빈 집합)

선택적 함수 `fn`이 제공되면 하나의 인수를 취하고 부울 값을 반환해야 합니다. 이 함수는 리스트의 각 요소에 대해 호출되며, 반환 값은 요소의 truthiness 를 결정하는 데 사용됩니다.

```python
def none(lst, fn = lambda x: x):
  return all(not fn(x) for x in lst)
```

```python
none([0, 1, 2, 0], lambda x: x >= 2 ) # False
none([0, 0, 0]) # True
```
