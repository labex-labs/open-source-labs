# 키를 기준으로 딕셔너리 정렬

`sort_dict_by_key(d, reverse=False)` 함수를 작성하세요. 이 함수는 딕셔너리 `d`를 인자로 받아 키를 기준으로 정렬된 새로운 딕셔너리를 반환합니다. 이 함수는 기본값이 `False`인 선택적 매개변수 `reverse`를 가져야 합니다. `reverse`가 `True`이면 딕셔너리는 역순으로 정렬되어야 합니다.

```python
def sort_dict_by_key(d, reverse = False):
  return dict(sorted(d.items(), reverse = reverse))
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_key(d) # {'five': 5, 'four': 4, 'one': 1, 'three': 3, 'two': 2}
sort_dict_by_key(d, True)
# {'two': 2, 'three': 3, 'one': 1, 'four': 4, 'five': 5}
```
