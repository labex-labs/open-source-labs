# 숫자가 나누어 떨어짐

두 개의 정수를 인수로 받아 `dividend`가 `divisor`로 나누어 떨어지면 `True`를 반환하고, 그렇지 않으면 `False`를 반환하는 함수 `is_divisible(dividend, divisor)`를 작성하십시오.

```python
def is_divisible(dividend, divisor):
  return dividend % divisor == 0
```

```python
is_divisible(6, 3) # True
```
