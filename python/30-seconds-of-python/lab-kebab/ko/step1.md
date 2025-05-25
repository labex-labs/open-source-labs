# 케밥 케이스 (kebabcase) 문자열

입력으로 문자열 `s`를 받아 케밥 케이스 버전의 문자열을 반환하는 Python 함수 `to_kebab_case(s)`를 작성하십시오. 이 함수는 다음 단계를 수행해야 합니다.

1. 정규 표현식 (regexp) `r"(_|-)+"`를 사용하여 `-` 또는 `_`를 공백으로 바꿉니다.
2. 문자열의 모든 단어를 일치시키고, `str.lower()`를 사용하여 소문자로 변환합니다.
3. `-`를 구분 기호로 사용하여 모든 단어를 결합합니다.

```python
from re import sub

def kebab(s):
  return '-'.join(
    sub(r"(\s|_|-)+"," ",
    sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
    lambda mo: ' ' + mo.group(0).lower(), s)).split())
```

```python
kebab('camelCase') # 'camel-case'
kebab('some text') # 'some-text'
kebab('some-mixed_string With spaces_underscores-and-hyphens')
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
kebab('AllThe-small Things') # 'all-the-small-things'
```
