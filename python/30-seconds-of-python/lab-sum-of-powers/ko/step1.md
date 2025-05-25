# 거듭제곱의 합

`sum_of_powers`라는 Python 함수를 작성하세요. 이 함수는 세 개의 매개변수를 받습니다.

- `end` - 범위의 끝을 나타내는 정수 (포함)
- `power` - 범위 내 각 숫자를 거듭제곱할 지수를 나타내는 정수 (기본값은 2)
- `start` - 범위의 시작을 나타내는 정수 (기본값은 1)

이 함수는 `start`부터 `end`까지 (둘 다 포함) 모든 숫자의 거듭제곱 합을 반환해야 합니다.

이 문제를 해결하려면 다음 단계를 따르세요.

1. `range()`를 리스트 컴프리헨션 (list comprehension) 과 함께 사용하여 지정된 `power`로 거듭제곱된 원하는 범위의 요소 목록을 생성합니다.
2. `sum()`을 사용하여 값을 모두 더합니다.

```python
def sum_of_powers(end, power = 2, start = 1):
  return sum([(i) ** power for i in range(start, end + 1)])
```

```python
sum_of_powers(10) # 385
sum_of_powers(10, 3) # 3025
sum_of_powers(10, 3, 5) # 2925
```
