# 가장 빈번한 요소

정수 목록을 입력으로 받아 목록에서 가장 빈번하게 나타나는 요소를 반환하는 `most_frequent(lst)`라는 Python 함수를 작성하십시오. 동일한 횟수로 나타나고 가장 높은 빈도를 가진 요소가 여러 개인 경우 목록에서 먼저 나타나는 요소를 반환합니다.

이 문제를 해결하려면 다음 단계를 따를 수 있습니다.

1. `set()`을 사용하여 `lst`의 고유한 값을 가져옵니다.
2. `max()`를 사용하여 가장 많이 나타나는 요소를 찾습니다.

함수는 다음과 같은 시그니처를 가져야 합니다.

```python
def most_frequent(lst: List[int]) -> int:
```

```python
def most_frequent(lst):
  return max(set(lst), key = lst.count)
```

```python
most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]) #2
```
