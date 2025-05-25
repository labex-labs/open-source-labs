# 문자열 애너그램 (String Anagram)

두 문자열을 인수로 받아 서로의 애너그램이면 `True`를, 그렇지 않으면 `False`를 반환하는 함수 `is_anagram(s1, s2)`를 작성하십시오. 이 함수는 대소문자를 구분하지 않으며, 공백, 구두점 및 특수 문자를 무시해야 합니다.

이 문제를 해결하려면 다음 단계를 따를 수 있습니다.

1. `str.isalnum()`을 사용하여 영숫자가 아닌 문자를 필터링하고, `str.lower()`를 사용하여 각 문자를 소문자로 변환합니다.
2. `collections.Counter`를 사용하여 각 문자열에 대한 결과 문자를 세고 결과를 비교합니다.

```python
from collections import Counter

def is_anagram(s1, s2):
  return Counter(
    c.lower() for c in s1 if c.isalnum()
  ) == Counter(
    c.lower() for c in s2 if c.isalnum()
  )
```

```python
is_anagram('#anagram', 'Nag a ram!')  # True
```
