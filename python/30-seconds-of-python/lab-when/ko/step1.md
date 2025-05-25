# 참일 때 함수 적용

`when`이라는 함수를 작성하세요. 이 함수는 두 개의 인수를 받습니다: 술어 함수 `predicate`와 적용할 함수 `when_true`. `when` 함수는 단일 인수 `x`를 받는 새로운 함수를 반환해야 합니다. 새로운 함수는 `predicate(x)`의 값이 `True`인지 확인해야 합니다. 만약 그렇다면, 새로운 함수는 `when_true(x)`를 호출하고 그 결과를 반환해야 합니다. 그렇지 않으면, 새로운 함수는 `x`를 반환해야 합니다.

```python
def when(predicate, when_true):
  return lambda x: when_true(x) if predicate(x) else x
```

```python
double_even_numbers = when(lambda x: x % 2 == 0, lambda x : x * 2)
double_even_numbers(2) # 4
double_even_numbers(1) # 1
```
