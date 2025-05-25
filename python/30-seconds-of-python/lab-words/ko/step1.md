# 문자열을 단어로

문자열 `s`와 선택적 `pattern` 문자열을 인수로 받아 문자열의 단어 목록을 반환하는 함수 `string_to_words(s: str, pattern: str = '[a-zA-Z-]+') -> List[str]`을 작성하십시오.

- 함수는 제공된 `pattern`을 사용하여 `re.findall()`을 호출하여 일치하는 모든 부분 문자열을 찾아야 합니다.
- `pattern` 인수가 제공되지 않으면 함수는 기본 정규 표현식 (regexp) 을 사용해야 하며, 이는 영숫자와 하이픈에 일치합니다.

```python
import re

def words(s, pattern = '[a-zA-Z-]+'):
  return re.findall(pattern, s)
```

```python
words('I love Python!!') # ['I', 'love', 'Python']
words('python, javaScript & coffee') # ['python', 'javaScript', 'coffee']
words('build -q --out one-item', r'\b[a-zA-Z-]+\b')
# ['build', 'q', 'out', 'one-item']
```
