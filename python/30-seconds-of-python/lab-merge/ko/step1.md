# 리스트 병합

`merge(*args, fill_value=None)`이라는 함수를 작성하세요. 이 함수는 두 개 이상의 리스트를 인수로 받아 리스트의 리스트를 반환합니다. 이 함수는 입력 리스트의 각 요소들을 위치를 기반으로 결합해야 합니다. 리스트가 가장 긴 리스트보다 짧은 경우, 함수는 나머지 항목에 대해 `fill_value`를 사용해야 합니다. `fill_value`가 제공되지 않으면 기본값은 `None`이어야 합니다.

`merge()` 함수를 구현하는 것이 당신의 과제입니다.

```python
def merge(*args, fill_value = None):
  max_length = max([len(lst) for lst in args])
  result = []
  for i in range(max_length):
    result.append([
      args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
    ])
  return result
```

```python
merge(['a', 'b'], [1, 2], [True, False]) # [['a', 1, True], ['b', 2, False]]
merge(['a'], [1, 2], [True, False]) # [['a', 1, True], [None, 2, False]]
merge(['a'], [1, 2], [True, False], fill_value = '_')
# [['a', 1, True], ['_', 2, False]]
```
