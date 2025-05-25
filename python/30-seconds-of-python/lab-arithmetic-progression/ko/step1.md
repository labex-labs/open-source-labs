# 등차수열 (Arithmetic Progression)

두 개의 양의 정수 `n`과 `lim`을 입력받아 `n`에서 시작하여 `lim`까지의 등차수열의 숫자 목록을 반환하는 함수 `arithmetic_progression(n, lim)`을 작성하십시오. 이 함수는 목록을 생성하기 위해 적절한 시작 값, 단계 값 및 종료 값을 사용하여 `range()`와 `list()`를 사용해야 합니다.

### 입력 (Input)

- 두 개의 양의 정수 `n`과 `lim`이며, 여기서 `n`은 시작 숫자이고 `lim`은 제한 값입니다.

### 출력 (Output)

- `n`에서 시작하여 `lim`까지의 등차수열의 숫자 목록입니다.

```python
def arithmetic_progression(n, lim):
  return list(range(n, lim + 1, n))
```

```python
arithmetic_progression(5, 25) # [5, 10, 15, 20, 25]
```
