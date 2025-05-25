# 피보나치 (Fibonacci)

정수 `n`을 매개변수로 받아 n 번째 항까지의 피보나치 수열을 포함하는 리스트를 반환하는 `fibonacci(n)`이라는 함수를 작성하십시오.

이 문제를 해결하려면 다음 단계를 따르세요.

1. `sequence`라는 빈 리스트를 생성합니다.
2. `n`이 0 보다 작거나 같으면 `sequence` 리스트에 0 을 추가하고 리스트를 반환합니다.
3. `sequence` 리스트에 0 과 1 을 추가합니다.
4. `sequence` 리스트의 마지막 두 숫자의 합을 리스트 끝에 추가하는 while 루프를 사용하여 리스트의 길이가 `n`에 도달할 때까지 반복합니다.
5. `sequence` 리스트를 반환합니다.

```python
def fibonacci(n):
  if n <= 0:
    return [0]
  sequence = [0, 1]
  while len(sequence) <= n:
    next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
    sequence.append(next_value)
  return sequence
```

```python
fibonacci(7) # [0, 1, 1, 2, 3, 5, 8, 13]
```
