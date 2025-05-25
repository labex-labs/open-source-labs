# 일치하는 값 찾기

`find(lst, fn)`이라는 함수를 작성하세요. 이 함수는 리스트 `lst`와 테스트 함수 `fn`을 인수로 받습니다. 이 함수는 `fn`이 `True`를 반환하는 `lst`의 첫 번째 요소의 값을 반환해야 합니다. 테스트 함수를 만족하는 요소가 없으면 함수는 `None`을 반환해야 합니다.

```python
def find(lst, fn):
  return next(x for x in lst if fn(x))
```

```python
find([1, 2, 3, 4], lambda n: n % 2 == 1) # 1
```
