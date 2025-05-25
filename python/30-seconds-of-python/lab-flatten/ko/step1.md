# 리스트 평탄화 (Flatten a List)

`flatten(lst)`라는 Python 함수를 작성하세요. 이 함수는 리스트의 리스트를 인수로 받아 평탄화된 리스트를 반환합니다. 이 함수는 리스트를 한 번만 평탄화해야 합니다. 즉, 원래 리스트 내의 중첩 리스트는 평탄화되지만, 해당 중첩 리스트 내의 중첩 리스트는 그대로 유지되어야 합니다.

이 문제를 해결하기 위해 리스트 컴프리헨션 (list comprehension) 을 사용하여 하위 리스트에서 각 값을 순서대로 추출할 수 있습니다.

```python
def flatten(lst):
  return [x for y in lst for x in y]
```

```python
flatten([[1, 2, 3, 4], [5, 6, 7, 8]]) # [1, 2, 3, 4, 5, 6, 7, 8]
```
