# 리스트에서 중복 항목 확인하기

`has_duplicates(lst)`라는 Python 함수를 작성하세요. 이 함수는 리스트를 인수로 받아 리스트에 중복 항목이 있으면 `True`를 반환하고, 그렇지 않으면 `False`를 반환합니다.

이 문제를 해결하기 위해 다음 단계를 사용할 수 있습니다.

1. `set()` 함수를 사용하여 리스트에서 중복 항목을 제거합니다.
2. 원래 리스트의 길이와 세트의 길이를 비교합니다. 길이가 같으면 중복 항목이 없는 것입니다. 길이가 다르면 중복 항목이 있는 것입니다.

```python
def has_duplicates(lst):
  return len(lst) != len(set(lst))
```

```python
x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
has_duplicates(x) # True
has_duplicates(y) # False
```
