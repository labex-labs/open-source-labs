# 리스트 분할 (Bifurcate List)

리스트 `lst`와 필터 `filter`를 입력으로 받아 두 개의 리스트를 반환하는 함수 `bifurcate(lst, filter)`를 작성하십시오. 첫 번째 리스트는 `lst`의 요소 중 필터를 통과하는 요소를 포함하고, 두 번째 리스트는 통과하지 못하는 요소를 포함해야 합니다.

이 함수를 구현하기 위해 리스트 컴프리헨션 (list comprehension) 과 `zip()` 함수를 사용할 수 있습니다. `zip()` 함수는 두 개 이상의 리스트를 입력으로 받아 각 튜플이 각 리스트의 해당 요소를 포함하는 튜플의 리스트를 반환합니다. 예를 들어, `zip([1, 2, 3], [4, 5, 6])`은 `[(1, 4), (2, 5), (3, 6)]`을 반환합니다.

이 함수를 사용하여 `lst`와 `filter`를 동시에 반복하고 필터를 통과하는지 여부에 따라 요소를 적절한 리스트에 추가할 수 있습니다.

```python
def bifurcate(lst, filter):
  return [
    [x for x, flag in zip(lst, filter) if flag],
    [x for x, flag in zip(lst, filter) if not flag]
  ]
```

```python
bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
# [ ['beep', 'boop', 'bar'], ['foo'] ]
```
