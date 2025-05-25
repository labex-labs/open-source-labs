# 값의 모든 인덱스

`index_of_all(lst, value)`라는 Python 함수를 작성하세요. 이 함수는 리스트 `lst`와 값 `value`를 인수로 받아 `lst`에서 `value`가 나타나는 모든 위치의 인덱스 리스트를 반환합니다.

이 문제를 해결하기 위해 `enumerate()`와 리스트 컴프리헨션 (list comprehension) 을 사용하여 각 요소가 `value`와 같은지 확인하고 `i`를 결과에 추가할 수 있습니다.

```python
def index_of_all(lst, value):
  return [i for i, x in enumerate(lst) if x == value]
```

```python
index_of_all([1, 2, 1, 4, 5, 1], 1) # [0, 2, 5]
index_of_all([1, 2, 3, 4], 6) # []
```
