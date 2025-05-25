# 문자열을 슬러그로 변환하기

문자열 `s`를 인수로 받아 슬러그를 반환하는 함수 `slugify(s)`를 작성하십시오. 이 함수는 다음 작업을 수행해야 합니다.

1. 문자열을 소문자로 변환하고 선행 및 후행 공백을 제거합니다.
2. 모든 특수 문자 (즉, 문자, 숫자, 공백, 하이픈 또는 밑줄이 아닌 모든 문자) 를 빈 문자열로 바꿉니다.
3. 모든 공백, 하이픈 및 밑줄을 단일 하이픈으로 바꿉니다.
4. 선행 또는 후행 하이픈을 제거합니다.

```python
import re

def slugify(s):
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$', '', s)
  return s
```

```python
slugify('Hello World!') # 'hello-world'
```
