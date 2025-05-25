# 딕셔너리 정렬 (Sort Dictionary)

`sort_dict_by_value(d, reverse=False)`라는 함수를 작성하여 딕셔너리 `d`를 값으로 정렬합니다. 이 함수는 원래 딕셔너리와 동일한 키를 가지지만 값이 오름차순으로 정렬된 새로운 딕셔너리를 반환해야 합니다. `reverse` 매개변수가 `True`로 설정되면 함수는 딕셔너리를 내림차순으로 정렬해야 합니다.

이 문제를 해결하려면 다음 단계를 따를 수 있습니다.

1. `dict.items()`를 사용하여 `d`에서 튜플 쌍의 목록을 가져옵니다.
2. 람다 함수와 `sorted()`를 사용하여 목록을 정렬합니다.
3. `dict()`를 사용하여 정렬된 목록을 다시 딕셔너리로 변환합니다.
4. `sorted()`의 `reverse` 매개변수를 사용하여 두 번째 인수를 기준으로 딕셔너리를 역순으로 정렬합니다.

**⚠️ 주의:** 딕셔너리 값은 동일한 유형이어야 합니다.

```python
def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_value(d) # {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
sort_dict_by_value(d, True)
# {'five': 5, 'four': 4, 'three': 3, 'two': 2, 'one': 1}
```
