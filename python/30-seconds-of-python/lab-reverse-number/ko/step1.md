# 숫자 뒤집기

`reverse_number(n)` 함수를 작성하세요. 이 함수는 숫자를 인수로 받아 해당 숫자를 뒤집은 값을 반환합니다. 이 함수는 다음 요구 사항을 충족해야 합니다.

- 함수는 양수 또는 음수 여부에 관계없이 숫자를 뒤집어야 합니다.
- 입력이 float 인 경우 float 를 반환하고, 입력이 integer 인 경우 integer 를 반환해야 합니다.
- 숫자를 직접 뒤집는 내장 함수 (예: `reversed()`) 를 사용해서는 안 됩니다.
- 숫자를 문자열로 직접 변환하는 내장 함수 (예: `str()`) 를 사용해서는 안 됩니다.
- 문자열을 숫자로 직접 변환하는 내장 함수 (예: `int()` 또는 `float()`) 를 사용해서는 안 됩니다.

```python
from math import copysign

def reverse_number(n):
  return copysign(float(str(n)[::-1].replace('-', '')), n)
```

```python
reverse_number(981) # 189
reverse_number(-500) # -5
reverse_number(73.6) # 6.37
reverse_number(-5.23) # -32.5
```
