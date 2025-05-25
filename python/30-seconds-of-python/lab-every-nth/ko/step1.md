# 리스트의 모든 n 번째 요소

리스트 `lst`와 정수 `nth`를 인수로 받아 원래 리스트의 모든 `nth` 요소를 포함하는 새로운 리스트를 반환하는 함수 `every_nth(lst, nth)`를 작성하십시오.

```python
def every_nth(lst, nth):
  return lst[nth - 1::nth]
```

```python
every_nth([1, 2, 3, 4, 5, 6], 2) # [ 2, 4, 6 ]
```
