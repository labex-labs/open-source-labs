# 문자열 패딩 (Pad String)

`pad(s: str, length: int, char: str = ' ') -> str` 함수를 작성하여 지정된 길이보다 짧은 문자열을 양쪽에서 지정된 문자로 패딩합니다. 이 함수는 세 가지 매개변수를 받습니다.

- `s`: 패딩이 필요한 문자열
- `length`: 패딩된 문자열의 총 길이를 지정하는 정수
- `char`: 문자열을 패딩하는 데 사용되는 문자. 기본값은 공백 문자입니다.

이 함수는 패딩된 문자열을 반환해야 합니다.

```python
from math import floor

def pad(s, length, char = ' '):
  return s.rjust(floor((len(s) + length)/2), char).ljust(length, char)
```

```python
pad('cat', 8) # '  cat   '
pad('42', 6, '0') # '004200'
pad('foobar', 3) # 'foobar'
```
