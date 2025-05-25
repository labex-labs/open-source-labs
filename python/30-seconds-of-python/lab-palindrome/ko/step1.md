# 회문 (Palindrome)

문자열 `s`를 유일한 매개변수로 받아 `s`가 회문이면 `True`를, 그렇지 않으면 `False`를 반환하는 함수 `palindrome(s)`를 작성하십시오. 회문을 확인할 때 대소문자와 영숫자가 아닌 문자는 무시해야 합니다.

이 문제를 해결하려면 다음 단계를 따를 수 있습니다.

1. `str.lower()`를 사용하여 문자열을 소문자로 변환합니다.
2. `re.sub()`를 사용하여 문자열에서 모든 영숫자가 아닌 문자를 제거합니다.
3. 슬라이스 표기법을 사용하여 결과 문자열을 뒤집은 문자열과 비교합니다.

```python
from re import sub

def palindrome(s):
  s = sub('[\W_]', '', s.lower())
  return s == s[::-1]
```

```python
palindrome('taco cat') # True
```
