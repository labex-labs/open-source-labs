# 중앙값 (Median)

`find_median`이라는 Python 함수를 작성하세요. 이 함수는 숫자 목록을 인수로 받아 목록의 중앙값을 반환합니다. 함수는 다음 단계를 수행해야 합니다.

1. `list.sort()`를 사용하여 목록의 숫자를 정렬합니다.
2. 중앙값을 찾습니다. 목록 길이가 홀수이면 목록의 중간 요소이고, 목록 길이가 짝수이면 중간 두 요소의 평균입니다.
3. 중앙값을 반환합니다.

함수는 문제를 직접 해결하는 내장 Python 라이브러리나 함수를 사용해서는 안 됩니다.

```python
def median(list):
  list.sort()
  list_length = len(list)
  if list_length % 2 == 0:
    return (list[int(list_length / 2) - 1] + list[int(list_length / 2)]) / 2
  return float(list[int(list_length / 2)])
```

```python
median([1, 2, 3]) # 2.0
median([1, 2, 3, 4]) # 2.5
```
