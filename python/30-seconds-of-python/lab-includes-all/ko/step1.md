# 리스트가 모든 값을 포함하는지 확인하기

`includes_all(lst, values)`라는 함수를 작성하세요. 이 함수는 두 개의 리스트를 매개변수로 받습니다. 이 함수는 `values` 리스트의 모든 값이 `lst` 리스트에 포함되어 있는지 확인해야 합니다. 모든 값이 포함되어 있다면 함수는 `True`를 반환해야 합니다. 어떤 값이라도 포함되어 있지 않다면 함수는 `False`를 반환해야 합니다.

이 문제를 해결하려면 다음을 수행해야 합니다.

1. `for` 루프를 사용하여 `values` 리스트의 각 값을 반복합니다.
2. `in` 연산자를 사용하여 현재 값이 `lst` 리스트에 포함되어 있는지 확인합니다.
3. 값이 포함되어 있지 않다면 `False`를 반환합니다.
4. 모든 값이 포함되어 있다면 `True`를 반환합니다.

```python
def includes_all(lst, values):
  for v in values:
    if v not in lst:
      return False
  return True
```

```python
includes_all([1, 2, 3, 4], [1, 4]) # True
includes_all([1, 2, 3, 4], [1, 5]) # False
```
