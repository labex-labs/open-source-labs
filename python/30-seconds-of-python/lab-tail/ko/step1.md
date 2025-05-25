# 리스트 테일 (List Tail)

`tail(lst)` 함수를 작성하세요. 이 함수는 리스트를 인수로 받아 첫 번째 요소를 제외한 리스트의 모든 요소를 반환합니다. 리스트에 요소가 하나만 있는 경우 전체 리스트를 반환합니다.

```python
def tail(lst):
  return lst[1:] if len(lst) > 1 else lst
```

```python
tail([1, 2, 3]) # [2, 3]
tail([1]) # [1]
```
