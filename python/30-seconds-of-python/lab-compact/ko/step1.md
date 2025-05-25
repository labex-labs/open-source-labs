# Compact List (압축된 리스트)

`compact(lst)` 함수를 작성하세요. 이 함수는 리스트를 인수로 받아 모든 falsy 값을 제거한 새로운 리스트를 반환합니다. Falsy 값에는 `False`, `None`, `0`, 그리고 `""`가 포함됩니다.

이 문제를 해결하기 위해 `filter()` 함수를 사용하여 리스트에서 falsy 값을 필터링할 수 있습니다.

```python
def compact(lst):
  return list(filter(None, lst))
```

```python
compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]
```
