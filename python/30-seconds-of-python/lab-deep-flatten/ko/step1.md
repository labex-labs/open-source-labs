# 깊이 평탄화 리스트

`deep_flatten(lst)` 함수를 작성하세요. 이 함수는 리스트 `lst`를 인수로 받아 `lst`의 깊이 평탄화된 버전을 반환합니다. 이 함수는 재귀 (recursion) 를 사용하고, 요소가 반복 가능한지 확인하기 위해 `collections.abc.Iterable`과 함께 `isinstance()` 함수를 사용해야 합니다. 요소가 반복 가능하다면, 함수는 해당 요소에 `deep_flatten()`을 재귀적으로 적용해야 합니다. 그렇지 않으면, 함수는 해당 요소만 포함하는 리스트를 반환해야 합니다.

```python
from collections.abc import Iterable

def deep_flatten(lst):
  return ([a for i in lst for a in
          deep_flatten(i)] if isinstance(lst, Iterable) else [lst])
```

```python
deep_flatten([1, [2], [[3], 4], 5]) # [1, 2, 3, 4, 5]
```
