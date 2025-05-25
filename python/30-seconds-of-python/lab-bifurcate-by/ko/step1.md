# 함수 기반 리스트 분할 (Bifurcate List Based on Function)

`bifurcate_by(lst, fn)` 함수를 작성하세요. 이 함수는 리스트 `lst`와 필터링 함수 `fn`을 인수로 받습니다. 이 함수는 필터링 함수의 결과에 따라 리스트를 두 그룹으로 분할해야 합니다. 필터링 함수가 요소에 대해 truthy 값을 반환하면 첫 번째 그룹에 추가해야 합니다. 그렇지 않으면 두 번째 그룹에 추가해야 합니다.

함수는 두 개의 리스트로 구성된 리스트를 반환해야 합니다. 여기서 첫 번째 리스트는 필터링 함수가 truthy 값을 반환한 모든 요소를 포함하고, 두 번째 리스트는 필터링 함수가 falsy 값을 반환한 모든 요소를 포함합니다.

각 요소에 대한 `fn`에서 반환된 값을 기반으로 요소를 그룹에 추가하기 위해 리스트 컴프리헨션 (list comprehension) 을 사용하세요.

```python
def bifurcate_by(lst, fn):
  return [
    [x for x in lst if fn(x)],
    [x for x in lst if not fn(x)]
  ]
```

```python
bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b')
# [ ['beep', 'boop', 'bar'], ['foo'] ]
```
