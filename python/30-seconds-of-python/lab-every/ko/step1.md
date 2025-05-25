# 모든 리스트 요소가 참인지 테스트

`every(lst, fn = lambda x: x)`라는 함수를 작성하세요. 이 함수는 리스트 `lst`와 함수 `fn`을 인수로 받습니다. 이 함수는 `fn`이 리스트의 모든 요소에 대해 `True`를 반환하면 `True`를 반환하고, 그렇지 않으면 `False`를 반환해야 합니다. 함수가 제공되지 않으면 기본적으로 항등 함수 (`lambda x: x`) 를 사용해야 합니다.

이 문제를 해결하려면 `all()` 함수를 `map()` 및 제공된 함수 `fn`과 함께 사용하여 `fn`이 리스트의 모든 요소에 대해 `True`를 반환하는지 확인해야 합니다.

```python
def every(lst, fn = lambda x: x):
  return all(map(fn, lst))
```

```python
every([4, 2, 3], lambda x: x > 1) # True
every([1, 2, 3]) # True
```
