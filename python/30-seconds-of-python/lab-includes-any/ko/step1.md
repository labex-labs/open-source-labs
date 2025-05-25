# 리스트의 값 중 다른 리스트에 포함된 값이 있는지 확인하기

두 개의 리스트를 인수로 받는 함수 `includes_any(lst, values)`를 작성하십시오. 이 함수는 `values`의 요소 중 `lst`에 포함된 요소가 있는지 확인해야 합니다. 하나의 값이라도 발견되면 함수는 `True`를 반환하고, 그렇지 않으면 `False`를 반환해야 합니다.

이 문제를 해결하기 위해 `for` 루프를 사용하여 `values`의 각 값을 반복할 수 있습니다. 그런 다음 `in` 연산자를 사용하여 해당 값이 `lst`에 포함되어 있는지 확인할 수 있습니다. 값이 발견되면 `True`를 반환합니다. 값이 발견되지 않으면 `False`를 반환합니다.

```python
def includes_any(lst, values):
  for v in values:
    if v in lst:
      return True
  return False
```

```python
includes_any([1, 2, 3, 4], [2, 9]) # True
includes_any([1, 2, 3, 4], [8, 9]) # False
```
