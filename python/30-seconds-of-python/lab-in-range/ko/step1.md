# 범위 내 숫자

세 개의 매개변수를 받는 함수 `in_range(n, start, end = 0)`을 작성하십시오.

- `n`: 범위 내에 속하는지 확인할 숫자
- `start`: 범위의 시작
- `end`: 범위의 끝 (선택 사항, 기본값은 0)

함수는 주어진 숫자 `n`이 지정된 범위 내에 속하면 `True`를 반환하고, 그렇지 않으면 `False`를 반환해야 합니다. `end` 매개변수가 지정되지 않은 경우, 범위는 `0`부터 `start`까지로 간주됩니다.

```python
def in_range(n, start, end = 0):
  return start <= n <= end if end >= start else end <= n <= start
```

```python
in_range(3, 2, 5) # True
in_range(3, 4) # True
in_range(2, 3, 5) # False
in_range(3, 2) # False
```
