# 발생 횟수 세기

`count_occurrences(lst, val)` 함수를 작성하세요. 이 함수는 리스트 `lst`와 값 `val`을 인수로 받아서 `lst`에서 `val`의 발생 횟수를 반환합니다. 함수는 내장 `list.count()` 메서드를 사용하여 발생 횟수를 세어야 합니다.

```python
def count_occurrences(lst, val):
  return lst.count(val)
```

```python
count_occurrences([1, 1, 2, 1, 2, 3], 1) # 3
```
