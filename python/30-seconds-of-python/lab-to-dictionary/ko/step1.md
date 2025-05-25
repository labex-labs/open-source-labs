# 리스트를 딕셔너리로

`to_dictionary(keys, values)` 함수를 작성하세요. 이 함수는 두 개의 리스트를 입력으로 받아 첫 번째 리스트의 요소를 키로, 두 번째 리스트의 요소를 값으로 하는 딕셔너리를 반환합니다. 이 함수는 두 리스트의 값을 딕셔너리로 결합하기 위해 `zip()`과 `dict()`를 함께 사용해야 합니다. 두 리스트의 길이가 같지 않으면 함수는 `None`을 반환해야 합니다.

```python
def to_dictionary(keys, values):
  return dict(zip(keys, values))
```

```python
to_dictionary(['a', 'b'], [1, 2]) # { a: 1, b: 2 }
```
