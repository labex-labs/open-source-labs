# 두 리스트가 동일한 내용을 갖는지 확인하기

두 리스트를 인수로 받아 내용이 동일하면 `True`를, 그렇지 않으면 `False`를 반환하는 함수 `have_same_contents(a, b)`를 작성하십시오. 이 함수는 두 리스트가 순서에 관계없이 동일한 요소를 포함하는지 확인해야 합니다.

이 문제를 해결하려면 다음 단계를 따를 수 있습니다.

1. 두 리스트의 조합에 `set()`을 사용하여 고유한 값을 찾습니다.
2. `for` 루프를 사용하여 각 고유 값의 각 리스트에서 `count()`를 비교합니다.
3. 어떤 요소에 대해서든 개수가 일치하지 않으면 `False`를 반환하고, 그렇지 않으면 `True`를 반환합니다.

```python
def have_same_contents(a, b):
  for v in set(a + b):
    if a.count(v) != b.count(v):
      return False
  return True
```

```python
have_same_contents([1, 2, 4], [2, 4, 1]) # True
```
