# 인덱스별 리스트 정렬

두 개의 리스트를 인수로 받아 두 번째 리스트의 인덱스를 기반으로 정렬된 새로운 리스트를 반환하는 함수 `sort_by_indexes(lst, indexes, reverse=False)`를 작성하십시오. 이 함수는 다음과 같은 매개변수를 가져야 합니다.

- `lst`: 정렬할 요소의 리스트입니다.
- `indexes`: `lst`를 정렬할 원하는 인덱스를 나타내는 정수 리스트입니다.
- `reverse`: `True`로 설정되면 리스트를 역순으로 정렬하는 선택적 부울 매개변수입니다.

이 함수는 두 번째 리스트의 인덱스를 기반으로 정렬된 새로운 리스트를 반환해야 합니다.

```python
def sort_by_indexes(lst, indexes, reverse=False):
  return [val for (_, val) in sorted(zip(indexes, lst), key=lambda x: \
          x[0], reverse=reverse)]
```

```python
a = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
b = [3, 2, 6, 4, 1, 5]
sort_by_indexes(a, b) # ['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']
sort_by_indexes(a, b, True)
# ['oranges', 'milk', 'jam', 'eggs', 'bread', 'apples']
```
