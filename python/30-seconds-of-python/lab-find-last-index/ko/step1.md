# 마지막 일치 인덱스 찾기

리스트 `lst`와 함수 `fn`을 인수로 받는 함수 `find_last_index(lst, fn)`을 작성하십시오. 이 함수는 `fn`이 `True`를 반환하는 `lst`의 마지막 요소의 인덱스를 반환해야 합니다. 조건을 만족하는 요소가 없으면 함수는 `-1`을 반환해야 합니다.

```python
def find_last_index(lst, fn):
  return len(lst) - 1 - next(i for i, x in enumerate(lst[::-1]) if fn(x))
```

```python
find_last_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 2
```
