# 팩토리얼 (Factorial)

음이 아닌 정수 `num`을 인수로 받아 팩토리얼을 반환하는 함수 `factorial(num)`을 작성하십시오. 이 함수는 재귀 (recursion) 를 사용하여 팩토리얼을 계산해야 합니다. `num`이 1 보다 작거나 같으면 `1`을 반환합니다. 그렇지 않으면 `num`과 `num - 1`의 팩토리얼의 곱을 반환합니다. `num`이 음수 또는 부동 소수점 숫자이면 예외 (exception) 를 발생시켜야 합니다.

```python
def factorial(num):
  if not ((num >= 0) and (num % 1 == 0)):
    raise Exception("Number can't be floating point or negative.")
  return 1 if num == 0 else num * factorial(num - 1)
```

```python
factorial(6) # 720
```
