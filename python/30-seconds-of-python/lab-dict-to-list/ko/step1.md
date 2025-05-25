# 딕셔너리에서 리스트로 변환

딕셔너리 `d`를 인수로 받아 튜플의 리스트를 반환하는 함수 `dict_to_list(d)`를 작성하십시오. 각 튜플은 딕셔너리에서 키 - 값 쌍을 포함해야 합니다. 리스트의 튜플 순서는 딕셔너리의 키 - 값 쌍 순서와 동일해야 합니다.

```python
def dict_to_list(d):
  return list(d.items())
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
dict_to_list(d)
# [('one', 1), ('three', 3), ('five', 5), ('two', 2), ('four', 4)]
```
