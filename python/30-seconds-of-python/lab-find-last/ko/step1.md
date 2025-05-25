# 마지막 일치 값 찾기

리스트 `lst`와 테스트 함수 `fn`을 인자로 받는 함수 `find_last(lst, fn)`을 작성하십시오. 이 함수는 `fn`이 `True`를 반환하는 `lst`의 마지막 요소 값을 반환해야 합니다. 테스트 함수를 만족하는 요소가 없으면 함수는 `None`을 반환해야 합니다.

이 문제를 해결하기 위해 리스트 컴프리헨션 (list comprehension) 과 `next()`를 사용하여 리스트를 역순으로 반복하고 테스트 함수를 만족하는 마지막 요소를 반환해야 합니다.

```python
def find_last(lst, fn):
  return next(x for x in lst[::-1] if fn(x))
```

```python
find_last([1, 2, 3, 4], lambda n: n % 2 == 1) # 3
```
