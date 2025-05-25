# 리스트 요소 중 일부가 참인지 테스트

리스트 `lst`와 함수 `fn`을 인수로 받는 함수 `some(lst, fn)`을 작성하십시오. 이 함수는 함수 `fn`이 리스트 `lst` 내의 최소한 하나의 요소에 대해 `True`를 반환하는 경우 `True`를 반환해야 합니다. 리스트 내의 어떤 요소도 조건을 만족하지 않으면 함수는 `False`를 반환해야 합니다. 함수가 제공되지 않으면 함수는 항등 함수 (요소 자체를 반환하는 함수) 를 사용해야 합니다.

```python
def some(lst, fn = lambda x: x):
  return any(map(fn, lst))
```

```python
some([0, 1, 2, 0], lambda x: x >= 2 ) # True
some([0, 0, 1, 0]) # True
```
