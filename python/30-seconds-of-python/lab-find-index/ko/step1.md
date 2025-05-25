# 일치하는 인덱스 찾기

리스트 `lst`와 테스트 함수 `fn`을 인수로 받는 함수 `find_index(lst, fn)`을 작성하십시오. 이 함수는 `fn`이 `True`를 반환하는 `lst`의 첫 번째 요소의 인덱스를 반환해야 합니다.

```python
def find_index(lst, fn):
  return next(i for i, x in enumerate(lst) if fn(x))
```

```python
find_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 0
```
