# 숫자 클램핑 (Clamp Number)

세 개의 매개변수를 받는 함수 `clamp_number(num, a, b)`를 작성하십시오.

- `num` (정수 또는 실수): 클램핑할 숫자
- `a` (정수 또는 실수): 범위의 하한 경계
- `b` (정수 또는 실수): 범위의 상한 경계

이 함수는 경계 값으로 지정된 포함 범위 내에서 `num`을 클램핑해야 합니다. `num`이 범위 (`a`, `b`) 내에 있으면 `num`을 반환합니다. 그렇지 않으면 범위 내에서 가장 가까운 숫자를 반환합니다.

```python
def clamp_number(num, a, b):
  return max(min(num, max(a, b)), min(a, b))
```

```python
clamp_number(2, 3, 5) # 3
clamp_number(1, -1, -5) # -1
```
